#there are 3 ways to get the exceptions-
#assert and raise keywords are used to fail the test when condition is not met , sometimes when
#we feel condition might fail then we use assert and raise keywords in Python
#try and except block we use when we dont want to fail the test but get the exception, so for the piece
#of code we think will fail we will put in try block and if the condition really fails the control will go to the except
#block

ItemsinCart=0
#imagine some automation code is to capture products in the above variable but we dont know if it passed or not
if ItemsinCart!=2:
    raise Exception("test failed")

assert(ItemsinCart==2)
assert(ItemsinCart==0)#assert expects the argument/condition passed to be true if not then test will fail with assertion error


try:
    with open('new.txt','r') as reader:
        reader.read()
except:
    print("Galat file knola bhai")

try:
    with open('Test.txt','r') as reader1:
        reader1.read()
except:
    print("wrong file")
try:
    with open('new.txt','r') as reader2:
        reader2.read()
except:
    print("Firse galat file knola bhai")
try:
    with open('test1.txt','r') as reader3:
        reader3.read()
except Exception as e:# here what exception python is throwing will be catched in variable e
    print(e)

finally:# this block will execute no matter if there is any error or not
    print("cleaning resources")
