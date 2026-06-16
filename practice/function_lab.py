def greet():
    return 'Welcome'

def greet_user(name):
    print(f'{greet()} {name}')

def add(a, b):
    return a + b

def calculate_total(expenses):
    
    total = 0

    for i in expenses:
        total += i
    return total

expenses = [100, 200, 300]
print(calculate_total(expenses))