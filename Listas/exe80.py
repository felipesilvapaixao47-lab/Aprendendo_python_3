#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
for i in range(5):
    numero = int(input("Digite um valor: "))
    if i == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print("Valor adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                print(f"Valor adicionado na posição {pos} da lista...")
                break
            pos += 1
print(f"Os valores digitados, em ordem crescente, são: {numeros}")