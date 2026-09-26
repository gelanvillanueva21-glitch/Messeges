
import sys
from pathlib import Path

# Ensure backend directory is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.utils.save_image import DATA_DIR

# Routes
from app.api.auth import route as auth_route
from app.api.message import router as message_route


app = FastAPI(title="Simple-Messenger")

DATA_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/data", StaticFiles(directory=DATA_DIR), name="data")

app.include_router(auth_route)
app.include_router(message_route)



