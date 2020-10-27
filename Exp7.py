#WAP to create a file & store the following information (taken from the user) 1)name 2) Add 3) Contact Info

f = open("demofile3.txt", "x")
name=input("Enter Name:")

Address=input("Enter Address:")
ContactNo=int(input("Enter Contact Number:"))

f.write("Name:",name)
f.write("Address:",Address)
f.write("ContactInfo:",ContactNo)

f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read()) 

#WAP to create to count the no. of times, the program is accessed 



#WAP to count the no. of occurrences of a word in a text file.



#WAP to create a small s/w for banking which should cover only two options i.e withdrawal & deposits 

