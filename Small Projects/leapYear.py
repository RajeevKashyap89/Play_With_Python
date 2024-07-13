year = input('which year do you want to check?')

if year.isdigit() and len(year) != 4:

  print('Invalid Input!')

else:
  year = int(year)

  if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("It's a leap year")
        else:    
            print('Not Leap Year') 
    else:
      print("It's a leap year")
  else:
    print('Not a leap year, Check for some other year')     