from fastapi import FastAPI
from app.api.route.user_routers import router as user_router

app = FastAPI()
app.include_router(user_router)


@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI!"}
