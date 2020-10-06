#first
print("Enter 5 numbers...")
import array 
   
arr = array.array('i', [])  
  
for i in range(0,5):
	num1=int(input())
	arr.append(num1)
print(arr)

#secound
num2=int(input("Enter a index val."))
arr.pop(num2)
print(arr)

#third
num3=int(input("Enter a number to be searched.."))
for i in arr:
	if(i==num3):
		if(num3%2==0):
			print("Number is present,It is Even")
		else:
		    print("Number is present,It is Odd")	
	
#fourth
print("Reversed array.....")
arr.reverse()
print(arr)
#fifth
a=array.array('i',[0,9,8,5,3,2,0])
print(a)
c=0
b=int(input("enter value for the frequency..:"))
for i in a:
    if i==b:
        c=c+1
print(c)

#six
n=int(input("enter value to be removed:"))
if n in a:
    a.remove(n)
print(a)