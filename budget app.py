class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        total = 0
        expenses = 0
        for dict in self.ledger:
            expenses = dict["amount"]
            total += expenses
        return print("Current balance: ", total)

    def withdraw(self, amount, description):
        amount = 0 - amount

        if self.ledger[0]:
            self.ledger.append({"amount": amount, "description": description})
        else:
            pass

    def transfer(self, amount, another_budget_category):
        amount = 0 - amount
        description = "Transfer to " + another_budget_category
        self.ledger.append({"amount": amount, "description": description})

        if another_budget_category == "Clothing":
            clothing.withdraw(amount, "Transfer from food")
        else:
            pass


food = Category("Food")
food.deposit(1000, "Initial deposit")
food.withdraw(10.15, "Groceries")
food.withdraw(15.89, "dessert")
clothing = Category("Clothing")
clothing.deposit(1000, "Initial deposit")
clothing.withdraw(10.15, "shirt")
food.transfer(50, "Clothing")
food.check_funds(500)


def spent_by_category(category):

    name = category.name
    width = 30
    width_without_name = (30 - len(name)) / 2
    width_without_name = int(width_without_name)

    # Category name with stars
    cool_name = []
    for x in range(width_without_name):
        cool_name.append("*")
    cool_name.append(name)
    for x in range(width_without_name):
        cool_name.append("*")
    print("".join(cool_name))

    for dict in category.ledger:
        withdrawal = []
        for value in dict.values():
            if type(value) != str:
                value = str(value)
                withdrawal.append(value)
            else:
                withdrawal.append(value)
        print(withdrawal[1] + ":",  withdrawal[0])
    category.get_balance()


spent_by_category(food)
spent_by_category(clothing)





