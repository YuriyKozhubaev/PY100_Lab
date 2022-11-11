money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital - spend > 0:
    month += 1
    money_capital += salary - spend
    spend *= increase + 1

print(month)

def month_for_live(money_capital, salary, spend, increase, month=0):
    while money_capital - spend + salary > 0:
        money_capital += salary - spend
        spend *= 1 + increase
        month += 1
    return month

# print(month_for_live(10000, salary, 6000, increase))