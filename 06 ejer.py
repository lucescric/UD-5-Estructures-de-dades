def passarAMorse(numero: int) -> str:
    morse_digits = {
        "0": "_____",
        "1": ".___",
        "2": "..__",
        "3": "..._",
        "4": "...._",
        "5": ".....",
        "6": "_....",
        "7": "__...",
        "8": "___..",
        "9": "____.",
    }

    numero_str = str(numero)
    resultat = []

    for d in numero_str:
        resultat.append(morse_digits[d])

    return "".join(resultat)


# Programa principal per provar la funció
if __name__ == "__main__":
    numero = 213
    resultat = passarAMorse(numero)
    print(f"{numero} en Morse és: {resultat}")
