from typing import Callable
from decimal import Decimal
import re


def generator_numbers(text: str):
    pattern = r'(\d+\.\d{2})'
    for elem in re.findall(pattern, text):
        yield Decimal(elem)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

if __name__ == '__main__':
    txt = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'
    print(sum_profit(txt, generator_numbers))