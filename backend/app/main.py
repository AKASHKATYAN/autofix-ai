from fastapi import FastAPI

from app.core.config import settings

from app.middleware import RequestLoggerMiddleware

from app.exceptions.custom_exceptions import AutoFixException

from app.exceptions.exception_handler import (
    autofix_exception_handler,
    generic_exception_handler
)

from app.logging import logger
from app.api import api_router


# ==================================================
# App
# ==================================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# ==================================================
# Middleware
# ==================================================

app.add_middleware(
    RequestLoggerMiddleware
)

# ==================================================
# Exception Handlers
# ==================================================

app.add_exception_handler(
    AutoFixException,
    autofix_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(
    api_router
)
# ==================================================
# Startup
# ==================================================

async def lifespan(app: FastAPI):
    # Startup logic
    logger.info(f"{settings.APP_NAME} started successfully.")
    yield
    # Shutdown logic
    logger.info(f"{settings.APP_NAME} stopped.")