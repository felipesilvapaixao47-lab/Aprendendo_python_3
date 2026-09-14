#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.
mumeros = []
while True:
    numero = int(input("Digite um valor: "))
    mumeros.append(numero)
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(f"Você digitou {len(mumeros)} números.")
mumeros.sort(reverse=True)
print(f"Os valores digitados, em ordem decrescente, são: {mumeros}")
if 5 in mumeros:
    print("O valor 5 está na lista.")
    print(f"O valor 5 aparece {mumeros.count(5)} vez(es).")
else:
    print("O valor 5 não está na lista.")