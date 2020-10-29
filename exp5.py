#wap to accept no. from user and populate a list and find the duplicate entries in the list.
'''
lst = []
duplicates = {}

print("Enter any 5 numbers: ", end="")

for i in range(0, 5):
     num = int(input())
     lst.append(int(num))

for i in lst:
     if i in duplicates:
         duplicates[i] += 1
     else:
         duplicates[i] = 1

print("Duplicate found in the list are: ", end="")

for i in duplicates:
     if duplicates[i] > 1:
         print(i, " ", end="")
'''
#wap to insert a string from a user and replace the 4th char of a string with h.
'''
a = input("Enter a string: ")

string = a[:3] + 'h' + a[5:]

print(string)
'''
#wap to accept 2 str from a user and check whether 2nd is a part of 1st or not.
'''
str1 = input("Enter a string: ")
str2 = input("Enter secound string: ")

if str2 in str1:
    print(str2, "is a substring of ", str1)
else:
    print(str2, "is not a substring of ", str1)
'''
#wap to accept a str from a user and display the reverse of it without using any inbuilt function.
'''
str1 = input("Enter a string: ")

size = len(str1)

for i in range(size-1, -1, -1):
    print(str1[i], end="")
set1 = {"a", "b", "c"}
print("original set: ", set1)

newvalue = input("Enter a value: ")
set1.update([newvalue])
print("Updated set: ", set1) 

dict={}
n=int(input("the number of keys to be inserted:"))
i=0
while i<n:
    
    key=input("enter the key{}:".format(i))
    if key.isnumeric():
        print("key cannot be numeric")
        i=i-1
    else :
        if len(key)>6:
            print("length of key cannot be more than six")
            i=i-1
        else:
            val=int(input("enter value:"))
            if(val%2!=0):
                print("value should be an even number")
                i=i-1
            else:
                dict[key]=val
    i=i+1
print(dict)

dict={'subject':{}}

name=input("enter name:")
roll=input("enter roll no.:")
subject1=input("enter subject 1:")
subject2=input("enter subject 2:")
subject3=input("enter subject 3:")
dict["name"]=name
dict["roll no."]=roll
dict["subject"]["subject1"]=subject1
dict["subject"]["subject2"]=subject2
dict["subject"]["subject3"]=subject3
print(dict)
'''
list=[123,122,128,130,158]
list2=[]
sum=0
for i in list:
    list2.insert(0,i)
    sum=sum+i
print(list2)
print("sum={}".format(sum))
