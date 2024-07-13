names = ['a','b','c']

for name in names:
    print(name, end = ', ')
print('')


str = 'foobar'

for i in str:
    print(i,end=' ')
print()    


####################

for i in range(10):
 print(i)

print()

#####################

for i in range(10, 55 , 4):
   print(i)


###########################


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


for k,v in users.items():
   print(f"Key:{k}, Value:{v}")


for user,status in users.copy().items():
   if status == 'inactive':
      del users[user]
print(users)


active_users = {}
for user, status in users.items():
   if status == 'active':
      active_users[user] = status

print(active_users)


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


###################################
print("\n")
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

print(basket) #source is unaltered

#######################################
print("\n")
result = 'Hello' or '' or 'man'
print(result)

result = 'Hello' or '' or 'man'
if(result):
    print(result)


