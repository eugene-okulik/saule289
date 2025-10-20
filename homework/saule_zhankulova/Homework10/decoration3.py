def calculate(func):
    def wrapper(*args, **kwargs):
        first, second = args
        operation = ''
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation=operation)
    return wrapper


first = int(input("Первая цифра: "))
second = int(input("Вторая цифра: "))


@calculate
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    elif operation == '-':
        return second - first


result = calc(first, second)
print(f"Результат: {result}")
