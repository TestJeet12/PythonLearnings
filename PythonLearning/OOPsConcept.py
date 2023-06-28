#class is nothing but user defined blueprint or prototype
#for example if we create a class called calculator we need to define what operations it will perform
#like sum, multiplication etc
#Class have these things- Methods(functions inside the class called as methods),
#class variables, instance variables, contructors etc
class Calculator:#class names should be capital
    num=100#class variable, class variables are always constant , instance variable changes
    def __init__(self,a,b):#this is constructor , when class object is created , constructor will be
        #called , name should be always__init__, self will be there as argument by default
        #self keyword is used for object reference, when objectis created constructor - self will store
        #the details of the arguments passed
        self.firstnumber=a#instance variables
        self.secondnumber=b
    def newmethod(self):
        print("this is new method")
    def Summation(self):
        return self.firstnumber+self.secondnumber + Calculator.num +self.num
    # in Python we need to use self. for calling instance variables and self. or classname. for
    #class variables


obj = Calculator(10,2)#syntax for object creation, object is required to call methods or functions outside the class
obj.newmethod()
print(obj.num)
print(obj.Summation())
print("************************************")
obj1=Calculator(10,10)
obj1.newmethod()
print(obj1.num)
print(obj1.Summation())

