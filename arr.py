from tkinter import *

tk = Tk()
tk.title("Banking")
account_no = IntVar()
user_name = StringVar()
choice = IntVar()

def transaction():
    choice = choice.get()
    print(choice)

def transactionMenu():
    
    acc_no = account_no.get()
    name = user_name.get()
    path = 'E:/CP/' + str(acc_no) + '.txt'
    try:
        f = open(path)
    except IOError:
        Label(tk, text="ERROR! ACCOUNT NOT REGISTERED....", width=50, anchor="w").grid(row=4, column=5)
    finally:
        f.close()


      Label(tk, text="Enter choice: ", width=25, anchor="w").grid(row=6, column=1)

    button_transact = Button(tk, text="submit", command=transaction)
    button_transact.pack()
    #cmd input as gui not working
    path = 'E:/CP/' + str(path) + '.txt'
    choice = int(input("Input choice: "))
    if choice == 1:
        with open(path, "r+") as file1:

            file1.seek(0)
            balance = file1.read()
            if len(balance) == 0:
                file1.write(str(1000))

            amount = int(input("Enter amount to withdraw: "))
            
            file1.seek(0)
            balance = file1.read()
            print("Opening balance: ", balance)
        
            file1.seek(0)
            if eval(balance) < amount:
                print("Insufficient Balance: ", balance)
            else:
                balance = eval(balance) - amount
                file1.write(str(balance))

                file1.seek(0)
                balance = file1.read()
                print("Closing balance: ", balance)

    else:
        with open(path, "r+") as file1:

            amount = int(input("Enter amount to Deposit: "))
            
            file1.seek(0)
            balance = file1.read()
            if len(balance) == 0: 
                balance = 0
            
            Label(tk, text="Opening balance: {0}".format(balance), width=15, anchor="w").grid(row=10, column=1)
        
            file1.seek(0)
            balance = eval(balance) + amount
            file1.write(str(balance))

            file1.seek(0)
            balance = file1.read()
            Label(tk, text="Closing balance: {0}".format(balance), width=15, anchor="w").grid(row=10, column=1)

Label(tk, text="Account Number : ", width=15, anchor="w").grid(row=1, column=1)
Label(tk, text="User Name : ", width=15, anchor="w").grid(row=2, column=1)
Entry(tk, width=15, textvariable=account_no, justify=RIGHT).grid(row=1, column=2, padx=(0,5))
Entry(tk, width=15, textvariable=user_name, justify=RIGHT).grid(row=2, column=2, padx=(0,5))

Button = Button(tk, text="Submit", command=transactionMenu).grid(row=3, column=1)

tk.mainloop()