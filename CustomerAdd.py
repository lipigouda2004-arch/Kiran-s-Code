#CustomerAdd.py<----module name and file name
import pickle
def isunique(Acno):
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","rb") as fp:
        records=list()
        while (True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
#check for unique
    found=True
    for record in records:
        if(record[0]==Acno):
            found=False
            break
    return found
def addcustomer():
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data", "ab") as fp:
        try:
            print("-"*40)
            Acno=int(input("Enter Account Number:"))
            if(isunique(Acno)):
                CustomerName=input("Enter Customer Name:")
                bal=int(input("Enter Balance:"))
                Pin=int(input("Enter Only 4-digit Pin:"))
                print("-"*40)
                lst=list()
                lst.append(Acno)
                lst.append(CustomerName)
                lst.append(bal)
                lst.append(Pin)
                pickle.dump(lst,fp)
                print("Customer data saved successfully in file")
            else:
                print("Account No. already exists in file---try again with new")
        except ValueError:
            print("Don't enter alnums,strs and symbols for acno,bal,pin")
