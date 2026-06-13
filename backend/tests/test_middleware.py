from fastapi import FastAPI

from app.middleware import RequestLoggerMiddleware

app = FastAPI()

app.add_middleware(
    RequestLoggerMiddleware
)


@app.get("/")
async def root():
    return {
        "message": "Middleware Working"
    }