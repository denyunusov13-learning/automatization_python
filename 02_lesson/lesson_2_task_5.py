seasons = ["Зима", "Весна", "Лето", "Осень"]


def month_to_season(num_month):
    if num_month == 1 or num_month == 2 or num_month == 12:
        print(seasons[0])
    elif num_month == 3 or num_month == 4 or num_month == 5:
        print(seasons[1])
    elif num_month == 6 or num_month == 7 or num_month == 8:
        print(seasons[2])
    elif num_month == 9 or num_month == 10 or num_month == 11:
        print(seasons[3])
    else:
        print("Это не номер месяца, введите число от 1 до 12.")


num_month = int(input("Введите номер месяца: "))
month_to_season(num_month)
