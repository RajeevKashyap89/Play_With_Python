'''Create a dictionary to store the names and ages of five people. Write a function to return the name of the oldest person.'''

name_age = {"sam":22,"paul":24, "raj": 30, "peter": 40, "swamy": 38}


def oldestPerson(name_age_dict):

    max_age = -1
    oldest_person = ""
    for name,age in name_age_dict.items():
        if  age > max_age:
            max_age = age
            oldest_person = name

    return oldest_person



print(oldestPerson(name_age))


print("************************************\n")

'''Write a function to merge two dictionaries into one'''

d1 = {'Alice': 30,
    'Bob': 25,
    'Charlie': 35,
    'David': 20,
    'Eve': 28}

d2 = {'swamy': 32,
    'karthik': 24,
    'pragg': 36,
    'Kevin': 23,
    'Kohl': 30}


def merge_dict(d1,d2):
    mergedDict = d1.copy()
    mergedDict.update(d2)
    return mergedDict


print(merge_dict(d1,d2))


print("************************************\n")



'''Create a dictionary from two lists: one of keys and one of values.'''

lst1 = ["walmart","target","Macy's","JCPenny","Nike","NewBalance","BananaRepublic"]

lst2 = [10, 20, 40, 15, 8, 6, 3, 9]

def create_dict_from_lst(keys, values):
    pairs = zip(keys,values)
    stores_distance = dict(pairs)
    return stores_distance


print(create_dict_from_lst(lst1, lst2))



print("************************************\n")


'''Write a fun to find the sum and avg of all values in a dictionary.'''

def sum_and_avg(name_age_dict):
    sum = 0
    avg = 0

    for age in name_age_dict.values():
        sum += age

    avg = sum /len(name_age_dict)

    return (sum,avg)    


print(sum_and_avg(name_age))


print("************************************\n")


'''Write a function to get the key of the smallest value in a dictionary.'''


def smallest_key_value(name_age_dict):

    youngest = 100
    youngest_name = ""
    for name,age in name_age_dict.items():
        if age < youngest:
            youngest = age
            youngest_name = name

    return youngest_name


print(smallest_key_value(name_age))


print("************************************\n")

'''Create a dictionary with keys as numbers from 1 to 5 and values as their squares.'''


def numbers_squares():
    num_sq = {}
    for i in range(1,6):
        num_sq[i] = i**2 
    return num_sq

print(numbers_squares())

print("************************************\n")

'''count the frequency of each word in a given string using a dictionary.'''

s = "woodbridge library is in woodbridge"


def count_frequency(s):
    word_count = {}
    lower_str = s.lower()
    words = lower_str.split(" ")
    #print(words)
    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1    
    return word_count

result = count_frequency(s)
print(result)

print("************************************\n")


'''remove a key from a dictionary'''


def remove_key(dictionary, key):
    if key in dictionary:
        dictionary.pop(key)
    return dictionary


print(remove_key(name_age,'swamy'))


print("************************************\n")


'''sort a dictionary by its keys'''

d = {"a":"aaa", "c":"ccc", "b":"bbb"}

def sort_by_keys(dictionary):
   sorted_keys = sorted(dictionary.keys())
   sorted_dict = {key: dictionary[key] for key in sorted_keys}
   return sorted_dict

print(sort_by_keys(d))    


print("************************************\n")

'''sort a dictionary by its values'''

def sort_by_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item:item[1])
    sorted_dict = {key:val for key,val in sorted_items}
    return sorted_dict


unsorted_dict = {"b" : 2, "c" : 1, "a" : 3}
print(sort_by_values(unsorted_dict))


print("************************************\n")

'''Write a program to create a dictionary from a list of tuples.'''

lst = [("sam",22),("paul",24), ("raj",30)]

def convert_tuple_lst_to_dict(lst):
    name_age_dct = {}
    for name,age in lst:
        name_age_dct[name] = age
    return name_age_dct;    

'''
    def create_dict_from_tuples(tuple_lst):
        return dict(tuple_lst)
'''


print(convert_tuple_lst_to_dict(lst))

print("************************************\n")

'''Create a dictionary with default values for all keys.'''

def dict_with_default_val(keys,default_val):
    return {key:default_val for key in keys}


keys = ["a","b","c","d"]
default_value = 0
result = dict_with_default_val(keys,default_value)
print(result)