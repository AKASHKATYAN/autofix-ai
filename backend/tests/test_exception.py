import asyncio
from fastapi import Request

from app.exceptions.custom_exceptions import (
    RepositoryNotFoundException
)
from app.exceptions.exception_handler import (
    autofix_exception_handler
)


class MockRequest:
    method = "GET"

    class URL:
        path = "/test"

    url = URL()


async def main():
    exc = RepositoryNotFoundException(
        "Repository not found",
        404
    )

    response = await autofix_exception_handler(
        MockRequest(),
        exc
    )

    print("Status Code:", response.status_code)
    print("Body:", response.body.decode())


asyncio.run(main())