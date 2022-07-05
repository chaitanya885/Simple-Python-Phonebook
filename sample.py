print("Welcome to python phonebook 😊")
thisdict={
    "police" :100,
    "Ambulance": 108 
}
print("If you want to add contact to phonebook enter 1 ")
print("If you want to edit the contact  enter 2 ")
print("IF you want to search a contact number enter 3 ")
print ("If you want to delete contact number enter 4 ")
print("If you want to see contact list enter 5 ")
print("If you want to perform none of the options above enter 6 ")
while(True):
    print()
    k=int(input("Enter the action to be performed : "))
    if(k==1):
        m=input("Enter the name of the person to be added to phonebook :")
        h=int(input("Enter the mobile number :"))
        if((len(str(h))==10) and  (type(q)==int)):
            thisdict[m]=h
            print("Contact number added to phonebook sucessfully ")
        else:
            print("The phone number is invalid ")
    if(k==2):
        y=input("Enter the full contact name to be edited :")
        q=int(input("Enter the new mobile number :"))
        if((len(str(q))==10) and (type(q)==int)):
            thisdict.update({y:q})
            print("Contact number added to phonebook sucessfully ")
        else:
            print("The phone number is invalid ")
    if(k==3):
        t=input("Enter the contact name :")
        if(t in thisdict):
            h=thisdict[t]
            print(h)
        else:
            print("Contact not found in phonebook ")
    if(k==4):
        u=input("Enter the contact name to be deleted :")
        thisdict.pop(u)
        print("Contact deleted sucessfully ")
    if(k==5):
        print(thisdict)
    if(k==6):
        break



    

