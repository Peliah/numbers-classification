from fastapi import APIRouter, Query
from app.models.responses import NumberClassification, ErrorResponse
from app.services.number_classifier import NumberClassifier
from app.services.numbers_api import NumbersAPIClient
from app.core.exceptions import InvalidInputError
from typing import Union 

router = APIRouter()

@router.get("/classify-number", 
    response_model=Union[NumberClassification,ErrorResponse],
    responses={400: {"model": ErrorResponse}})
async def classify_number(
    number: str = Query(..., description="The number to classify")
):
    try:
        num = int(number)
        print(num ," is a number")
    except ValueError:
        print(number ," is not a number")
        return ErrorResponse(number=number)
    
    classifier = NumberClassifier()
    
    return NumberClassification(
        number=num,
        is_prime=classifier.is_prime(num),
        is_perfect=classifier.is_perfect(num),
        properties=classifier.get_properties(num),
        digit_sum=classifier.get_digit_sum(num),
        fun_fact=await NumbersAPIClient.get_fun_fact(num)
    )
