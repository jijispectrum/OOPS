#__init__ function
#In the __init__ method, self refers to the newly created object; in other class #methods, it refers to the instance whose method was called.


# Create class Employee

# Create class Employee

class Employee:
   'Common base class for all employees'
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   def displayCount(self):
      print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
         print ("Name : ", self.name,)  
         print ("Salary: ", self.salary)

emp1 = Employee("Zara", 2000)            
emp1.displayEmployee()                      


# emp2.displayEmployee()
# print ("Total Employee %d" % Employee.empCount)

 
# Create a class named Person, use the __init__() function to assign 
#values for name and age:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age) 
