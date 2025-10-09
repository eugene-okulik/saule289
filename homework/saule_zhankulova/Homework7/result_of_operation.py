result0 = "результат операции: 42"
result1 = "результат операции: 514"
result2 = "результат работы программы: 2"
result3 = "результат: 2"

def result_of_operation(result):
    colon_index = result.index(':')
    number_index = result[colon_index + 2:]
    print(int(number_index) + 10)

result_of_operation(result = result0)
result_of_operation(result = result1)
result_of_operation(result = result2)
result_of_operation(result = result3)
