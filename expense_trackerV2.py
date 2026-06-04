print("Expense Tracker")

expenses = []


def load_expenses():

    keys_list = ["name", "amount", "category"]

    with open('expenses.txt', 'r') as r:
        for line in r:
            clean_line = line.strip()
            new_dict = dict(zip(keys_list, clean_line.split(",")))
            new_dict['amount'] = int(new_dict['amount'])
            expenses.append(new_dict)

def save_expenses(expense, amount, category):
    with open('expenses.txt', 'a') as f:
        f.write(f'{expense},{amount},{category}\n')

    save_dict = {"name" : expense, "amount" : amount, "category" : category}
    expenses.append(save_dict)
        
def add_expense():
    expense = input("Enter expense name: ").lower()

    while True:
        try:
            amount = int(input("Enter amount spent: "))
        except ValueError:
            print("Error! Enter correct amount")
            continue
        break

    category = input("Enter category: ")
    save_expenses(expense, amount, category)


def show_expenses():
    if expenses:
        for x in expenses:
            print(f'{x['name'].title()} - {x['amount']} - {x['category'].title()}')
    else:
        print("No expenses found.")

def calculate_total():
    totals = {}
    for i in expenses:
        category = i['category']
        if category in totals:
            totals[category] += i['amount']
        else:
            totals[category] = i['amount']

    for expense in totals:
        amount = totals[expense]
        print(f'{expense.title()} total = {amount}')
            

load_expenses()

while True:


    menu = ["\n1. Add Expense", "2. Show Expense", "3. Total Spent", "4. Exit"]
    for i in menu:
        print(i)

    choice = input("Enter the index: ")
    print()

    if choice == "1":
        add_expense()            
            
    elif choice == "2":
        show_expenses()

    elif choice == "3":
        calculate_total()
                    
    elif choice == "4":
        print("Thank you for using Expense Tracker")
        break






