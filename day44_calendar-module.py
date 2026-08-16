import calendar

month, day, year = map(int, input("Enter month day year: ").split())

print(calendar.day_name[calendar.weekday(year, month, day)].upper())