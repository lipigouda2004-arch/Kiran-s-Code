#EmployeeDelete.py<----Module Name
import pickle
def deleteemployee():
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","rb") as fp:
        records=list()
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    found=False
    Acno=int(input("Enter Account Number to Delete:"))
    for index in range(len(records)):
        if(records[index][0]==Acno):
            found=True
            recindex=index
            break
    if(found):
        del records[recindex]
        with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmployee Deleted---Verify")
    else:
        print("Employee Does Not Exist")
