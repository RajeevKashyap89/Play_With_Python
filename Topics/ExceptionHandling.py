try:
    print(10 + '5')
except:
    print("something went wrong, Please check the logs")
finally:
    print("I always print")



try:
    print(10 + '5')
except Exception as e:
    
    print(f"something went wrong, Please check the logs, {e}")
finally:
    print("I always print")   


print("\n")


## Unpacking

def sum_of_five(a,b,c,d,e):
    return a+b+c+d+e

lst = [1,2,3,4,5]
print(sum_of_five(*lst))



args = [2, 7]
numbers = range(*args)
print(list(numbers))



def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'raj', 'country':'US', 'city':'Woodbridge', 'age':22}
print(unpacking_person_info(**dct))   


## Enumerate
for index, item in enumerate([20,30,40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway']
for index, i in enumerate(countries):
    print("hi")
    if i == "Finland":
        print(f"the country {i} has been found at index {index}")

print("\n")

 ## Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

fruits_Vegetables = zip(fruits, vegetables)
print(list(fruits_Vegetables))
print("\n")
fruits_and_vegetables = []
for f,v in zip(fruits,vegetables):
    fruits_and_vegetables.append({'fruit':f, 'Vegetable':v})

print(fruits_and_vegetables)    


names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

#one, two, three, four, five, *rest = names

nordic_countries ,es, ru = names[:5], names[5], names[6]

#nordic_countries = [one, two, three, four, five]

#es = rest[0]
#ru = rest[1]

print(nordic_countries, es, ru)