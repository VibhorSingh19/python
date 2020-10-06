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
