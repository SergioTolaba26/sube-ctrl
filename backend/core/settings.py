PROJECT_NAME = "SUBE Control"

from pathlib import Path


class Settings:
    """Configuración global del proyecto."""

    BASE_DIR = Path(__file__).resolve().parent.parent

    STORAGE_PATH = BASE_DIR / "storage" / "json"


settings = Settings()