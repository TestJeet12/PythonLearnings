print("Hello")
a=5
b,c,d=10,5.6,"Test"

print(d)

print("{} {}".format(c,d))# need format function when concatinating diffent data type values
print(d+" "+d)
#comments in Python
print(type(d))
print(type(c))

#5 main data types in python- numeric, string, list , tuple and dictionary
#int,float, complex comes under numeric parent data type
#List-its a datatype that allows to store multiple values with different data type
print("List")

Values=[2,3,"Test",4.5]
print(Values[0])#to fetch the values as per index
print(Values[-1])#to fetch the value at last
print(Values[1:3])#to fetch the values based on sub index
print(Values[0:-1])
print(Values[2:])
print(Values)
Values.append("Testnew")#to append at the end
Values.insert(2,"new")# to insert after a particular index
print(Values)
Values[3]=9.009#updating
print(Values)
del Values[0]#deleting
print(Values)

#Tuple- same as List data type just use parenthesis in place of square bracket and Tuple is immutable means
#cannot update
print("Tuple")

Val=(2,3,"Test",2.2)
print(Val)
#Val[2]=3.4#This will give error
print(Val)
print(Val[1])

#Dictionary- works in Key:Value pair-
print("Dictionary")

Dic = {"Name": "JeetC", 2:3, 4:"","age":28}
print(Dic)
print(Dic["Name"])
Dic["New"]="insert"#inseting in Dictionary
print(Dic)

