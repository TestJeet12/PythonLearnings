#another way of opening file in Python-with this way no need to specifically write close line to close file in Python
with open('Test.txt','r') as reader:#reader is the object , any name can be given, r parameter inside open
    #tells to open the file in read mode and w for write mode, if we dont pass the second parameter inside open
#then by default it will be in read mode
    #now we will write a program to reverse and write the contents of Test.txt file
    Contents=reader.readlines()
    reversed(Contents)# to reverse the list- Contents
    with open('Test.txt','w') as writer:
        for j in reversed(Contents):
            writer.write(j)
