'''
написати додаток що буде сдідкувати за фінансами

за тиждень буду витрачати: 1000
за понеділок: 100
за вівторок: 200
...

чи я вилетів за бюджет і в який день я витрачав найбільше

'''

# Поки користувач не ввів вірне число, питати нове

while True:
    try:
        weeklt_budget = float(input("Please enter budget for a week!"))
        print("Entered a correct value") # !

    except ValueError:
        print("Please enter a new value, this one is wrong")

print("End of program!")
