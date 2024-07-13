
#My first python program !!

print('hello!!!')

is_this_going_to_do_good=True
name = "Rajeev"
anotherString = r"""    
                    ABC
                    @Rajeev
                """
anotherStringOp =   (    
                    "ABC"
                    r"\nRajeev"
)

anotherStringPrinting10 = "R"*10

if is_this_going_to_do_good:
    print('Great!! have fun '+ name)
    print(anotherString)
    print(anotherStringOp)
    print(anotherStringPrinting10)
    print(name[0])
    print(name[-1])
    print(name[0:3])
    print(name[:2])
    print(name[-2:])
    #print(name[-200])
    print(name[:] + ' : creating a shallow copy of name')

    #python strings are immutable

    #name[0] = 'K'

s = 'supercalifragilisticexpialidocious'
print(len(s))
print(str(len(name[0:2])) + ' '+ name[0 :2])
print(str(len(name)) + ' '+ name)


#notice that its creating new copy of the list
my_fav_number = [10,20,30,40]
print(my_fav_number)
print(my_fav_number + my_fav_number)
print(my_fav_number + [50])

#append method
my_fav_number.append(60)

my_num_string = str(my_fav_number)
print(my_num_string + "Hey!")

#nesting two different lists
a = [1,2,3]
b = ['a','b','c']
x = [a,b]
print(x)
print(x[1][0])


name, age = 'Raj',25
print (name)
print(age)


print('alice ' * 5)



