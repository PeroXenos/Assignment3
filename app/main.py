from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="E-Commerce API")


app.include_router(router)

@app.get("/")
def home():
    return {"message": "E-Commerce API is running!"}
