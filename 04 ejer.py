def passarAPalotes(numero: int) -> str:
    digits = str(numero)
    resultat = []

    for d in digits:
        valor = int(d)
        palotes = "|" * valor
        resultat.append(palotes)

    return "-".join(resultat)


# Programa principal per provar la funció
if __name__ == "__main__":
    numero = 470213
    print(f"{numero} en palotes és: {passarAPalotes(numero)}")
