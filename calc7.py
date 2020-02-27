# version v0.7.3

import math

print("\nHello! Welcome to my first calculator on Python :)\n")

print("1. Summa (example: x + y)")
print("2. Minus (example: x - y)")
print("3. Multiplication (x * y)")
print("4. Divide (x / y)")
print("5. Exponent (e^x)")
print("6. Square root (sqrt(x))")
print("7. Power to (x ^ y)")
print("8. Factorial (n!)")
print('9. Exit')

while True:
    choise = input('\nPlease, choise what do you want: ')
    dchoise = (choise.isdigit())

    if dchoise == False:
        print('Error, exiting...')  ### If choise < 0 or 0.5  ???
    elif choise > '9' or choise < '1':
        print('Error. Enter from 1 to 9.')
    elif dchoise == True and choise <= '9' or choise >= '1':
        if choise == '1':  # Plus
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            print('x + y =', x + y)

        if choise == '2':  # Minus
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            print('x - y =', x - y)

        if choise == '3':  # Multiplication
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            print('x * y =', x * y)

        if choise == '4':  # Divide
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            if y != 0:
                print('x / y =', x / y)
            else:
                print('ERROR! Division by zero!')

        if choise == '5':  # Exponent
            E = 2.718281
            x = float(input('Enter x: '))
            print('E ^ x =', E ** x)

        if choise == '6':  # Square root
            x = float(input('Enter x: '))
            if x > 0:
                print('sqrt(x) =', math.sqrt(x))
            else:
                print('ERROR! Square root from negative number')

        if choise == '7':  # Power to
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            # print('x ^ y =', x**y)
            print('x ^ y =', pow(x, y))

        if choise == '8':  # Factorial
            n = int(input('Enter n: '))
            def calc_factorial(x):
                if x == 1:
                    return 1
                else:
                    return (x * calc_factorial(x - 1))
            print("The factorial of", n, "is", calc_factorial(n))

        if choise == '9':
            print('Exiting. Good bye')
            exit()