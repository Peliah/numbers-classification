import math
from typing import List

class NumberClassifier:
    @staticmethod
    def is_armstrong(num: int) -> bool:
        num = abs(num)
        str_num = str(num)
        power = len(str_num)
        return num == sum(int(digit) ** power for digit in str_num)

    @staticmethod
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def is_perfect(num: int) -> bool:
        if num < 2:
            return False
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        return divisors_sum == num

    @staticmethod
    def get_digit_sum(num: int) -> int:
        num = abs(num)
        return sum(int(digit) for digit in str(num))

    @staticmethod
    def get_properties(num: int) -> List[str]:
        properties = []
        if NumberClassifier.is_armstrong(num):
            properties.append("armstrong")
        properties.append("odd" if num % 2 else "even")
        return properties