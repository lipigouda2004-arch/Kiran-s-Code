#EmlopyeeUpdate.py<----Module name
import pickle
def updatepin():
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","rb") as fp:
        records=list()
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    found=False
    Acno=int(input("Enter Account Number to Update pin:"))
    for index in range(len(records)):
        if(records[index][0]==Acno):
            found=True
            recindex=index
            break
    if(found):
        newpin=int(input("Enter New pin for update pin:"))
        records[recindex][3]=newpin
        with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("Pin Updated----Verify")
    else:
        print("Customer does not exist")


