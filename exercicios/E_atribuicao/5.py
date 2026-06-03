Solicite ao usuário que informe uma quantidade de horas e converta para dias utilizando /= 24.  

# Solicite ao usuário que informe uma quantidade de horas
número = float(input("Digite as horas: "))

# Calcule
número /= 24  # Saída: 15.0

# Imprima o resultado na tela
print(f"Convertido para dias e horas restantes: {número:.1f}")