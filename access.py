while True:
    account_name = ['abdullahi usman musa']
    ussd = int(input("please type in your ussd code"))
    if ussd == 901:
        print('1.check balance \n2. transfer \n3. airtime \n4. other services \n 5. access money \n6. Diamond extra \n7. xtracash loan \n8. mobile wallet')
        option = int(input('select option'))
    if (option == 1):
        pin = int(input('enter pin'))
        print('you account balance is 500000 Naira')
        break
    elif (option == 2):
        amount = int(input('enter amount'))
        account = int(input('enter account number'))
        print("1. access bank \n2. first bank \n3. zenith bank")
        option = int(input("enter beneficiary bank"))
        if (option == 1):
            print("you want  to tranfer",amount,account_name,)
            pin = int(input("enter pin"))
            print("transaction successful")
        elif (option == 2):
            print("you want  to tranfer",amount,account_name,)
            pin = int(input("enter pin"))
            print("transaction successful")
        elif (option == 3):
            print("you want  to tranfer",amount,account_name,)
            pin = int(input("enter pin"))
            print("transaction successful")
            break
    elif (option == 3):
        print("1. self \n2. others")
        option = int(input('select option'))
        if (option == 1):
            amount = int(input('enter amount'))
            pin = int(input('enter pin:'))
            print("trasfer successful")
            break
        elif (option == 2):
            amount = int(input('enter amount'))
            number = int(input('enter phone number'))
            print("trsaction successful")
            break
    elif (option == 4):
        print("1. paybill \n2. accesspay \n3. pay day long \n4. enquary service \n5. resetpin \n6. cardless withdrawal \n7. refferal scheme \n8. update info\n9. opt out")
        option = int(input('select option'))
        for keep in range(0,10): 
            if option == keep:
                print('sorry not currently available')
        break
    elif (option == 5):
        option = int(input('select option'))
        print("sorry,this service is currently unavailable. we are working to restore it soon.Kindly use our alternative channels")
    elif (option == 6): 
        print("sorry,this service is currently unavailable. we are working to restore it soon.Kindly use our alternative channels")
    elif (option == 7): 
        print("sorry,this service is currently unavailable. we are working to restore it soon.Kindly use our alternative channels")
    elif (option == 8): 
        print("sorry,this service is currently unavailable. we are working to restore it soon.Kindly use our alternative channels")
        break  
    else:
        ussd = int(input("please type in your ussd code"))
