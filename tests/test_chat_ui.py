"""Unit tests for the chat web UI endpoint."""

from __future__ import annotations

from collections.abc import Callable

from fastapi.testclient import TestClient


def test_chat_endpoint_returns_html(make_client: Callable[..., TestClient]) -> None:
    """The /chat endpoint returns an HTML page when enabled (default)."""
    client = make_client(enable_chat_ui=True)
    resp = client.get("/chat")
    assert resp.status_code == 200
    assert "text/html" in resp.headers["content-type"]
    assert "vertex-proxy" in resp.text
    assert "<script>" in resp.text


def test_chat_endpoint_disabled(make_client: Callable[..., TestClient]) -> None:
    """The /chat endpoint returns 404 when disabled."""
    client = make_client(enable_chat_ui=False)
    resp = client.get("/chat")
    assert resp.status_code == 404
