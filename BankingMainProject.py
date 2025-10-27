from BankMenu import menu
from CustomerAdd import addcustomer
from CustomerDelete import deleteemployee
from CustomerPinUpdate import updatepin
from CustomerSearch import searchcustomer
from CustomerView import viewcustomer, viewallcustomer
from CustomerUpdate import withdraw, deposit
while(True):
    try:
        menu()
        ch=int(input("Enter Ur choice:"))
        match(ch):
            case 1:
                addcustomer()
            case 2:
                deleteemployee()
            case 3:
                withdraw()
            case 4:
                deposit()
            case 5:
                viewcustomer()
            case 6:
                viewallcustomer()
            case 7:
                searchcustomer()
            case 8:
                updatepin()
            case 9:
                print("\tThnx For using this Project")
            case _:
                print("\tUr selection of choice is wrong--try again")
    except ValueError:
        print("Don't Enter Alnums ,strs,symbols for ur choice")
