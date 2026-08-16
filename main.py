import interpretador as itp
from utilidades import texto

print("\033[H\033[J")
texto("calculadora\n\n", 0.05)
texto('inserte "salir" para', 0.05)
texto("... ", 0.5)
texto("salir\n\n", 0.05)

while True:

    expresion = input("inserte expresion: ")
    print()

    if expresion.strip().lower() == "salir":
        texto("saliendo", 0.05)
        texto("... ", 0.5)
        texto("este tiempo de carga es falso btw\n\n", 0.05)
        break  # hola dani

    try:
        resultado = itp.enlistar(expresion)
        resultado = itp.parentesis(resultado)

        print(f"resultado: {resultado}\n")

    except ZeroDivisionError:
        texto("no puedes dividir entre cero\n\n", 0.05)

    except Exception:
        texto("debes introducir una expresion valida\n\n", 0.05)
