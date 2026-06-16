print("Expense Tracker")

expenses = []
total =[]
total_amount = 0

while True:
    value = 0

    menu = ["1. Add Expense", "2. Show Expense", "3. Total Spent", "4. Exit"]
    for i in menu:
        print(i)
    value = input("Enter the index: ")

    if value in ["1", "2", "3", "4"]:

        if value == "1":
            expense = input("Enter expense name: ")
            amount = input("Enter amount spent: ")
            expenses.append({"name":expense,"amount":amount})
            total.append(int(amount))
        elif value == "2":
            if len(expenses) == 0:
                print("No expenses")
            else:
                for ex in expenses:
                    print(f'{ex["name"]}: {ex["amount"]}')
        elif value == "3":
            if len(expenses) == 0:
                print("Total amount Spent: 0")
            else:
                for i in total:
                    total_amount += i
            print(f"Total amount Spent: {total_amount}")
            total_amount = 0
        elif value == "4":
            print("Thank you for using Expense Tracker")
            break






