"""Optional chat web UI route, served at GET /chat."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, Response

from .common import get_services

router = APIRouter()


@router.get("/chat", include_in_schema=False)
async def chat_ui(request: Request) -> Response:
    svc = get_services(request)
    if not svc.settings.enable_chat_ui:
        return Response(status_code=404)
    from ..chat_ui import CHAT_HTML
    return HTMLResponse(CHAT_HTML)
