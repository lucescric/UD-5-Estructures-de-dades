import unicodedata
import string


def netejar_text(text):
    # 1. Normalitzar accents
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")

    # 2. Convertir a minúscules
    text = text.lower()

    # 3. Eliminar tot el que no siga lletra o número
    caracters_permesos = string.ascii_lowercase + string.digits
    text_netejat = "".join(c for c in text if c in caracters_permesos)

    return text_netejat


def es_palindrom(text):
    text_netejat = netejar_text(text)
    return text_netejat == text_netejat[::-1], text_netejat


frases = [
    "Anna",
    "Mínim",
    "Atreballar allà, Berta!",
    "A ti no, bonita",
    "Yo hago yoga hoy",
    "Ella te dará detalle",
    "Esto es serio, papá",
]

for f in frases:
    resultat, net = es_palindrom(f)
    print(f"{f} -> {resultat} (neteja: {net})")
