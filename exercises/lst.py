
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


'''Write a function to remove duplicates from a list.'''

lst = [1,1,2,3,4,5]

def remove_duplicates(lst):
     return list(set(lst))

print(remove_duplicates(lst))



'''Create a list of the first 10 even numbers.'''

def print_10_even_nos():
     for i in range(11):
            print(i * 2)

print_10_even_nos()     


'''
    even_numbers = [2 * i for i in range(1,11)]

'''