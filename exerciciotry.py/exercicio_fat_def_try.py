def fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado
while True:
    try:
        fat = int(input("Digite um número para fatorial: "))
        if fat < 0:
            print("Não é possível calcular fatorial de número negativo.")
        else:
            print(f" O fatorial de {fat} é → {fatorial(fat)}")
    except ValueError:
            print("Por favor, digite um número inteiro valido.")
            continue
    c = input("Deseja continuar?(s/n): ").strip().lower()
    if c not in ["s","n"]:
        print("Por favor, digite somente (s/n).")
        continue
    if c == "n":
        print("Programa encerrado.")
        break