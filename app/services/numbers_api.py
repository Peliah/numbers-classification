import httpx
from app.core.config import settings

class NumbersAPIClient:
    @staticmethod
    async def get_fun_fact(num: int) -> str:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{settings.NUMBERS_API_BASE_URL}/{num}/math"
                )
                return response.text
            except:
                return f"{num} is an interesting number with various mathematical properties."