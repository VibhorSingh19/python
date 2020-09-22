'''number=int(input("Enter a number:"))
num_sqt=number**0.5
print("Square Root of %0.2f is %0.2f"%(number,num_sqt))


a = int(input('Enter First Side of Triangle: '))
b = int(input('Enter Second Side of Triangle: '))
c = int(input('Enter Third Side of Triangle: '))

s = (a + b + c ) / 2
areaTri = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The Area of the Triangle is %0.3f " %areaTri)

import cmath

a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

x = (b**2)-(4*a*c)
 
s1 = (-b-cmath.sqrt(x)) / (2*a)
s2 = (-b+cmath.sqrt(x)) / (2*a)

print('\nThe solution of given Equation is {0} and {1}'.format(s1,s2))

import random
print(random.randint(0,10))

first = int(input('Enter First Number: '))
sec = int(input('Enter Second Number: '))

sum = first + sec

print("The Sum of ",first," and ",sec," is: ",sum)

num=int(input("Enter a Number:"))
a=num
sum=0
while(a>0):
    d=a%10
    sum=sum+(d**3)
    a=a//10

if(sum==num):
    print("It is an Armstrong Number")
else:
    print("Not an Armstrong Number")

num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))

if(num1%2==0):
     print('It is an Even Number')
else: 
   print('It is Odd Number')
    
if(num2%2==0):
 	print('It is an Even Number')
else:
    print('It is Odd Number')
...
num= int(input("Enter the Number: "))
if num < 0: 
    print("The Entered number is Negative.")
elif num > 0:
    print("The Entered number is Positive.")
elif num == 0:
    print("Number is Zero.")
else:
    print("The input is not Valid!!")
'''
'''
ch = input("Enter a Character : ")
li=['a','e','i','o','u','A','E','I','O','U']
if(ch in li):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")


import random
num1=random.randint(0,9)
num2=random.randint(0,9)
num3=random.randint(0,9)
print (num1,num2,num3)
if num1==num2==num3:
    print("First Prize")
elif num1==num2 or num2==num3 or num1==num3:
    print("Second Prize")
else:
    print("Try Again")



a=3
b=2
try:
	c=a/b
	print(c)
	num=int(input("Enter a nuumber"))
except ZeroDivisionError as e:
	print("Zero division errorr...!")
except ValueError as e:
	print("Invalid number...!")
finally:
  print("Bye")

import sys
li=[4,7,2,5,9]
li.sort()
print(len(li))

for x in sys.argv:
	print(x)

num1=int(input("Enter first number.."))
num2=int(input("Enter secound number.."))
print(1,end=" ")
for i in range(num1,num2):
    a=i+(i+1)
    if(a<=num2):
    	print(a,end=" ")	'''
try:
	c=a/b
	print(c)
	num=int(input("Enter a nuumber"))
except ZeroDivisionError as e:
	print("Zero division errorr...!")
except ValueError as e:
	print("Invalid number...!")
finally:
  print("Bye") 	