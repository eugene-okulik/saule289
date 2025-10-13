import sys

sys.set_int_max_str_digits(1000000)

def fibonachchi():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


count = 0
numbers = [5, 10, 200, 1000, 100000]


for i in fibonachchi():
    count += 1
    if count in numbers:
        print(i)
        continue
    if count >= max(numbers):
        break
