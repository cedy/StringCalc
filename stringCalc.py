import math
math_operators_precedence = \
    {"^": 4,
     "*": 3,
     "/": 3,
     "+": 2,
     "-": 2,
     "(": 0,
     ")": 0}

def main():

    print("Please enter mathematical expression. For exit type 'exit'")
    while True:
        user_input = input()
        if user_input == "exit":
            print("Bye.")
            break
        else:
            notation = to_polish_notation(user_input)
            result = calculate_polish_notation(notation)
            print(user_input + " = " + str(result))


def to_polish_notation(string):
    operationStack = []
    polishNotation = []
    string = string[::-1]
    string = [str(x) for x in string]
    while string:
        element = string.pop()
        if is_digit(element):
            number = element
            while True:
                # collecting numbers with point and pushing them to notation. '1', '.', '3' = '1.3'
                if len(string) == 0:
                    break
                element = string.pop()
                if is_math_operator(element) or element == "(" or element == ")":
                    break
                number += element

            polishNotation.append(number)

        if is_math_operator(element):
            # while on stack math operator has stronger power and is left associated
            # move elements from stack of operators to notation list
            if len(operationStack) > 0:
                while math_operators_precedence[operationStack[-1]] >= math_operators_precedence[element] and element != "^":
                    polishNotation.append(operationStack.pop())
                    if len(operationStack) == 0:
                        break
            operationStack.append(element)

        if element == "(":
            operationStack.append(element)

        if element == ")":
            while(operationStack[-1] != "("):
                # until we find opening, move elements from stack of operators to notation list
                polishNotation.append(operationStack.pop())
            operationStack.pop() # removes opening bracket

    while(operationStack):
        # move whatever left in stack of operators to notation list
        polishNotation.append(operationStack.pop())
    return polishNotation


def calculate_polish_notation(notation):
    calculation_stack = []
    for element in notation:
        if is_math_operator(element):
            operand_1 = calculation_stack.pop()
            operand_2 = calculation_stack.pop()
            if element == "^":
                result = math.pow(float(operand_2), float(operand_1))
            else:
                result = eval(str(operand_2) + element + str(operand_1))
            calculation_stack.append(result)
        else:
            calculation_stack.append(element)
    return calculation_stack.pop()

def is_digit(value):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    return value in digits

def is_math_operator(value):
    mathFuncs = ("+", "-", "*", "/", "^")
    return value in mathFuncs


if __name__ == "__main__":
    main()