lista = []
frutas = ["maça", "banana", "uva"]
numeros = [1, 2, 3, 4]

# Acessanco elementos
print("Primeira fruta:", frutas[0])  # "maça"
print("Ultima fruta:", frutas[-1])   # "uva"

# Alterando elementos
frutas[1] = "banana-nanica"
print("Após alterar:", frutas)

# Adicionando elementos
frutas.append("morango")             # adiciona no final
frutas.insert(1, "pera")             # adiciona na posição 1
print("Após adicionar:", frutas)

# Removendo elementos
frutas.remove("uva")                 # remove pelo valor
última = frutas.pop()                # remove e retorna o ultimo
print("Após remover 'uva' e pop():", frutas, "Última removida:", última)

# Tamanho (quantidade de elementos)
print("Quantidade de frutas:", len(frutas))

# Fatiamento (slicing)
print("Fatiamento [0:2]:", frutas[0:2])

# Verificar se um item está na lista
print("Tem 'maça'?", "maça" in frutas)

# Outras operações uteis
print("Lista original 'numeros': ", numeros)
print("Soma dos numeros:", sum(numeros))
print("Maior numero:", max(numeros))
print("Menor numero:", min(numeros))
numeros.reverse()
print("Reversa:", numeros)
numeros.short()
print("Ordenada crescente:", numeros)
numeros.sort(reverse=True)
print("Ordenada decrescente:", numeros)

# Iterar sobre a lista
for fruta in frutas:
    print("Fruta:", fruta)

# List comprehension (exemplo simples)
quadrados = [n * n for n in [1, 2, 3, 4, 5,]]
print("Quadrados:", quadrados)

