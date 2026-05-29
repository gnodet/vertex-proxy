"""Configuration loaded from environment variables."""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration for vertex-proxy."""

    model_config = SettingsConfigDict(
        env_prefix="VERTEX_PROXY_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- GCP ---
    credentials_path: Path | None = None
    project_id: str | None = None
    anthropic_region: str = "us-east5"
    gemini_region: str = "us-central1"

    # --- Server ---
    host: str = "127.0.0.1"
    port: int = 8787
    log_level: str = "info"
    api_key: str | None = None
    metrics_enabled: bool = False

    # --- Auth refresh ---
    token_refresh_seconds: int = 3000

    # --- Model aliases ---
    anthropic_model_aliases: dict[str, str] = {
        # Opus 4.8
        "claude-opus-4-8": "claude-opus-4-8",
        # Opus 4.7
        "claude-opus-4-7": "claude-opus-4-7",
        # Opus 4.6
        "claude-opus-4-6": "claude-opus-4-6",
        # Sonnet 4.6
        "claude-sonnet-4-6": "claude-sonnet-4-6",
        # Sonnet 4.5
        "claude-sonnet-4-5": "claude-sonnet-4-5@20250929",
        "claude-sonnet-4-5-20250929": "claude-sonnet-4-5@20250929",
        # Opus 4.5
        "claude-opus-4-5": "claude-opus-4-5@20250929",
        "claude-opus-4-5-20250929": "claude-opus-4-5@20250929",
        # Sonnet 4
        "claude-sonnet-4-20250514": "claude-sonnet-4-20250514",
        # Haiku 4.5
        "claude-haiku-4-5": "claude-haiku-4-5@20250929",
        "claude-haiku-4-5-20250929": "claude-haiku-4-5@20250929",
    }

    gemini_model_aliases: dict[str, str] = {
        "gemini-2.5-pro": "gemini-2.5-pro",
        "gemini-2.5-flash": "gemini-2.5-flash",
        "gemini-2.0-flash": "gemini-2.0-flash-001",
    }

    maas_region: str = "us-central1"

    maas_model_aliases: dict[str, str] = {
        "kimi-k2.5": "publishers/moonshotai/models/kimi-k2.5",
        "kimi-k2": "publishers/moonshotai/models/kimi-k2",
        "glm-5": "publishers/zhipu/models/glm-5",
        "glm-5.1": "publishers/zhipu/models/glm-5.1",
        "glm-4.6": "publishers/zhipu/models/glm-4.6",
        "minimax-m2.5": "publishers/minimax/models/minimax-m2.5",
        "minimax-m1": "publishers/minimax/models/minimax-m1",
        "qwen3.5": "publishers/qwen/models/qwen3.5",
        "qwen-3": "publishers/qwen/models/qwen-3",
        "grok-4.20": "publishers/xai/models/grok-4.20",
        "grok-4.1-fast": "publishers/xai/models/grok-4.1-fast",
    }


def load_settings() -> Settings:
    return Settings()
