# Leia um número qualquer
# Mostre o seu fatorial
n = int(input('Digite um número :'))
resp = 1
for c in range(1, n + 1, 1):
    resp = resp * c
print(resp)
