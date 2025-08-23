def coletar_numero():
    numeros = []
    print("Digite números (digite 0 para sair):")
    
    while True:
        try:
            n = int(input("Número: "))
            if n == 0:
                print("Programa encerrado.")
                break
            if n not in numeros:
                numeros.append(n)
                print(f"Lista atual {numeros}")
            else:
                print(f" {n} já na lista, ignorado.")
        except ValueError:
            print("Digite um número válido.")    
resultado = coletar_numero()
print(f"O resultado é {resultado}")