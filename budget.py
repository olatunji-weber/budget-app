class Category:
  def __init__(self,name):
    self.categoryName = name
    self.ledger = []

  def __str__(self):
    myString = f"{self.categoryName:*^30}\n"
    #items = ""
    total = 0
    for item in self.ledger:    #Loop through the ledger's lines
      myString += f"{item['description']:23.23}" + f"{item['amount']:>7.2f}\n"
      total += item['amount']
    return myString + "Total: " + str(total)
  
  def deposit(self, amount, description=""):
    #Method to add an amount to the balance and log the ledger
    depositItem = {"amount": amount, "description": description}
    self.ledger.append(depositItem)
    
  def withdraw(self, amount, description=""):
    #Method to deduct an amount from balance and log the ledger
    withdrawItem = {"amount": -amount, "description": description}
    if self.check_funds(amount):
      self.ledger.append(withdrawItem)
      return True
    else:
      return False

  def get_balance(self):
    #Method to determine the current balance
    currentBalance = 0
    for item in self.ledger:
      currentBalance += item["amount"]
    return currentBalance

  def transfer(self, amount, category):
    #call withdraw function with arguments amount & "Transfer to [Destination Budget Category]"
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.categoryName}")
      category.deposit(amount, f"Transfer from {self.categoryName}")
      return True
    else:
      return False
  
  def check_funds(self, amount):
    #Method to check amount is up to the funds available
    if amount > self.get_balance():
      return False
    elif self.get_balance() >= amount:
      return True

def create_spend_chart(categories):
    pass