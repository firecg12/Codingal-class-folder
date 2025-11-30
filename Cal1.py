from datetime import datetime
import calendar

current_year = datetime.now().year



for month in range(1, 13):
    print(calendar.month(current_year, month))


for year in range(2000, current_year + 1):
    print(calendar.calendar(year))


for day in range(1, 32):
    print(f"Day: {day}")


