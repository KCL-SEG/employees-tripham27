"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class Salary_Employee(Employee):
    def __init__(self,name,salary,numContracts=0,contractCommission=0,bonus=0):
        self.name = name
        self.salary = salary
        self.numContracts = numContracts
        self.contractCommission = contractCommission
        self.bonus = bonus

    def get_pay(self):
        totalPay = self.salary
        if self.numContracts:
            totalPay += self.numContracts * self.contractCommission
        if self.bonus:
            totalPay += self.bonus
        return totalPay

    def __str__(self):
        output = f"{self.name} works on a monthly salary of {self.salary}"
        if self.numContracts:
            output += f" and receives a commission for {self.numContracts} contract(s) at {self.contractCommission}/contract."
        elif self.bonus:
            output += f" and receives a bonus commission of {self.bonus}."
        else:
            output += "."
        output += f" Their total pay is {self.get_pay()}."
        return output

class Hourly_Employee(Employee):
    def __init__(self,name,hours,wage,numContracts=0,contractCommission=0,bonus=0):
        self.name = name
        self.hours = hours
        self.wage = wage
        self.numContracts = numContracts
        self.contractCommission = contractCommission
        self.bonus = bonus

    def get_pay(self):
        totalPay =  self.hours * self.wage
        if self.numContracts:
            totalPay += self.numContracts * self.contractCommission
        if self.bonus:
            totalPay += self.bonus
        return totalPay

    def __str__(self):
        output = f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour"
        if self.numContracts:
            output += f" and receives a commission for {self.numContracts} contract(s) at {self.contractCommission}/contract."
        elif self.bonus:
            output += f" and receives a bonus commission of {self.bonus}."
        else:
            output += "."
        output += f" Their total pay is {self.get_pay()}."
        return output



 # Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary_Employee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee('Charlie',100,25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary_Employee('Renee',3000,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Employee('Jan',150,25,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary_Employee('Robbie',2000,0,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Employee('Ariel',120,30,0,0,600)


