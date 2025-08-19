print("### Tabuada ###")
while True:
    try:
        num = int(input("Digite um número (ou digite 0 para sair): "))
        if num == 0:
            print("saindo do programa...")
            break
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
        