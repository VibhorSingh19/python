
#Ques1:WAP to create a file & store the following information (taken from the user) 1)name 2) Add 3) Contact Info
'''
f = open("demofile3.txt", "w")
name=input("Enter Name:")

Address=input("Enter Address:")
ContactNo=int(input("Enter Contact Number:"))

f.write("Name:"+name+"\n")
f.write("Address:"+Address+"\n")
f.write("ContactInfo:"+str(ContactNo)+"\n")

f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read()) 

'''
#Ques2:WAP to create to count the no. of times, the program is accessed 
'''
f=open("file1.txt","r")
a=f.read()
f.close()
f=open("file1.txt","w")
if(len(a)==0):
    f.write("0")
else:
    b=int(a)
    b=b+1
    b=str(b)
    f.write(b)
print(a)    
'''
#Ques3:WAP to count the no. of occurrences of a word in a text file.
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

#WAP to create a small s/w for banking which should cover only two options i.e withdrawal & deposits 

f=open("file1.txt","r")
a=f.read().split()
f.close()
f=open("file1.txt","w")
acc=int(input("Enter your account number.."))
if(acc==int(a[0])):
   print("Your Balance is:",a[1])
   input1=int(input("press 1 to withdeaw press 2 to deposit"))
   if(input1==1):
      amount=int(input("Enter the amount."))
      final=int(a[1])-amount;
      f.write(a[0]+str(final))
   elif(input1==2):
      amount=input("Enter the amount.")
      final=int(a[1])+amount;
      f.write(a[0]+str(final))
      	
print("Your New Balance is:",a[1])







