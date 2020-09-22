#first
'''
file = open('file.txt', 'w') 
L = ["Name:Vibhor \n", "Age:20\n", "Class:12 \n", "Month:4 \n", "Year:2020 \n"] 
file.writelines(L) 
file.close() 
print("Added successfully!") 
'''
#secound
'''
file1 = open('file.txt', 'r') 
print(file1.read()) 
file1.close() 
'''
#third 
'''
file2 = open('file1.txt', 'a') 
s = "a"
file2.write(s)
file2.close() 
file1 = open('file1.txt', 'r') 
print(len(file1.read())) 
file1.close() 
'''
#third
'''
f=open("file1.txt","r")
a=f.read()
print(a)
f.close()
f=open("file1.txt","w")
if(len(a)==0):
    f.write("0")
else:
    b=int(a)
    b=b+1
    b=str(b)
    f.write(b)
'''
#4
'''
from collections import Counter
def func(name):
	with opn(name) as f:
		rturn Counter(f.read().split())
print(fun("filec.txt"))
Counter({"September":1,"hello":1,"world":1})
'''
#4
'''
c=0
input1=input("enter the word to be searched in a file:")
f=open("filec.txt","r")
words=f.read().split()
for i in words:
    if (input1==i) :
        c=c+1

#max_len=len(max(words,key=len))
print(c)
f.close()
'''
f=open("filec.txt","r")
r=f.read()
f.close()
f=open("file5.txt","w")
f.write(r)
f.close()