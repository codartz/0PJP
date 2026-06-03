# O aluno digita uma nota de 0 a 10. O programa retorna:

# ≥ 9 → Excelente
# ≥ 7 → Bom
# ≥ 5 → Regular
# < 5 → Reprovado

# Solicite ao usuario que informe sua nota
nota = float(input("Informe sua nota: "))
# If/Else
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Nota inválida")
