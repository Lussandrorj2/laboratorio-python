
numeros = []

while True:

    for i in range(2):
        num = int(input(f"Digite o {i}º número: "))
        numeros.append(num)
    operacao = input("Digite a operação: ")
    
    match operacao:
        case "+":
            res = numeros[0] + numeros[1]
        case "-":
            res = numeros[0] - numeros[1]
        case "*":
            res = numeros[0] * numeros[1]
        case "/":
            if numeros[1] != 0:
                res = numeros[0] / numeros[1]
            else:
                print("Erro: Divisão por zero.")
        
            
    print(f"Resultado → {res}") 
    
    c = input("Continuar(s/n): ").lower()
    if c != "s":
        break
print("Programa encerrado...")