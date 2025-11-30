from datetime import date,time,datetime

date_today = date.today()
date_now = datetime.now()
time_now = datetime.now().time()
print("Today's date:", date_today)
print("Current date and time:", date_now)
print("Current time:", time_now)

print(f"Year: {date_today.year}, Month: {date_today.month}, Day: {date_today.day}")
print(f"Hour: {time_now.hour}, Minute: {time_now.minute}, Second: {time_now.second}, Microsecond: {time_now.microsecond}")

formatted_date = date_now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date and time:", formatted_date)






