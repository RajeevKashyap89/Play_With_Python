from datetime import datetime,date

#print(datetime.now())

now = datetime.now()
day = now.day
year =  now.year
month = now.month
hours = now.hour
mins = now.minute

print(f"{month}-{day}-{year} {hours}:{mins}")

timestamp = now.timestamp()

print('timestamp:', timestamp)


d = date(2024, 5, 26)
print(d)