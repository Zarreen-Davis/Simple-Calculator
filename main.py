operation=input("""Please choose the Math operation you would like to perform: 
+ for addition
- for subtraction
* for multiplication
/ for division
** for to the power of """)

number_1=int(input("Enter your first number: "))
number_2=int(input("Enter your second number: "))

if operation == '+':
  print("{} + {} = ".format(number_1, number_2))
  print(number_1 + number_2)

elif operation == '-':
  print("{} - {} = ".format(number_1, number_2))
  print(number_1 - number_2)


elif operation == '*':
  print("{} * {} = ".format(number_1, number_2))
  print(number_1 * number_2)

elif operation == '/':
  print("{} / {} = ".format(number_1, number_2))
  print(number_1 / number_2)

elif operation == '**':
  print("{} ** {} = ".format(number_1, number_2))
  print(number_1 ** number_2)
