# Peça para o aluno digitar a idade de uma pessoa e o programa deve classificar:

# 0–12 → Criança
# 13–17 → Adolescente
# 18–59 → Adulto
# 60+ → Idoso

# Solicite ao usuario que informe sua idade
idade = int(input("Informe sua idade: "))

# If/Else
if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")


