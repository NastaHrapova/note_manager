date = int(input("Введите число дедлайна: "))
month = int(input('Введите месяц(числом) дедлайна: '))
year = 2025
today = 1
now = 1
age = int(date - today)
ager = int(month - now)
print(f"Осталось {age} дней и {ager} месяцев!")