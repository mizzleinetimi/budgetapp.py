class budget:
    


    def __init__(self, category,amount):
        self.category = category
        self.amount = amount

    def operation(self):
        operand = int(input("welcome \n select an option to proceed: \n 1. deposit \n 2.withdraw \n 3. check balance \n 4.transfer \n"))
        if operand == 1:
            self.deposit()
        elif operand == 2:
           self.withdraw()
        elif operand == 3:
            self.balance()
        elif operand == 4:
            self.transfer()
        else:
            print("invalid input, try again.")
            self.operation()
    
    def deposit(self):
        depamnt = int(input("how much would you like to deposit? \n"))
        print(f'you deposited {depamnt},your new balace is {depamnt + self.amount}.')
        self.another()


    def balance(self):
        print(f'here is your current balance: \n {self.amount}')
        self.another()


    def withdraw(self):
        collect = int(input("how much would you like to wiithdraw?"))
        if collect >= self.amount:
            print("insufficient funds")
            self.withdraw()
        elif collect < self.amount:
            print(f'you withdrew {collect} from {self.category} balance')
            collect-self.amount
            self.another()
        else:
            print("invalid input")
            self.withdraw()

    def transfer(self):
        transf = int(input("how much would you like to transfer? \n"))
        person = int(input("enter account number of recipient \n"))
       

        if transf > self.amount:
            print("insufficient balance")
            self.transfer()
        else:
            print( f'you successfully sent {transf} to {person}')
            self.another()



    def another(self):
        nother = str(input("would you like to perform another operation? \n select(Y/N) \n")).upper()
   
        if (nother == "Y"):
            self.operation()
        elif(nother == "N"):
            exit()
        else:
            print("invalid input")
            self.another()


catg1 = budget("clothing",1000)
catg2 = budget("food",1000)
catg3 = budget("entertainment",1000)

catg1.operation()
print(' thanks genius')