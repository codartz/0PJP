# Exercício 1: Praticando Listas
# 1. Crie uma lista tarefas com 3 tarefas que você faz no dia a dia.
# 2. Adicione mais 2 tarefas usando append().
# 3. Remova 1 tarefa (use remove ou pop).
# 4. Imprima a lista toda com print().
# 5. Imprima só as 2 primeiras tarefas (usando fatiamento).

compras = []

for i in range(3):
    item = input(f"Digite o item {i + 1}: ")
    compras.append(item)

def mostrar(lista):
    for item in lista:
        print(f" comprar: {item}")

mostrar(compras)

chocolate = any(item.lower() == "chocolate" for item in compras)
print(f"Tem chocolate na lista? {chocolate}")

