File = open('Test.txt')# to open the file in python and store in a object
#print(File.read())#reads all the lines in file#commenting  otherwise it will read from where last left reading
print("***************")
#print(File.read(7))#Reads n number of characters, next line is also treated as characters#commenting  otherwise it will read from where last left reading
print("***************")
#File.readline()#Reads line by line
#Test=File.readlines()#reads all the lines and stores in a List
#print(Test)
#File.close()#to close file in Python

# print line by line using readlines

#Line=File.readline()
#while Line!="":
    #print(Line)
    #Line=File.readline()

#now same program as above using readlines
Line=File.readlines()
for J in Line:
    print(J)

File.close()
