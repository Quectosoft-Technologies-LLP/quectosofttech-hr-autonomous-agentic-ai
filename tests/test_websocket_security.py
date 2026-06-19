from pathlib import Path

def test_websocket_route_requires_token_logic_present():
    text = Path('src/quectosoft_hr/api.py').read_text(encoding='utf-8')
    assert 'invalid websocket token' in text
    assert 'token: str | None = Query' in text
