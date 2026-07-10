def add(*numbers):
    return sum(numbers)


def mul(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def sub(*numbers):
    if not numbers:
        return 0

    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def div(a, b):
    return a / b