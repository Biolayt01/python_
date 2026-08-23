import art



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():

    print(art.logo)
    to_accumulate = True
    first_input = float(input("Enter your first number: "))

    while to_accumulate:

        operator_input = input("Enter any operator  from ( + or - or * or / ): ")
        second_input = float(input("Enter your second number: "))

        computation = operators[operator_input]

        result = computation(first_input, second_input)
        print(f"{first_input} {operator_input} {second_input} = {result}")


        continue_operation = input(f"Enter Y to continue calculating with {result} or N to begin another one: ").upper()
        if continue_operation == "Y":
            first_input = result
        else:
            to_accumulate = False
            calculator()



calculator()





