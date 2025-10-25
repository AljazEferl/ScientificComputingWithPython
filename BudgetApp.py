class Category:
    
   

    def __init__(self, name ):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            description = entry['description'][:23]
            amount = f"{entry['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

           
            
        return description + ledgers + str(f"Total: {self.get_balance():.2f}") 

    def deposit(self,amount, description=""):
        self.ledger.append({'amount' : amount ,   'description': description})
    
    def withdraw(self, amount, description = ""):
        if  self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
            
        
    
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            #print(i['amount'])
            balance  += i['amount']

        return balance
            
    def transfer(self, amount,category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        return False
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

def create_spend_chart(categories):
    spent = []
    for category in categories:
        total_withdraw = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent.append(total_withdraw)

    total_spent = sum(spent)

    if total_spent == 0:
        percents = [0 for _ in spent]
    else:
        percents = [int(round(s / total_spent * 100, 0)) for s in spent]

    chart_lines = ["Percentage spent by category"]

    for row in range(100, -1, -10):
        line = f"{row:>3}|"
        for p in percents:
            line += " o " if p >= row else "   "
        line += " "
        chart_lines.append(line)

    chart_lines.append("    " + "-" * (len(categories) * 3 + 1))

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        chart_lines.append(line)

    return "\n".join(chart_lines)

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(10.15, 'groceries')
print(food)
print(clothing)

print(create_spend_chart([food, clothing]))