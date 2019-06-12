def controller():

    from threa import threadd
    from temp3 import go
    from register import register_face
    from temp2 import findface
    from storecsv import csv 

    print(""""
    --------------------------------------------------------------
    _________________Welcome to Smart Attendence__________________
    
    --------------------------------------------------------------
    Choose the following from the set of options
    
    Press ( 1 ) for SignIn
    Press ( 2 ) for Signout
    Press ( 3 ) to add new User  
    Press ( 4 ) to remove existing User  
    Press ( 5 ) to know your SignIn and Signout History
    """)
    x = int(input("Enter from the given set of options : "))
    if(x == 1):
        threadd()
    elif(x == 2):
        go()
    elif(x == 3):
        register_face()
    elif(x == 4):
        print("Functionality not added")
    elif(x == 5):
        print("Functionality not added")

    else:
        print("___ Enter a valid Number ___ ")
    
    controller()

controller()
