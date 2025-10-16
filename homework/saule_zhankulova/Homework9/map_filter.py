temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]

hot_days = filter(lambda x: x > 28, temperatures)
hot_days1 = sorted(hot_days)
print(hot_days1)
print(f'Максимальная температура: {max(hot_days1)}')
print(f'Минимальная температцра: {min(hot_days1)}')
print(f'Средняя температура: {round(sum(hot_days1) / len(hot_days1))}')
