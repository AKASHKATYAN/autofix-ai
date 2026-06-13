import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.logging import logger


class RequestLoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next
    ):
        start_time = time.time()

        response = await call_next(request)

        process_time = round(
            time.time() - start_time,
            4
        )

        logger.info(
        f"Client={request.client.host} "
        f"Method={request.method} "
        f"Path={request.url.path} "
        f"Status={response.status_code} "
        f"Time={process_time}s"
    )
        return response