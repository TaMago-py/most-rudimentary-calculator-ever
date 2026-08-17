import interpreter as itp
from utils import typewriter

print("\033[H\033[J")
typewriter("calculator\n\n", 0.05)
typewriter('Type "exit" to', 0.05)
typewriter("... ", 0.5)
typewriter("Exit\n\n", 0.05)

while True:

    expression = input("Enter expression: ")
    print()

    if expression.strip().lower() == "exit":
        typewriter("Shutting down", 0.05)
        typewriter("... ", 0.5)
        typewriter("This loading screen is fake btw\n\n", 0.05)
        break  # hola dani

    try:
        result = itp.transform(expression)
        result = itp.parentheses(result)

        print(f"Result: {result}\n")

    except ZeroDivisionError:
        typewriter("Error: You can't divide by zero\n\n", 0.05)

    except Exception:
        typewriter("Error: Please enter a valid expression\n\n", 0.05)
