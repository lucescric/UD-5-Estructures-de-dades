def imprimir_caixa(text):
    amplada = len(text) + 4  # 2 espais + 2 asteriscs
    print("*" * amplada)
    print(f"* {text} *")
    print("*" * amplada)


imprimir_caixa("¡Cuidado! Python suelta")
imprimir_caixa("while True: learn Python")
