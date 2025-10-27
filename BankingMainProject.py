from BankMenu import menu
from CustomerAdd import addcustomer
from CustomerPinUpdate import pinupdate
from CustomerView import viewallcustomer, viewcustomer
from Withdraw import withdraw
menu()
ch=int(input("Enter Ur choice:"))
match(ch):
    case 1:
        addcustomer()
    case 2:pass
    case 3:
        withdraw()
    case 4:pass
    case 5:
        viewcustomer()
    case 6:
        viewallcustomer()
    case 7:pass
    case 8:
        #pinupdate()
    case 9:
        print("\tThnx For using this Project")
    case _:
        print("\tUr selection of choice is wrong--try again")
