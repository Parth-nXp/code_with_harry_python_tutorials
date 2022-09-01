'''
Faulty calculator
Design a calculator which will correctly solve all the problems except the following ones:
45*3=555,
56+9=77,
56/6=4
Your program should take operator and the two numbers as input from the user and then return the result.
'''
operator = input(
    "Enter an operator (+, -, *, /): ")  # +, -, *, / will be taken as input to perform the operation

# number_1 will be taken as input to perform the operation
number_1 = int(input("Enter the first number: "))

# number_2 will be taken as input to perform the operation
number_2 = int(input("Enter the second number: "))

if operator == "+":
    if number_1 == 56 and number_2 == 9:
        print("56+9=77")
    elif number_1 == 9 and number_2 == 56:
        print("56+9=77")
    else:
        print(str(number_1) + operator + str(number_2) +
              "=" + str(number_1 + number_2))
elif operator == "-":
    print(str(number_1) + operator + str(number_2) +
          "=" + str(number_1 - number_2))
elif operator == "*":
    if number_1 == 45 and number_2 == 3:
        print("45*3=555")
    elif number_1 == 3 and number_2 == 45:
        print("45*3=555")
    else:
        print(str(number_1) + operator + str(number_2) +
              "=" + str(number_1 * number_2))
else:
    if number_1 == 56 and number_2 == 6:
        print("56/6=4")
    else:
        print(str(number_1) + operator + str(number_2) +
              "=" + str(number_1 / number_2))
