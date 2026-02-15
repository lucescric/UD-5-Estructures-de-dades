def validar_contrasenya(pwd: str) -> list:
    errors = []

    # Restriccions
    especials = "!+-*$%()"

    # 1. Mida mínima
    if len(pwd) < 8:
        errors.append("La contrasenya ha de tindre almenys 8 caràcters.")

    # 2. Majúscules
    maj = sum(1 for c in pwd if c.isupper())
    if maj < 2:
        errors.append("La contrasenya ha de contindre almenys 2 lletres majúscules.")

    # 3. Minúscules
    minusc = sum(1 for c in pwd if c.islower())
    if minusc < 3:
        errors.append("La contrasenya ha de contindre almenys 3 lletres minúscules.")

    # 4. Dígits
    digits = sum(1 for c in pwd if c.isdigit())
    if digits < 1:
        errors.append("La contrasenya ha de contindre almenys un dígit.")

    # 5. Caràcters especials
    if not any(c in especials for c in pwd):
        errors.append(
            "La contrasenya ha de contindre almenys un dels caràcters especials: !+-*$%()"
        )

    # 6. No pot contindre '@'
    if "@" in pwd:
        errors.append("La contrasenya no pot contindre el caràcter '@'.")

    return errors


# Programa principal
if __name__ == "__main__":
    while True:
        contrasenya = input("Introdueix una contrasenya: ")
        errors = validar_contrasenya(contrasenya)

        if not errors:
            print("Contrasenya vàlida!")
            break
        else:
            print("\nLa contrasenya no és vàlida. Errors trobats:")
            for e in errors:
                print(" -", e)
            print()  # línia en blanc per a llegibilitat
