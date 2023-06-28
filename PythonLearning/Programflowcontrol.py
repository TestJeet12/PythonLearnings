#if else statement in python-
print("****if else in python****")
Greeting="Good Morning"
if Greeting=="Morning":#indentation is imp in python, also colon is required which acts as opening bracket
    print("Condition is pass")
else:
    print("condition is fail")
print("end of if else statement")

#for loop in python-
print("****for loop in python****")
obj=[1,2,3,4,5,6]
for i in obj:# i is the variable that will iterate in obj list
    print(i)
print("*********************")

Summation=0
for j in range(1,10):# range(i,j)->i to j-1
    Summation=Summation+j
print(Summation)
print("***********************")
for k in range(10):#statring value will be 0
    print(k)
print("*************************")
for l in range(1,5,2):#increment by 2
    print(l)
print("*************************")
for m in range(10,1,-1):#decrement by 1
    print(m)

print("*****************************")

#while loop in python-for loop we use when we have fixed number of iterations but while loop we use when we dont know the number of iterations
print("****while loop in python****")
it=10
while it>1:
    if it==9:
        it=it-1
        continue# continue is used to skip the iteration

    if it==3:
        break# break is used to stop the loop abruptly

    print(it)
    it = it - 1
print("while loop execution is done")

print("*****************************")

#Functions in python-
#function is a group of relative statements that perform a specific task
print("****functions in python****")
def greetings(a,b):#Function declaration
    print(a+b)
greetings(1,2)#Function call