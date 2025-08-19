print("### Tabuada ###") 
while True:
    try: #Trato o erro ValueError caso o usuário digite algo que não seja um número
        num = int(input("Digite um número (ou digite 0 para sair): "))
        if num == 0:
            print("saindo do programa...")
            break
    except ValueError: #Junto ao try trato o erro em caso o usuário digite algo que não seja o número
        print("Por favor, digite um número válido.")
        continue
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
        