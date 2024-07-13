'''
 accepts the user's first and last name and prints them in reverse order with a space between them.
'''


first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')

fullname = first_name +' '+ last_name


def reverse(name):
    for char in range(len(name)-1,-1,-1):
        yield name[char]


print(fullname)

print(last_name + " " + first_name)


reversedName = ''
for letter in reverse(fullname):
    reversedName += letter

print(reversedName)    




