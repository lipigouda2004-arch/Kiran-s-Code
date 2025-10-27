#ATMOperations.py<---Module Name
from BankExcept import WithdrawError,DepositError,InsuffFundError
import pickle
def deposit():
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data","rb") as fp:
        records = list()
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    Acno=int(input("Enter Account Number for Deposit:"))
    found=False
    for index in range(len(records)):
        if records[index][0] == Acno:
            found = True
            recindex = index
            break
    if found:
        bal=records[recindex][2]
        damt=int(input("Enter Deposit Amount:"))
        try:
            if damt<=0:
                raise DepositError
        except DepositError:
            print("\tDon't try to deposit -ve/zero value----try again")
        except ValueError:
            print("\tDon't enter alnums,strs,symbols----try again")
        else:
            bal=bal+damt
            print("\tUr Account {} Credited with INR:{}".format(Acno,damt))
            print("\tUr Account {} Balance After Deposit INR:{}".format(Acno,bal))
            records[index][2] = bal
            with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data", "wb") as fp:
                for records in records:
                    pickle.dump(records, fp)
                print("record updated successfully")
    else:
        print("Customer Does Not Exist")
def withdraw():
    with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data", "rb") as fp:
        records = list()
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    Acno = int(input("Enter Account Number for withdraw:"))
    found = False
    for index in range(len(records)):
        if records[index][0] == Acno:
            found = True
            recindex = index
            break
    if found:
        bal=records[recindex][2]
        wamt=int(input("Enter Withdraw Amount:"))
        try:
            if wamt<=0:
                raise WithdrawError
            elif (wamt+500)>bal:
                raise InsuffFundError
        except InsuffFundError:
            print("\tur account does not have enough fund----try again")
        except WithdrawError:
            print("\tDon't try to Withdraw -ve/zero value----try again")
        except ValueError:
            print("\tDon't enter alnums,strs,symbols----try again")
        else:
            bal=bal-wamt
            print("\tUr Account {} Debited with INR:{}".format(Acno, wamt))
            print("\tUr Account {} Balance After withdraw INR:{}".format(Acno, bal))
            records[index][2] = bal
            with open("C:\\Users\\HP 440 G8\\PycharmProjects\\Banking Project\\bankproject.data", "wb") as fp:
                for records in records:
                    pickle.dump(records, fp)
                print("record updated successfully")
    else:
        print("Customer Does Not Exist")












