print(''' _____________________
|  _________________  |
| |              /  | |
| |       /\    /   | |
| |  /\  /  \  /    | |
| | /  \/    \/     | |
| |/             JO | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________| ''')


def add(n1, n2):
    """[this is the sum of 2 numbers]

    Args:
        n1 ([int]): [first number]
        n2 ([int]): [second number]

    Returns:
        [int]: [result of the sum]
    """
    return n1+n2


def substraction(n1, n2):
    """[this is the subtraccion of two numbers only positive result ]

    Args:
        n1 ([int]): [first number]
        n2 ([int]): [second number]

    Returns:
        [int]: [return of the substracion]
    """
    if n2 > n1:
        return n2-n1
    else:
        return n1-n2


def multiplication(n1, n2):
    """"multiplication of 2 numbers"""
    return n1*n2


def division(n1, n2):
    """ Division of 2 numbers the biggers always gets diveded"""
    if n2 > n1:
        return n2/n1
    else:
        return n1/n2


operations = {
    "+": add,
    "-": substraction,
    "*": multiplication,
    "/": division
}

num1 = int(input("whats the first number: "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the lines above: ")
num2 = int(input("whats the second number: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f'{num1} {operation_symbol} {num2}= {first_answer}')

# //!  This part is for a secondary operation and use of returns
operation_symbol = input("pick another operation: ")
num3 = int(input("whats the next number: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
