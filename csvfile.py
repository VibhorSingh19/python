
# writing to CSV 
import csv 	
# field names 
fields = ['RollNo.', 'Name', 'Subject'] 	
# data rows of csv file 
print("Enter rollno. name and subject..")
rollno=input("Enter roll no.:")
name=input("Enter name:")
subject=input("Enter subject:")

rows = [ [rollno,name,subject]  
       ]

# name of csv file 
filename = "evaluation.csv"
	
# writing to csv file 
with open(filename, 'w') as csvfile: 
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile) 
		
	# writing the fields 
	csvwriter.writerow(fields) 
		
	# writing the data rows 
	csvwriter.writerows(rows) 
with open('evaluation.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)