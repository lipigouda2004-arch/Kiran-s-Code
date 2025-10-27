#EmployeeSearch.py<----Module Name
import pickle
def searchcustomer():
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","rb") as fp:
        records=list()
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    Acno=int(input("Enter Account Number to Search:"))
    found=False
    for record in records:
        if (record[0]==Acno):
            found=True
            break
    print("-"*50)
    if(found):
        print("Customer Found---Valid Employee")
    else:
        print("Customer Does not Exist---Invalid Employee")
        print("-"*50)


