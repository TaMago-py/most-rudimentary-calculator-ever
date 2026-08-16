def enlistar(texto: str):

    cambios = {" ": "", ",": ".", "^": "**", "{": "(", "}": ")", "[": "(", "]": ")"}

    for viejo, nuevo in cambios.items():
        texto = texto.replace(viejo, nuevo)

    lista = []
    numero_actual = ""
    potencia = ""
    permitidos = "0123456789.+-*/()"

    for caracter in texto:

        if caracter not in permitidos:
            raise ValueError

        if lista == [] or lista[-1] == "(":
            if (caracter == "+" or caracter == "-") and not numero_actual:
                numero_actual += caracter
                continue

        if caracter.isdigit() or caracter == ".":
            if potencia:
                lista.append(potencia)
                potencia = ""

            numero_actual += caracter

        elif caracter == "*":
            if numero_actual:
                lista.append(float(numero_actual))
                numero_actual = ""

            if len(potencia) <= 1:  # le voy a poner un testo al dani, hola dani
                potencia += caracter

            else:
                raise ValueError

        else:
            if numero_actual:
                lista.append(float(numero_actual))
                numero_actual = ""

            if potencia:
                lista.append(potencia)
                potencia = ""

            lista.append(caracter)

    if numero_actual:
        lista.append(float(numero_actual))
        numero_actual = ""

    return lista


def potencia(lista: list):

    while "**" in lista:

        for i in range(len(lista)):
            operador = lista[i]

            if operador == "**":
                numero_a = lista[i - 1]
                numero_b = lista[i + 1]

                if operador == "**":
                    resultado = numero_a**numero_b

                for _ in range(3):
                    lista.pop(i - 1)

                lista.insert(i - 1, resultado)

                break

    return lista


def multiplicacion(lista: list):

    while "*" in lista or "/" in lista:

        for i in range(len(lista)):
            operador = lista[i]

            if operador == "*" or operador == "/":
                numero_a = lista[i - 1]
                numero_b = lista[i + 1]

                if operador == "*":
                    resultado = numero_a * numero_b
                else:
                    resultado = numero_a / numero_b

                for _ in range(3):
                    lista.pop(i - 1)

                lista.insert(i - 1, resultado)

                break

    return lista


def suma(lista: list):

    while "+" in lista or "-" in lista:

        for i in range(len(lista)):
            operador = lista[i]

            if operador == "+" or operador == "-":
                numero_a = lista[i - 1]
                numero_b = lista[i + 1]

                if operador == "+":
                    resultado = numero_a + numero_b
                else:
                    resultado = numero_a - numero_b

                for _ in range(3):
                    lista.pop(i - 1)

                lista.insert(i - 1, resultado)

                break

    return lista


def parentesis(lista: list):
    if "(" not in lista and ")" not in lista:
        lista = potencia(lista)
        lista = multiplicacion(lista)
        lista = suma(lista)
        return lista[0]

    if lista.count("(") != lista.count(")"):
        raise ValueError

    for i in range(len(lista)):
        if lista[i] == ")":
            cierre = i
            break

    for i in range(cierre, -1, -1):
        if lista[i] == "(":
            apertura = i
            break

    expresion = lista[apertura + 1 : cierre]

    resultado = potencia(expresion)
    resultado = multiplicacion(resultado)
    resultado = suma(resultado)[0]

    for _ in range(cierre - apertura + 1):
        lista.pop(apertura)

    lista.insert(apertura, resultado)

    return parentesis(lista)
