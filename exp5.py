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

str1 = input("Enter a string: ")

size = len(str1)

for i in range(size-1, -1, -1):
    print(str1[i], end="")
 