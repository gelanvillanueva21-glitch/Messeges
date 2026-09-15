
from fastapi import FastAPI


# Routes
from app.api.auth import route as auth_routh


app = FastAPI(title="Simple-Messenger")




app.include_router(auth_routh)


