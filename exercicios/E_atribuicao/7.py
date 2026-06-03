Solicite ao usuário que informe uma quantidade de segundos e depois transforme em minutos inteiros utilizando //=60. 

# Solicite ao usuário que informe segundos
número = float(input("Digite os segundos: "))

# Calcule
número //= 60  # Saída: 15.0

# Imprima o resultado na tela
print(f"Convertido para minutos: {número:.0f}")