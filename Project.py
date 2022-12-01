print("***Welcome To System To Slice Emails*** ")
start1=input("Do you want to start the program(yes/no): ")
if start1.lower() != 'yes':
    print("GoodBye")
    print()
    print()
    print()
    print()
    print()                
    input("Press enter to close")
    quit()
else:
    number=int(input("How many emails do you have? "))
    i = 1
    count = 1
    while(i<=number):
        c = print("Enter Email: ",i)
        email=input("").strip()
        a = '@gmail.com'
        b = '@yahoo.com'
        
        
        if a in email or b in email:
            pass
        else:
            print("Invalid email")
            email=input("Try Again: ")  
        i+=1
       
        for x in range(1,i):
            if '@' in email: 
                username = email[:email.index("@")]
                domain =   email[email.index("@")+1:]    
                print("Username: ",username.capitalize(),"and Domain: ",domain.upper())
                print("")
                break
            else:
                print("Error: invalid email: ",i-1)
print()
print()
print()
print()
print()                
input("Press enter to close")
            
            



    
            
