def transform(text: str):

    changes = {
        " ": "",
        ",": ".",
        "^": "**",
        "{": "(",
        "}": ")",
        "[": "(",
        "]": ")"
        }

    for old, new in changes.items():
        text = text.replace(old, new)

    expression = []
    actual_number = ""
    power = ""
    allowed = "0123456789.+-*/()"

    for character in text:

        if character not in allowed:
            raise ValueError

        if expression == [] or expression[-1] == "(":
            if (character == "+" or character == "-") and not actual_number:
                actual_number += character
                continue

        if character.isdigit() or character == ".":
            if power:
                expression.append(power)
                power = ""

            actual_number += character

        elif character == "*":
            if actual_number:
                expression.append(float(actual_number))
                actual_number = ""

            if len(power) <= 1:  # le voy a poner un testo al dani, hola dani
                power += character

            else:
                raise ValueError

        else:
            if actual_number:
                expression.append(float(actual_number))
                actual_number = ""

            if power:
                expression.append(power)
                power = ""

            expression.append(character)

    if actual_number:
        expression.append(float(actual_number))
        actual_number = ""

    return expression


def power(expression: list):

    while "**" in expression:

        for i in range(len(expression)):
            operator = expression[i]

            if operator == "**":
                number_a = expression[i - 1]
                number_b = expression[i + 1]

                if operator == "**":
                    result = number_a ** number_b

                for _ in range(3):
                    expression.pop(i - 1)

                expression.insert(i - 1, result)

                break

    return expression


def multiplication(expression: list):

    while "*" in expression or "/" in expression:

        for i in range(len(expression)):
            operator = expression[i]

            if operator == "*" or operator == "/":
                number_a = expression[i - 1]
                number_b = expression[i + 1]

                if operator == "*":
                    result = number_a * number_b

                else:
                    result = number_a / number_b

                for _ in range(3):
                    expression.pop(i - 1)

                expression.insert(i - 1, result)

                break

    return expression


def add(expression: list):

    while "+" in expression or "-" in expression:

        for i in range(len(expression)):
            operator = expression[i]

            if operator == "+" or operator == "-":
                number_a = expression[i - 1]
                number_b = expression[i + 1]

                if operator == "+":
                    result = number_a + number_b

                else:
                    result = number_a - number_b

                for _ in range(3):
                    expression.pop(i - 1)

                expression.insert(i - 1, result)

                break

    return expression


def parentheses(expression: list):
    if "(" not in expression and ")" not in expression:
        expression = power(expression)
        expression = multiplication(expression)
        expression = add(expression)
        return expression[0]

    if expression.count("(") != expression.count(")"):
        raise ValueError

    for i in range(len(expression)):
        if expression[i] == ")":
            closing = i
            break

    for i in range(closing, -1, -1):
        if expression[i] == "(":
            opening = i
            break

    parenthesized_expression = expression[opening + 1 : closing]

    result = power(parenthesized_expression)
    result = multiplication(result)
    result = add(result)[0]

    for _ in range(closing - opening + 1):
        expression.pop(opening)

    expression.insert(opening, result)

    return parentheses(expression)
