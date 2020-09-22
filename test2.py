'''
# First question
str=input("Enter a string..")
l=len(str)
str2=""
for i in range(l, -1, -1) : 
	str2= str[::-1]
print(str2)
if(str2==str):
	print("It is a palindrome number..")
else:
	print("It is not a palindrome number..")

# Second
num1=int(input("Enter first number.."))
num2=int(input("Enter secound number.."))
for i in range(num1,num2+1):
	c=0
	for j in range(1,i+1):
		if(i%j==0):
			c+=1
	if(c==2):
		print(i)		
#Third
num1=int(input("Enter first number.."))
num2=int(input("Enter secound number.."))
print(1,end=" ")
for i in range(num1,num2):
    a=i+(i+1)
    if(a<=num2):
    	print(a,end=" ")	
    


#Forth
key = int(input("Enter a key:"))
val = int(input("Enter a value:"))
class_list = {}

c=0
for j in range(1,key+1):
	
	if(key%j==0):
		c+=1
if(c==2):
	if(val%2!=0):
		class_list[key] = val
		print("Successfully Added")
print(class_list)

