from time import sleep


def texto(texto: str, velocidad: float):
    for letra in texto:
        print(letra, end="", flush=True)
        sleep(velocidad)
