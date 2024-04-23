#class is a collection of   objects and it conatain attributes and methods
#syntax of class
#Syntax to define a class

#class ClassName:  
#    <statement-1>  
#        .  
#        .  
#        .  
#    <statement-N>  //

#objects
#Object is simply a collection of data (variables) and methods (functions) that act on those data. 
#Data member: A class variable or instance variable that holds data associated with a class and its objects.

#Method : A special kind of function that is defined in a class definition. 

# Create a class 

# class Employee:

    
#     #  // data members
#     #  // methods

# obj = Employee()   #creates object for class


#class examples
#Create a class named MyClass, with a property named x:
# class MyClass:
#   x = 5
# #Now we can use the class named MyClass to create objects:
# #Create an object named p1, and print the value of x:
# p1 = MyClass()
# print(p1.x) 

# # create class
# class Bike:
#     name = "anu"
#     gear = 0
# # create objects of class
# bike1 = Bike()
# print(bike1.name)
# print(bike1.gear)


# # define a class
# class Employee:
#     # define an attribute
#     employee_id = 0

# # create two objects of the Employee class
# employee1 = Employee()
# employee2 = Employee()

# # access attributes using employee1
# employee1.employeeID = 1001
# print(f"Employee ID: {employee1.employeeID}")

# # access attributes using employee2
# employee2.employeeID = 1002
# print(f"Employee ID: {employee2.employeeID}")


class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
print('Student:', s1.name, s1.age)