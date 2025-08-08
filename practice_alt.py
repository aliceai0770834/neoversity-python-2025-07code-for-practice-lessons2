'''
написати додаток що буде сдідкувати за фінансами

за тиждень буду витрачати: 1000
за понеділок: 100
за вівторок: 200
...

чи я вилетів за бюджет і в який день я витрачав найбільше

'''

def try_getting_number_from_user(promt):  # оголошення функції defenation
    while True:
        try:
            weekly_budget = float(input(promt))
            print("Entered a correct value") # !
            return weekly_budget
        except ValueError:
            print("Please enter a new value, this one is wrong")

        print("End of program!")


# Поки користувач не ввів вірне число, питати нове

# while True:
#     try:
#         weeklt_budget = float(input("Please enter budget for a week!"))
#         print("Entered a correct value") # !

#     except ValueError:
#         print("Please enter a new value, this one is wrong")

# print("End of program!")

weekly_budget = try_getting_number_from_user("Please enter budget for a week!")
print(f"Budget of the week is {weekly_budget}")

# list, tuple, dict, set

# set (100, 200, 300) -> no order, not recomend

# l = (100, 200, 300) - Monday, l[1] - Recomended

# t = (100, 200, 300) -> Not recomended, fixed value

# d = (0: 100, 1: 200)

# d = ("Monday": 100, "Tuesday: 200")
# spends = {'Monday': 100, 'Tuesday': 200}

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saterday', 'Sunday']
money_spent_during_the_week = []

# for i in range(0, 7): # 0, 1, 2, 3, 4, 5, 6, 7
for i in range(7):
    day = weekdays[i]
    money_spent_during_the_week.append(try_getting_number_from_user(f"Please enter money spend on {day}: "))

# Monday
# money_spent_during_the_week.append(try_getting_number_from_user("Please enter money spend on Monday: "))
# Tuesday# 
# money_spent_during_the_week.append(try_getting_number_from_user("Please enter money spend on Tuesday: "))
# Wednessday# 
# money_spent_during_the_week.append(try_getting_number_from_user("Please enter money spend on Wednesday: "))
# 
# print(money_spent_during_the_week)

# spending = (monday_money_spent, tuesday_money_spent, wednesday_money_spent)

