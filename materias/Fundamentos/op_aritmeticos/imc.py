# Solicite ao usuario que informe os dados para o cálculo do IMC e classifica-lo de forma simples

nome = input("Nome: ")
idade = input("Idade: ")
cpf = input("CPF: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)    # aritméticos
print(f"IMC de {imc:.2f}")

# comparação + lógicos (faixa simplificada)
baixo_peso = imc < 18.5
normal = (imc >= 18.5) and (imc < 25)
sobrepeso = (imc >= 25) and (imc < 30)
obesidade = imc >= 30

print("Baixo peso?", baixo_peso)
print("Normal?", normal)
print("Sobrepeso?", sobrepeso)
print("Obesidade?", obesidade)