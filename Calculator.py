
# CALCULATOR

def add(x, y):
   return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return float(x) / float(y)

print("What would you like to do? \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide")

while True:

    choice = input("Input operation selection here! ")

    if choice in ('1', '2', '3', '4'):
        num1 = int(input('Enter first Number '))
        num2 = int(input('Enter Second Number '))

        if choice == '1':
            print(num1, "+", num2, "=", (add(num1, num2)))

        if choice == '2':
            print(num1, "-", num2, "=", (subtract(num1, num2)))

        if choice == '3':
            print(num1, "x", num2, "=", (multiply(num1, num2)))

        if choice == '4':
            print(num1, "/", num2, "=", (divide(num1, num2)))






















