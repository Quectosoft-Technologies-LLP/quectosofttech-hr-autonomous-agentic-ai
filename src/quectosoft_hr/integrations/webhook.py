from fastapi import APIRouter, Request
router = APIRouter()
@router.post("/webhook/{service}")
async def ingest(service: str, request: Request):
    payload = await request.json()
    return {"received": True, "service": service, "payload_keys": list(payload.keys())}
