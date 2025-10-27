#CustomerView.py<---module name
import pickle
def viewcustomer():
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","rb") as fp:
        all_records=list()
        while(True):
            try:
                customer_records=pickle.load(fp)
                all_records.append(customer_records)
            except EOFError:
                break
    Acno=int(input("enter Account No.to view detals:"))
    found=False
    for record in all_records:
        if(record[0]==Acno):
            found=True
            rec=record
            break
    if(found):
        print("-"*50)
        print("Customer Acno:{}".format(rec[0]))
        print("Customer Name:{}".format(rec[1]))
        print("Customer Balance:{}".format(rec[2]))
        print("Customer Pin:{}".format(rec[3]))
        print("-"*50)
    else:
        print("Customer does not exist---invalid customer")
def viewallcustomer():
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","rb") as fp:
        print("-"*40)
        print("\tACNO\tCustNAME\tBALANCE\tPIN")
        print("-"*40)
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("-"*40)
                break
