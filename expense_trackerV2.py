print("Expense Tracker")


while True:

    expenses = []
    food_total =[]
    travel_total =[]
    clothes_total =[]
    food_amount = 0
    travel_amount = 0
    clothes_amount = 0

    menu = ["\n1. Add Expense", "2. Show Expense", "3. Total Spent", "4. Exit"]
    for i in menu:
        print(i)

    value = input("Enter the index: ")
    print()


    if value in ["1", "2", "3", "4"]:

        keys_list = ["name", "amount", "category"]
        values_list = []

        with open('expenses.txt', 'r') as r:
            for line in r:
                clean_line = line.strip()
                values_list.append(clean_line.split(","))
            
            for i in values_list:
                    new_dict = dict(zip(keys_list, i))
                    expenses.append(new_dict)

        if value == "1":
            expense = input("Enter expense name: ")
            amount = input("Enter amount spent: ")
            category = input("Enter category: ")

            with open('expenses.txt', 'a') as f:
                f.write(f'{expense},{amount},{category}\n')
            
            with open('expenses.txt', 'r') as r:
                for line in r:
                    values_list = line.split(",")
                    values_list.append(values_list)
                
            
        elif value == "2":
                             
            print(expenses)


        elif value == "3":
                        
            for i in expenses:
                if i['category'] == 'food':
                    food_total.append(int(i['amount']))
                if i['category'] == 'travel':
                    travel_total.append(int(i['amount']))  
                if i['category'] == 'clothes':
                    clothes_total.append(int(i['amount']))
            
            if len(food_total) > 0:
                for i in food_total:
                    food_amount += i
                print(f'Food total = {food_amount}')

            if len(travel_total) > 0:
                for i in travel_total:
                    travel_amount += i
                print(f'Travel total = {travel_amount}')

            if len(clothes_total) > 0:
                for i in clothes_total:
                    clothes_amount += i
                print(f'Clothes total = {clothes_amount}')

        elif value == "4":
            print("Thank you for using Expense Tracker")
            break






