from webbrowser import open_new_tab


def calculate(func):
    def wrapper(*args, **kwargs):
        first, second = args
        operation = kwargs.get('operation')
        if first == second:
            result = first + second
        elif first > second:
            result = second - first
        elif first < second:
            result = first / second
        elif first < 0 or second < 0:
            result = first * second
        else:
            result = "Numbers are not correct"
        return result
    return wrapper


first = int(input("Первая цифра: "))
second = int(input("Вторая цифра: "))


@calculate
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '/':
        return first % second
    elif operation == '*':
        return first * second
    elif operation == '-':
        return second - first


result = calc(first, second, operation='+')
print(f"Результат: {result}")
