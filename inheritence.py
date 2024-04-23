#It refers to defining a new class with little or no modification to
# an existing class. The new class is called derived (or child) class 
#and the one from which it inherits is called the base
# (or parent) class. Syntax is :
#single inheritence
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()
#multiple
# class Base1:
#     pass

# class Base2:
#     pass

# class MultiDerived(Base1, Base2):
# create child class
class Student(Person):
  pass 
x = Student("Mike", "Olsen")
x.printname() 

#Use the super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
#multilevel
# Multilevel inheritance : -  You can inherit a derived class from 
#another derived class. This is known as multilevel inheritance. 
# In Python, multilevel inheritance can be done at any depth.

