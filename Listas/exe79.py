#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = []
while True:
    numero = int(input("Digite um valor: "))
    if numero not in numeros:
        numeros.append(numero)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não será adicionado...")
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
numeros.sort()
print(f"Os valores digitados, em ordem crescente, são: {numeros}")