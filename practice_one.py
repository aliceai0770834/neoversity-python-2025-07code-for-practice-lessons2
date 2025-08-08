'''
написати додаток що буде сдідкувати за фінансами

за тиждень буду витрачати: 1000
за понеділок: 100
за вівторок: 200
...

чи я вилетів за бюджет і в який день я витрачав найбільше

'''


# який спланований бюджет на тиждень
try:
    weeklt_budget = float(input("Please enter budget for a week!")) # 100.1 100
except ValueError:
    print("You have entered a wrong value, using a default value: 1000")
    weekly_burget = 1000 # TODO: clear non-numeric values
print(weekly_burget / 10)

