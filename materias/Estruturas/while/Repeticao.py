while True:
    #if com continue e break:
    numero = int(input("Digite un número _ (0 para sair): "))
    if numero == 0:
        print("Encerrando o programa...")
        break
    if numero == 99:
        print("Número 99 encontrado!!! Continuando para o próximo número...")
        continue
    print(f"Você digitou: {numero}")
    
