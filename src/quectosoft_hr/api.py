import asyncio
from typing import Any
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect, Header, Query
from pydantic import BaseModel
from prometheus_client import make_asgi_app
from quectosoft_hr.config.settings import get_settings
from quectosoft_hr.core.project_manager import GLOBAL_PROJECT_MANAGER
from quectosoft_hr.core.live_events import GLOBAL_LIVE_HUB
from quectosoft_hr.raid.raid_store import GLOBAL_RAID_STORE

settings = get_settings()
app = FastAPI(title='Quectosoft HR Agentic AI', version='0.3.2')
app.mount('/metrics', make_asgi_app())

class ProjectRequest(BaseModel):
    client_id: str
    objective: str
    budget: int = 0
    timeline_days: int = 0
    domain: str = 'general'
    privacy_level: str = 'standard'

def require_api_key(x_api_key):
    if x_api_key not in settings.api_keys:
        raise HTTPException(status_code=401, detail='invalid api key')

def validate_ws_token(token: str | None):
    if token not in settings.api_keys:
        raise HTTPException(status_code=401, detail='invalid websocket token')

@app.get('/v1/health')
async def health() -> dict[str, Any]:
    return {'status': 'ok', 'version': '0.3.2'}

@app.get('/v1/catalog')
async def catalog(x_api_key: str | None = Header(default=None)):
    require_api_key(x_api_key)
    return GLOBAL_PROJECT_MANAGER.list_catalog()

@app.get('/v1/raid')
async def raid(x_api_key: str | None = Header(default=None)):
    require_api_key(x_api_key)
    return {'summary': GLOBAL_RAID_STORE.summary(), 'entries': GLOBAL_RAID_STORE.all()[-50:]}

@app.post('/v1/projects')
async def create_project(req: ProjectRequest, x_api_key: str | None = Header(default=None)):
    require_api_key(x_api_key)
    return await GLOBAL_PROJECT_MANAGER.create_project(req.model_dump())

@app.get('/v1/projects/{project_id}')
async def get_project(project_id: str, x_api_key: str | None = Header(default=None)):
    require_api_key(x_api_key)
    project = GLOBAL_PROJECT_MANAGER.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail='project not found')
    return project

@app.websocket('/v1/projects/{project_id}/stream')
async def project_stream(websocket: WebSocket, project_id: str, token: str | None = Query(default=None)):
    try:
        validate_ws_token(token)
    except HTTPException:
        await websocket.close(code=1008)
        return
    await websocket.accept()
    queue = await GLOBAL_LIVE_HUB.subscribe(project_id)
    try:
        while True:
            try:
                event = await asyncio.wait_for(queue.get(), timeout=15)
                await websocket.send_json(event)
            except asyncio.TimeoutError:
                await websocket.send_json({'type': 'heartbeat', 'project_id': project_id})
    except WebSocketDisconnect:
        pass
    finally:
        GLOBAL_LIVE_HUB.unsubscribe(project_id, queue)
