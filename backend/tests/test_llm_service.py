from app.services.llm_service import (
    LLMService
)

llm = LLMService()

response = llm.generate_response(
    "Explain FastAPI in 50 words."
)

print(response)