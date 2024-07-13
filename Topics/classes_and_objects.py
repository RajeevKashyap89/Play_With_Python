class Person:
    def __init__(self,firstName='R', lastName='A', age=25, country='US', skills = None): 
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.country = country
        self.skills = []
    def person_info(self):
        return f"{self.firstName} {self.lastName} is {self.age} lives in {self.country}" + (f" and has {self.skills} skills" if self.skills else "")    
    def add_skills(self, skill):
        self.skills.append(skill)



p = Person()
print(p.person_info())  
p.add_skills("HTML")
p.add_skills("CSS")     
print(p.person_info())

## person class is base class and student class is 
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland','test1')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland','test')
s1.add_skills("Python")
print(s1.person_info())
s2.add_skills("Java")
print(s2.person_info())

print(issubclass(Student,Person))
print(isinstance(s1,Person))
print(s1.firstName)

#####################################################
## Scopes and Namespaces ##
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def again_local():
        spam = "local_spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    again_local()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


#################################################

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter    



####################################################

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# Create an instance of Mapping
m = Mapping([1, 2, 3])
print(m.items_list)  # Output: [1, 2, 3]

# Create an instance of MappingSubclass
ms = MappingSubclass([4, 5, 6])
print(ms.items_list)  # Output: [4, 5, 6]

# Use the overridden update method
ms.update(['a', 'b'], [7, 8])
print(ms.items_list)  # Output: [4, 5, 6, ('a', 7), ('b', 8)]
