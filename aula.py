nome = input("Qual é o seu nome? ")

idade_texto = input("Qual é a sua idade? ")

idade = int(idade_texto)

    if idade >= 18:
        print(f"Olá, {nome}, você é maior de idade.")
    else:
        print(f"Olá, {nome}, você é menor de idade.")
dawdawd
22
numero_str = input("Digite um número para ver a tabuada: ")
numero = int(numero_str)

    print(f"\n--- Tabuada do {numero} ---")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")