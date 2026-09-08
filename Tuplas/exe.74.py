from random import randint
numero = ( randint(1, 100), randint(1, 100), randint(1, 100),
           randint(1, 100), randint(1, 100) )
print(f"Números sorteados: {numero}")
print(f"O maior número sorteado foi {max(numero)}.")
print(f"O menor número sorteado foi {min(numero)}.")