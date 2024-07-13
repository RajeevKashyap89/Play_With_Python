language = 'Python'
Lst = list(language)


lst = ['p','y','T','H', 'O', 'N']

#Another way of creating a list

lst = [i for i in range(11)]
print(type(lst))
print(lst)




numbers = [i for i in range(11)]
print(numbers)


squares = [i * i for i in range(11)]
print(squares)

numbers = [(i,i*i) for i in range(11)]
print(numbers)


even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)


odd_numbers =[i for i in range(21) if i % 2 != 0]
print(odd_numbers)



#flattening

list_of_lists = [[1,2,3],[4,5,6],[7,8,9,10]]
flattened_list = [num for row in list_of_lists for num in row]
print(flattened_list)



##Lambda function


# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3)) 



add_two_numbers = lambda a,b : a + b
print(add_two_nums(4,4))



print((lambda a,b : (a - b))(8,6))



square = lambda x : x ** 2
print(square(3))


cube = lambda x : x ** 3
print(cube(3))



##Exercises

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = []

for name_lst in names:
        first_name, last_name = name_lst[0]
        full_name = first_name + last_name
        full_names.append(full_name)

print(full_names)
print("**************")

concatenated_List = [' '.join(name[0]) for name in names]

print(concatenated_List)

print("\n")

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

#dict_lst = [for country in countries]


result = []
for country_tuple in countries:
    
    country, city = country_tuple[0]
    dict_lst = {
        'country' : country.upper(),
        'city' : city.upper()
    }
    result.append(dict_lst)

print(result)



dict_Lst  =  [{'country': country.upper(), 'city' : city.upper()} for [(country, city)] in countries]

print(dict_Lst)
    

result = lambda x1,y1,x2,y2 : (y1 - y2)/(x1 - x2)


print(result(1,3,2,8))