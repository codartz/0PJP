Solicite ao usuário que informe os tempos em segundos (int). 
Converta para minutos inteiros com //= e depois use %= para obter segundos restantes.  

# Solicite ao usuário que informe os segundos
número = float(input("Digite os segundos: "))

# Calcule
número //= 60  # Saída: 15.0
segundos_restantes = número % 60

# Imprima o resultado na tela
print(f"Convertido para minutos: {número:.0f}")
print(f"Segundos restantes: {segundos_restantes:.1f}")