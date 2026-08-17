from time import sleep


def typewriter(text: str, delay: float):
    for character in text:
        print(character, end="", flush=True)
        sleep(delay)
