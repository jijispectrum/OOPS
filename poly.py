#polymorphism
#Polymorphism is based on the greek words Poly (many) and morphism (forms).
#Wewill create a structure that can take or use many forms of objects. 
#Polymorphism can be referred as the process of taking many 
#forms by a same object.
#Method Overloading:

#Two or more methods have the same name but different numbers of parameters or
# different types of parameters, or both.
#These methods are called overloaded methods and this is called method overloading. 
#ython does not support method overloading by default
class Human:
 
    def sayHello(self, name=None):
 
        if name is not None:
            print ('Hello ' + name)
        else:
            print ('Hello ')
 
# Create instance
obj = Human()
 
# Call the method
obj.sayHello()
 
# Call the method with a parameter
obj.sayHello('Guido')