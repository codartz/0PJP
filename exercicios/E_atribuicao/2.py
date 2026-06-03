Solicite ao usuário que informe um orçamento (float) e um gasto (float). 
Utilize atribuição -= para descontar o gasto do orçamento.  

# Solicite ao usuário que informe o orçamento e o gasto
orcamento = float(input("Informe o orçamento: "))
gasto = float(input("Informe o gasto: "))

# Imprima o resultado na tela
orcamento -= gasto
print(f"Orçamento restante: {orcamento:.2f}")