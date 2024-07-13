
"""This is Docstring and something similar 
to javadocs"""
def hello_world(name):
    print('Hello ' + name)

hello_world('Raj')
#hello_world(10)

"""another way of calling function"""
f = hello_world
f('Raj')

"""or"""
f = hello_world('Raj_thrird_time')
f


"""fib series"""

def fib(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b ,a+b
    return result

fun = fib(10)    
print(fun)


"""default value"""
'''
    l=[]
    l.append(1)
    l.append(2)
'''
def fun(a, l=[]):
    l.append(a)
    return l

print(fun(6))
print(fun(7))
print(fun(8 , []))
print(fun(9))
print(fun(10))


"""non default"""

def fun(a, l=None):
    if l is None:
        l=[]
    l.append(a)
    return l

print(fun(6))
print(fun(7))
print(fun(8 , []))
print(fun(9))
print(fun(10))

#####################################
print("\n")

def fib(n):
    
    result = []
    a,b = 0,1

    while a < n:
        result.append(a)
        a,b = b,a+b

    return result    

print(fib(5))