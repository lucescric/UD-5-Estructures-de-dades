email = input("Introdueix un email: ")

# 1. ERROR1: Ha de contindre '@'
if "@" not in email:
    print("ERROR1: L’email deu contindre una '@'.")
    exit()

# Separem en dues parts
pos_arroba = email.find("@")
ident1 = email[:pos_arroba]
rest = email[pos_arroba + 1 :]

# 2. ERROR2: Abans de '@' ha d'haver identificador1
if ident1 == "":
    print(
        "ERROR2: Abans de l @ ha d'haver un identificador1, un email no pot començar amb '@'."
    )
    exit()

# 3. ERROR3: identificador1 mínim 4 caràcters
if len(ident1) < 4:
    print("ERROR3: El identificador1 ha de tindre una longitud mínima de 4 caràcters.")
    exit()

# 4. ERROR4: Després de '@' ha d'haver un punt en algun moment
if "." not in rest:
    print("ERROR4: Darrere de l @ ha d'haver un punt.")
    exit()

# Separem identificador2 i domini
pos_punt = rest.find(".")
ident2 = rest[:pos_punt]
domini = rest[pos_punt:]

# 5. ERROR5: identificador2 mínim 3 caràcters
if len(ident2) < 3:
    print(
        "ERROR5: Abans del punt ha d'haver un identificador2 amb una longitud mínima de 3 caràcters."
    )
    exit()

# 6. ERROR6: Domini final vàlid
dominis_valids = [".com", ".es", ".org", ".gov"]
if domini not in dominis_valids:
    print(
        "ERROR6: Al final de l’email ha d'haver un domini vàlid (.com, .es, .org, .gov)."
    )
    exit()

# Si tot és correcte
print("Enhorabona, email correcte!")
