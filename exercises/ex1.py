'''
 Accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
'''


user_input = input('enter numbers comma separated :')

lst = user_input.split(",")

print(lst)

tpl = tuple(lst)

print(tpl)



##############################

numLst = [int(i) for i in lst]
print(numLst)
print(tuple(numLst))



print('Twinkle, twinkle, little star,\n'
      '\t How I wonder what you are!')