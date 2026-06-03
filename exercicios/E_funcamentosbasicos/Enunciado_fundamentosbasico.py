1. # Peça ao usuário seu nome e cumprimente utilizando a função print(), ex.: "Olá, Carol!" nome = input("Digite seu nome ") print("Olá, " + nome + "!")

# Lê o nome digitado pelo usuário
nome = input("Digite seu nome: ")

# Exibe uma saudação com o nome informado
print("Olá,", nome + "!")

2. # Peça ao usuário sua idade e exiba na tela: "Você tem {idade} anos!"
idade = input("Digite sua idade ")  
print("Você tem " + idade + " anos!")

# Lê a idade digitada pelo usuário
idade = input("Digite sua idade: ")

# Exibe a frase com a idade informada
print("Você tem", idade, "anos!")

3. # Lê o nome digitado pelo usuário
nome = input("Digite o nome: ")

# Exibe uma saudação com o nome informado (com dois nomes)
print("Olá, bem-vindo!", nome)

4. # Crie um programa que receba um número do usuário e exiba o valor multiplicado por 2.

num = int(input("Digite um número: "))
resultado = num * 2
print(f"O número {num} multiplicado por 2 é {resultado}")

5. # Crie um programa que solicite ao usuário que digite dois números e exiba a soma deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}")

6. # Crie um programa que receba uma frase do usuário e exiba quantos caracteres tem.

frase = input("Digite uma frase: ")
print(f"A frase tem {len(frase)} caracteres")

7. # Crie um programa que receba dois números e exiba o resultado da multiplicação entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
mult = num1 * num2
print(f"A multiplicação de {num1} e {num2} é {mult}")

8. # Crie um programa que converta uma temperatura de Celsius para Fahrenheit. A fórmula é: F = (C × 9/5) + 32

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")