results = "результат операции: 42"
colon_index = results.index(':')
number_index = results[colon_index + 2:]
print(int(number_index) + 10)

results1 = "результат операции: 514"
colon_index = results1.index(':')
number_index = results1[colon_index + 2:]
print(int(number_index) + 10)

results2 = "результат работы программы: 9"
colon_index = results2.index(':')
number_index = results2[colon_index + 2:]
print(int(number_index) + 10)
