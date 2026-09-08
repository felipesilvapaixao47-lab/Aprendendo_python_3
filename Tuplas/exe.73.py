times = ("Corinthians", "Palmeiras", "Santos", "Flamengo", "Grêmio", "Cruzeiro", "Vasco", "Atlético-MG","Botafogo", "Internacional", "São Paulo", "Bahia", "Sport", "Fluminense", "Atlético-PR", "Coritiba", "Vitória", "Chapecoense", "Avaí", "Ceará")

print("Os 5 primeiros times são:")
for t in range(5):
    print(f"{t+1}. {times[t]}")

print("\nOs 4 últimos colocados são:")
for t in range(-4, 0):
    print(f"{len(times)+t+1}. {times[t]}")

print("\nTimes em ordem alfabética:")
for t in sorted(times):
    print(t)
    
print(f"\nO time Chapecoense está na {times.index('Chapecoense')+1}ª posição.")