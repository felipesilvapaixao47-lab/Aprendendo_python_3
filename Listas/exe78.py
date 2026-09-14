#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = [ ]
min = 0
max = 0
for i in range(5):
    numero = int(input(f"Digite um valor para a posição {i}: "))
    numeros.append(numero)
    if i == 0:
        min = numero
        max = numero
    else:
        if numero < min:
            min = numero
        if numero > max:
            max = numero
print("-="*30)
print(f"Os números digitados foram: {numeros}")
print(f"O maior número é: {max}, que está na posição: {numeros.index(max)}")
if numeros.count(max) > 1:
    print(f"O maior número aparece {numeros.count(max)} vezes.")
print(f"O menor número é: {min}, que está na posição: {numeros.index(min)}")
if numeros.count(min) > 1:
    print(f"O menor número aparece {numeros.count(min)} vezes.")