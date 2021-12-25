print("     Welcome to the most basic calculator, Made by one and only... Sid")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    return x / y


def mul(x, y):
    return x * y


# Taking Input from the user
while True:
    print("Select the operation:")
    print("\"a\" for addition")
    print("\"s\" for subtraction")
    print("\"m\" for multiplication")
    print("\"d\" for Division")

    user_input = input("Enter operation (a,s,m,d):")

    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))

    if user_input == 'a':
        print(x, "+", y, "=", add(x, y))

    elif user_input == 's':
        print(x, "-", y, "=", sub(x, y))

    elif user_input == 'm':
        print(x, "*", y, "=", mul(x, y))

    elif user_input == 'd':
        print(x, "/", y, "=", div(x, y))

    else:
        print("Either you can't read or I messed up this program... Try again bozo")

    user_input = input("press r to restart or q to quit")

    if user_input == 'r':
        continue

    elif user_input == 'q':
        print("Have an amazing day friendo :)")

    else:
        print("You really can't read huh...Go back to school...BYE! *sighs*")

    break  # program stops here
