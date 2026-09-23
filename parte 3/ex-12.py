soma = 0
while True:
    num = float(input("Digite um número (ou 0 para sair): "))
    if num == 0.0:
        break
    soma += num
    
    # Apresenta a soma sem casas decimais se for inteiro
if soma.is_integer():
    print(f"Soma: {int(soma)}")
else:
    print(f"Soma: {soma}")
print(f"A soma dos números digitados é: {soma}")