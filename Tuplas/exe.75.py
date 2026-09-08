numero = (int(input("Digite um número: ")) for c in range(0, 5))
print(f"Números digitados: {numero}")
print(f"O numero 9 apareceu {numero.count(9)} vezes.")
if 3 in numero:
    print(f"O número 3 apareceu na {numero.index(3)+1}ª posição.")
else:
    print("O número 3 não foi digitado.")
print("Números pares digitados: ", end="")
for n in numero:
    if n % 2 == 0:
        print(n, end=" ")