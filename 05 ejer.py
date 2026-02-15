def passarAParaules(numero: int) -> str:
    digits_a_paraules = {
        "0": "zero",
        "1": "un",
        "2": "dos",
        "3": "tres",
        "4": "quatre",
        "5": "cinc",
        "6": "sis",
        "7": "set",
        "8": "vuit",
        "9": "nou",
    }

    numero_str = str(numero)
    paraules = []

    for d in numero_str:
        paraules.append(digits_a_paraules[d])

    return ",".join(paraules)


# Programa principal per provar la funció
if __name__ == "__main__":
    numero = 470213
    resultat = passarAParaules(numero)
    print(f"{numero} → {resultat}")
