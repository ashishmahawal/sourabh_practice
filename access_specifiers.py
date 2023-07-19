# access specifires
# class Employee:
#     pass
# a = Employee()
# a.emp = 5 


# public access specifire in python
# class Employee:
#     # constructor
#     def __init__(self):
#         self.name = "sourabh malik"  # public variable

# a = Employee()
# print(a.name) # we can access easily from outside a.name because this is a public access specifier 

# private access modifier
# these are not access out side from the class (these are prifixing by the double underscore(__). 
# this is known as a "weak internal use indicator")
# class Employee:
#     def __init__(self):
#         self.__name = "sourabh malik"

# a = Employee()
# #print(a.__name) # we cannot access the private access modifier
# # we can access the private access modifier(varible name._classname__variable)
# print(a._Employee__name)# we can access the private access modifier by this way this is called name mangling
# print(a.__dir__())


#protected Access modifier
# these protected mdifier are only access by class itself and its subclasses
# protected modifier are  indicating by prifixing the single underscore(_) 
class student:
    def __init__(self):
        self._name = "sourabh malik"
    def _funname(self):  # protected method
        return "code with sourabh malik"
class subject(student):   # inherited class
    pass
a1 = student()
a2 = subject()
# calling by a1 of student class
print(a1._name)
print(a1._funname())
# callinmg by a2 of subject class 
print(a2._name)
print(a2._funname())
print(dir(a1))