
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False        


def calculate_days(year, month):
    
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    is_Leap_year = is_leap(year)
    
    days = month_days[month-1]
    if is_Leap_year and month == 2:
        return days+1
    else:
        return days 




print("Hi!, please let me know for which year and moth you need to know the number of days")

year = int(input("Year: "))

while year <=0 or year >= 9999:
    print("Enter a Valid year")
    year = int(input("Year: "))

month = int(input("Month: "))

while month <= 0 or  month >= 12:
    print("Enter a valid month")  
    month = int(input("Month: "))  

days = calculate_days(year, month)

print(f"Month {month} in the year {year} has {days} days")

