from art import logo


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


def calculator():  # ! This is the recursion! it calls it self

    print(logo)

    num1 = float(input("whats the first number: "))
    for symbol in operations:
        print(symbol)

    should_continue = True  # //! this is a condition for the while loop

    while should_continue:

        operation_symbol = input("Pick an operation from the lines above: ")
        num2 = float(input("whats the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2}= {answer}')
        user_options = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, type q to exit: ")

        if user_options == "y":
            num1 = answer
        elif user_options == "n":
            should_continue = False
            calculator()  # ! when the if statement is false this will call it self to the def calculator and it will start all over again
        else:
            should_continue = False


calculator()  # ! recursion calling
