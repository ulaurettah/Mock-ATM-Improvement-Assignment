from datetime import*
Balance=500000
name = input("What is your UserName? \n")
allowedUsers=['Seyi','Mike','Love']
allowedPassword =['passwordSeyi','passwordMike','passwordLove']

import random
database ={}
def init():
    
    if(name in allowedUsers):
        password = input("your password? \n")
        userId = allowedUsers.index(name)

    else:
        print('Name not found, Please try again')

    if(password == allowedPassword[userId]):
        print(datetime.now())
    else:
        print('Password Incorrect, please try again')
    
        print('Welcome %s' % name)
    isValidOptionSelected =False
    print("Welcome to bankPHB")

    while isValidOptionSelected ==False:

        haveAccount =int(input("Do you have account with us: 1(yes) 2 (no)\n"))

        if(haveAccount ==1):
            isValidOptionSelected =True
            login()
        elif(haveAccount ==2):
            isValidOptionSelected =True
            register()
        else:
            print("You have selected invalid option")
def login():
            print("********** Login *********")

            accountNumberFromUser = int(input("What is your account number?\n"))
            password = input("What is your password\n")

            for accountNumber, userDetails in database.items():
                    if(accountNumber == accountNumberFromUser):
                        if(userDetails[3] ==password):
                            bankOperation(userDetails)

            print('invalid account or password')
            login()

def register():
        print("******Register******")
        email= input("What is your email address?\n")
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        password = input("create a password for yourself\n")

        accountNumber =generateAccountNumber()

        database[accountNumber] =[first_name, last_name, email, password]

        print("Your Account Has been created")
        print("== === ==== === ==")
        print("Your account number is:%d" % accountNumber)
        print("Make sure you keep it safe")
        print("== === ===== ==== ===")

        login()
def bankOperation(user):
    print('these are the available options')
    print("Welcome %s %s" % (user[0], user[1]))
    isSelectedOptionValid = False
    while isSelectedOptionValid == False:

        selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Complaint (4) Exit\n"))

        if(selectedOption == 1):
            
            depositOperation(selectedOption)
        elif(selectedOption == 2):
            
            withdrawalOperation(selectedOption)
        elif(selectedOption == 3):
            
            feedback(selectedOption)
        elif(selectedOption == 4):
            
            exit()
        else:

            print("invalid option selected")
            bankOperation()
def withdrawalOperation(selectedOption):
    global Balance
    print("withdrawal")
    print('you selected %s' % str(selectedOption))
    Response= int(input('How Much do you want to collect'))
    if Response<= Balance:
        Balance=Balance-Response
        print('you have withdrawn N%d'%Response)
        print('Please take your Cash')
    else:
        print('insufficient fund')


def depositOperation(selectedOption):
    global Balance
    print("Deposit Operations")
    print('you selected %s' % str(selectedOption))
    Deposit= int(input('How Much would you like to deposit ?'))
    Balance=Balance+Deposit
    print('Your Balance is N%d'%Balance)


def feedback(selectedOption):
    print("Feedback section")
    print('you selected %s' % str(selectedOption)) 
    complaint=input('complaint type')
    print('Thank you for contacting us')

def generateAccountNumber():
    print("account number generator")
    return random.randrange(1111111111,9999999999)
   
def logout():
    login()

    #### ACTUAL BANKING SYSTEM #####
init()
