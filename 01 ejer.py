def mostrar_menu():
    print("\n--- MENÚ D'OPERACIONS AMB STRINGS ---")
    print("1. Longitud d'una cadena")
    print("2. Comparar alfabèticament dos cadenes")
    print("3. Concatenació de dos cadenes")
    print("4. Obtindre subcadena")
    print("5. Invertir cadena")
    print("9. Eixir")
    print("-------------------------------------")


while True:
    mostrar_menu()
    opcio = input("Introdueix una opció: ")

    if opcio == "1":
        cadena = input("Introdueix una cadena: ")
        print("La longitud és:", len(cadena))

    elif opcio == "2":
        cad1 = input("Introdueix la primera cadena: ")
        cad2 = input("Introdueix la segona cadena: ")

        if cad1 > cad2:
            print("La cadena major alfabèticament és:", cad1)
        elif cad2 > cad1:
            print("La cadena major alfabèticament és:", cad2)
        else:
            print("Les dues cadenes són iguals.")

    elif opcio == "3":
        cad1 = input("Introdueix la primera cadena: ")
        cad2 = input("Introdueix la segona cadena: ")
        print("Resultat de la concatenació:", cad1 + cad2)

    elif opcio == "4":
        cadena = input("Introdueix una cadena: ")
        inici = int(input("Introdueix la posició inicial: "))
        fi = int(input("Introdueix la posició final: "))
        print("La subcadena és:", cadena[inici:fi])

    elif opcio == "5":
        cadena = input("Introdueix una cadena: ")
        print("Cadena invertida:", cadena[::-1])

    elif opcio == "9":
        print("Gràcies per utilitzar el programa. Fins prompte!")
        break

    else:
        print("Opció no vàlida. Torna-ho a intentar.")
