print(" <<< Exercícío com Try/Except >>> ")

soma = 0 # Variável para armazenar a soma dos números
while True: # Faz um loop infinito até que o usuário decida sair
    try: # Trata o erro ValueError caso o usuário digite algo que não seja um número
        for i in range(2): # Loop para solicitar dois números
            num = int(input(f"Digite o número {i+1}: "))
            soma += num # Acumula a soma dos números digitados
        print(f"\033[32mA soma dos números é: {soma}\033[m")
        continua = input("Deseja continuar? (s/n): ").strip().lower() # Solicita ao usuário se deseja continuar
        if continua != 's':
            print("Programa encerrado.")
            break # Se o usuário não quiser continuar, encerra o loop
    except ValueError: # Trata o erro caso o usuário digite algo que não seja um número
        print("\033[31mO número digitado é inválido. Digite apenas número inteiros.\33[m")