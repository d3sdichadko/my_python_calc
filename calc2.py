# version v0.5

import math

print("\nHello! Welcome to my first calculator on Python :)\n")

print("Summa (example: x + y): 1")
print("Minus (example: x - y): 2")
print("Multiplaying: 3")
print("Divide: 4")
print("Exponent: 5")
print("Square root: 6")
print("Power to: 7")
print("Factorial (n!): 8")

choise = input('Please, choise what do you want: ')

dchoise = (choise.isdigit())

if dchoise == False:
    print('Error, exiting...')
elif dchoise == True:
   if choise == 1:
      x = float(input('Enter x: '))
      y = float(input('Enter y: '))
      print('x + y =', x + y)

if choise == 2:
   x = float(input('Enter x: '))
   y = float(input('Enter y: '))
   print('x - y =', x - y)

if choise == 3:
   x = float(input('Enter x: '))
   y = float(input('Enter y: '))
   print('x * y =', x * y)

if choise == 4:
   x = float(input('Enter x: '))
   y = float(input('Enter y: '))
   if y != 0:
      print('x / y =', x / y)
   else:
       print('ERROR! Division by zero!')

if choise == 5:
   E = 2.718281
   x = float(input('Enter x: '))
   print('E ^ x =', E**x)

if choise == 6:
   x = float(input('Enter x: '))
   if x > 0:
       print('sqrt(x) =', math.sqrt(x))
   else:
       print('ERROR! Square root from negative number')

if choise == 7:
   x = float(input('Enter x: '))
   y = float(input('Enter y: '))
   #print('x ^ y =', x**y)
   print('x ^ y =', pow(x,y))

if choise == 8:
   n = int(input('Enter n: '))
   def calc_factorial(x):
      if x == 1:
         return 1
      else:
         return (x * calc_factorial(x-1))
   print("The factorial of", n, "is", calc_factorial(n))
