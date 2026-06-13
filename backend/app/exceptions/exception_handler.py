from fastapi import Request
from fastapi.responses import JSONResponse

from app.logging import logger
from app.exceptions.custom_exceptions import AutoFixException


# ==================================================
# AutoFix Custom Exception Handler
# ==================================================

async def autofix_exception_handler(
    request: Request,
    exc: AutoFixException
):
    """
    Handles all project-specific exceptions.
    """

    logger.error(
        f"[{exc.__class__.__name__}] "
        f"{request.method} "
        f"{request.url.path} "
        f"- {exc.message}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.__class__.__name__,
            "message": exc.message
        }
    )


# ==================================================
# Generic Exception Handler
# ==================================================

async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    """
    Handles unexpected exceptions.
    """

    logger.exception(
        f"Unhandled Exception: "
        f"{request.method} "
        f"{request.url.path}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "InternalServerError",
            "message": "An unexpected error occurred."
        }
    )