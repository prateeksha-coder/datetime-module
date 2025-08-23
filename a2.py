import calendar
obj=calendar.Calendar()
print(obj.monthdatescalendar(2021,8),"\n\n")

print(obj.monthdays2calendar(2021,8),"\n\n")
print(obj.monthdayscalendar(2021,8),"\n\n")
print(calendar.calendar(2025))

cal = calendar.Calendar()
for day in cal.itermonthdays(2025, 8):
    print(day)