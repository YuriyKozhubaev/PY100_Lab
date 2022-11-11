salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# log = []
# цикл для расчёта трат в текущем месяце и занесение их в список трат
for current_months in range(months):
    if current_months >= 1:     # рост цен со второго месяца (у нас отсчёт с нулевого)
        spend *= 1 + increase # переприсваеваем траты, так как рост цен динамический
    need_money += spend - salary
    # log.append(need_money)

print(round(need_money))
# print(log)
# print(sum(log))