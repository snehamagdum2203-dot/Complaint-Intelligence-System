from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "complaints.db"

SECRET_KEY = "dev-secret-key"