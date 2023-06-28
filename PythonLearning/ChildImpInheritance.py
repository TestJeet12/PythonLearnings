#Inheritance- is inheriting properties of parent class into child class.
#with inheritance we can call the methods and variables of parent class into child class without
#creating an object.
from OOPsConcept import Calculator


class ChildImp(Calculator):
    num2=200
    def __init__(self):#As per OOPs principle if there is any contructor in parent class then we have
        #to call that constructor mandatorily from child class constructor.
        Calculator.__init__(self,10,2)
    def newSummation(self):
        return self.firstnumber+self.secondnumber+ChildImp.num2+Calculator.Summation(self)
newobj1=ChildImp()
print(newobj1.newSummation())

print("************************************")
#String functions-
str1="JeetChakraborty.new"
str2="Jeet"
str3=" Test "

print(str1[2])#string extract from index, same as list
print(str1[0:4])#string extract from range of index, same as List, if u want substring in Python
print(str2 in str1)#string check
print(str1+" "+str2)#concatination of 2 strings
print(str1.split("."))#string split, return type is List
print(str3.strip())#string strip(trimming spaces from both end)
print(str3.lstrip())#string strip from left
print(str3.rstrip())#string strip from right