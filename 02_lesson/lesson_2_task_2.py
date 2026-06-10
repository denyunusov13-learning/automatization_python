def is_year_leap(year):
    return int(year) % 4 == 0


year = input("Введите год: ")
res = is_year_leap(year)
print("Год " + str(year) + ": " + str(res))
