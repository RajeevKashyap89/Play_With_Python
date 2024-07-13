import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Password Generator!!')
nr_letters = (input("How many letters would you like in your password?\n"))
nr_symbols = (input(f"How many symbols would you like?\n"))
nr_numbers = (input(f'how many numbers would you like\n'))


if not nr_letters.isdigit() or not nr_numbers.isdigit() or not nr_symbols.isdigit():
    print('Invalid input, Please try again!')
else:
    password = []

    for i in range(0, int(nr_letters)):
        random_letter = random.randint(0,51)
        password.append(letters[random_letter])

    for i in range(0, int(nr_numbers)):
        random_number = random.randint(0,9)
        password.append(numbers[random_number])   


    for i in range(0, int(nr_numbers)):
        random_symbol = random.randint(0,8)
        password.append(symbols[random_symbol])


    random.shuffle(password)      
    print(f"Here is your password: {''.join(password)}")

    

    if len(password) <= 6:
     print("your password is weak, try to include at-least 8 char's for a stronger password.")
    elif len(password) == 7:
        print('Your password is Medium, try to include at least 8 characters for a strong password.')
    else:
        print('your password is Strong.!!')    
