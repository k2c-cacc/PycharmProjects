import random
#num = random.random()
#num = random.randint(1, 50)

numeros = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)

print(numeros)
menor = numeros[0]
maior = numeros[0]
for c in range(0, len(numeros)):
    if numeros[c] < menor:
        menor = numeros[c]
    if numeros[c] > maior:
        maior = numeros[c]

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')
