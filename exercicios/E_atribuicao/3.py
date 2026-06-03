Solicite ao usuário que informe o estoque no início do dia (int) e a quantidade vendida ao final do dia (int). 
Atualize a quantidade utilizando atribuição -= para mostrar o estoque final.  

# Solicite ao usuário que informe o estoque no início do dia e a quantidade vendida ao final do dia.
estoque_inicial = int(input("Informe o estoque no início do dia: "))
quantidade_vendida = int(input("Informe  vendida ao final do dia: "))

# Atualize a quantidade utilizando atribuição -=
estoque_final = estoque_inicial - quantidade_vendida

# Imprima o resultado na tela
print(f"Estoque final: {estoque_final}")