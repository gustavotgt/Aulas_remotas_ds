#exercicio 1. verificaçao de idade


Nome = input("Qual é o seu nome? ")


idade_txt = input("Qual é a sua idade? ")


idade_num = int(idade_txt)


if idade_num >= 18:
  
    print(f"Olá, {Nome}, você é maior de idade.")
else:
    
    print(f"Olá, {Nome}, você é menor de idade.")


    #excercicio 2. tabuada

   
numero_str = input("Digite um número para ver a tabuada: ")
numero = int(numero_str)

print(f"--- Tabuada do {numero} ---")

for i in range(1, 11):
    
    
    resultado = numero * i
    
   
    print(f"{numero} x {i} = {resultado}")