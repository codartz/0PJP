Solicite ao usuário uma distância em metros e depois converta para km inteiros com //= 1000, guarde os metros restantes utilizando %= (utilize outra variável).  

# Solicite ao usuário que informe um distancia em metros
número = float(input("Digite uma dintância: "))

# Converta
número //= 1000  # Saída: 15.0
segundos_restantes = número % 1000

# Imprima o resultado na tela
print(f"Convertido para km: {número:.0f}")


