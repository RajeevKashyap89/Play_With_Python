
'''	
    1	Write a program to find the second largest number in a list.
	2	Write a function to remove duplicates from a list.
	3	Create a list of the first 10 even numbers.
	4	Write a program to find the intersection of two lists.
	5	Write a function to find the longest word in a list of words.
	6	Write a program to count the number of times a specified element appears in a list.
	7	Create a list of tuples where each tuple contains a number and its square.
	8	Write a program to reverse a list without using the built-in reverse function.
	9	Write a function to check if a list is a palindrome.
	10	Create a list of numbers and write a program to shift the elements one position to the left.
	11	Write a function to find the common elements in three lists.
	12	Create a list of strings and write a program to sort it by the length of the strings.
	13	Write a function to rotate a list by n positions.
	14	Write a program to find the maximum product of two integers in a list.
	15	Create a list of random numbers and write a program to find the average of the numbers.
'''






'''Write a program to find the second largest number in a list.'''

lst = [2,5,23,45,343,435,22,454,357,77,43]

def second_largest(lst):
    second_largest = -1
    largest = lst[0]
    for num in lst:
            if num > largest:
                second_largest = largest
                largest = num
            elif num <= largest & num > second_largest:
                second_largest = num    
    return (largest,second_largest)

print(second_largest(lst))            


print("****************************************\n")

'''Write a function to remove duplicates from a list.'''

lst = [1,1,2,3,4,5]

def remove_duplicates(lst):
     return list(set(lst))

print(remove_duplicates(lst))

print("****************************************\n")

'''Create a list of the first 10 even numbers.'''

def print_10_even_nos():
     for i in range(11):
            print(i * 2)

print_10_even_nos()     


'''
    even_numbers = [2 * i for i in range(1,11)]

'''

print("****************************************\n")

'''Find the intersection of two lists.'''

lst1 = [1,2,3,4,5,6]
lst2 = [4,5,6,7,8,9]

def find_intersection(list1, list2):   
    return list(set(lst1) & set(lst2))

print(find_intersection(lst1, lst2))


'''
    return [x for x in lst1 if x in lst2]

'''

print("****************************************\n")

'''function to find the longest word in a list of words'''

lst = ["Using", "Set", "Intersection", "with", "List", "Comprehension"]

def  longest_word(lst):
     longestWord = lst[0]
     for word in lst:
          len(word) > len(longestWord)
          longestWord = word
     return longestWord

print(longest_word(lst))     


'''   
    return max(lst, key=len)

'''


print("****************************************\n")


'''Function to count the number of times a specified element appears in a list.'''

lst = [1,2,2,3,4,5,6]


def count_freq(lst, n):
     count = 0
     for num in lst:
          if num == n:
               count +=1
     return count

print(count_freq(lst,2))       

'''
*** Other Options ***

  return sum([1 for x in lst if x == n])

  return lst.count(n)

'''


print("****************************************\n")


'''Create a list of tuples where each tuple contains a number and its square.'''

def number_square():
     result = []
     for x in range(1,11):
        result.append((x,x**2))
     return result   
     
print(number_square())     


'''
 
return [(x,x**2) for x in range(1,11)]

'''

print("****************************************\n")


'''Function to reverse a list without using the built-in reverse function.'''

lst = [1,2,3,4,5]

def reverse_lst(lst):
     return [lst[x] for x in range(len(lst)-1,-1,-1)]

print(reverse_lst(lst))     


'''
reversedLst = []
     for x in range(len(lst)-1,-1,-1):
          reversedLst.append(lst[x])
     return reversedLst
'''


print("****************************************\n")

'''function to find the common elements in three lists.'''


lst1 = [1,2,3,4,5,6]
lst2 = [3,4,5,6,7,8]
lst3 = [5,6,7,8,9]

def find_common(lst1,lst2,lst3):
   common_elements =  set(lst1) & set(lst2) & set(lst3)
   return list(common_elements)
    
print(find_common(lst1,lst2,lst3))   


print("****************************************\n")

'''Function to find the maximum product of two integers in a list.'''

lst = [1,2,3,4,5,6]

def max_product(lst):
    
    if len(lst) < 2:
         return None
    
    sortedLst =  sorted(lst,reverse=True)
    
    return sortedLst[0]*sortedLst[1]

print(max_product(lst))