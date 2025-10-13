import random


def calculate_bonus():


    salary = int(input("What is your salary? "))
    solution = [True, False]
    bonus = random.choice(solution)


    if bonus:
        change_salary = salary * random.randint(10, 100)
        print(f"\u2022 {salary}, {bonus} - '${change_salary}'")
        print(f'Your salary will be {change_salary}')
    else:
        print(f"\u2022 {salary}, {bonus} - '${salary}'")
        print(f'Your salary is not changed')

calculate_bonus()
