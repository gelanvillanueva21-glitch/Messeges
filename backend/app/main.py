
import sys
from pathlib import Path

# Ensure backend directory is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI


# Routes
from app.api.auth import route as auth_routh


app = FastAPI(title="Simple-Messenger")




app.include_router(auth_routh)


