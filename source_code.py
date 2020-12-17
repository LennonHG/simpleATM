# ATM by Lennon 

class ATM:
    def __init__(self, name, password):
        self.name = name 
        self.password = password
        
print("Welcome")
print("Please input password to continue")


balance = 1000
i = 0
tries = 3

while i <= tries:
    password = int(input("Enter Password: "))
    if password == 1234:
        print("Your balace is RM" + str(balance))
        break
    else:
        print("password incorrect, you have" + str(tries - i))
    i += 1

if password == 1234:
    print("")
else:
    print("Max tries has been reached")


    
