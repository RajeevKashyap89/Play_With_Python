users = {'a':'active','b':'inactive', 'c':'inactive','x':'active'}
for user in users:
    print(user)

print(users.values())   

###################

for key, value in users.items():
    print('key :' + key + ', Value :' + value)


#####################
print()
for key, value in users.items():
    if value == 'inactive':
        print('key :' + key + ', Value :' + value)

#######################
print()

active_users = {}
for user, status in users.items():
    if status == 'active':
     active_users[user] = status
for key, value in active_users.items():     
    print('key :' + key + ', Value :' + value) 

print()

############################


a = ['1','2','3','4','5']
for i in range(len(a)):
    print(i, a[i])

print()
###########################
for i in a:
    print(i, end = ', ')
print()    


###########################

print(sum(range(10000)))

print(len(range(10000)))

print()
##########################

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            if n % 2 == 0:
                print(n, 'is even number')

            print(n, 'equals',x,'*', n//x)
            break
    else:
        print(n, 'is a prime number')     