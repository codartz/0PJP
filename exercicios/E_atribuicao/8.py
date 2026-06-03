Solicite um número (int), aplique n %= 2 e exiba o valor na tela. Se o resultado for 0, o número é par; se o resultado for 1, o número é ímpar.  

# Solicite ao usuário que informe número
número = float(input("Digite um valor: "))

# Calcule
número %= 2  # Saída: 15.0

# Imprima o resultado na tela
print(f"O número é {'par' if número == 0 else 'ímpar'}")
