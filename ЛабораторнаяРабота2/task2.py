salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05  # Ежемесячный рост цен

capital = 0

for i in range(months):
    delta = spend * ((1 + increase) ** i) - salary
    capital += delta

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(capital))
