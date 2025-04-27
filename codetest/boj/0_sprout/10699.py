from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
if month <= 10:
    month = "0" + str(month)
if day <= 10:
    day = "0" + str(day)
print(f"{year}-{month}-{day}")