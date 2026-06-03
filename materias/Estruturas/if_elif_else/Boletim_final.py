# Adicionar ou alterar notas

Nota = 5
# = 0 a 3 Reprovado
# = 3 a 7 Recuperação
# = 7 a 10 Aprovado

# Solicite ao usuario que informe o valor da nota
nota  = float(input("Informe sua nota: "))

# If/Else
if nota >= 0 and nota < 3:
    print("Reprovado :(")

elif nota >= 3 and nota <= 7:
    print("Recuperação :|")

elif nota > 7 and nota <= 10:
    print("Aprovado! :D")

else:
    print("Nota inválida")


