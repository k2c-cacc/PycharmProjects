tupla = (int(input("Digite o 1o número: ")),
         int(input("Digite o 2o número: ")),
         int(input("Digite o 3o número: ")),
         int(input("Digite o 4o número: ")))
print(tupla)
#print(tupla.count(9))
print(f'O número 9 apareceu {tupla.count(9)} vez')
if 3 in tupla:
   print(f'Número 3 apareceu na posição: {tupla.index(3) + 1}a')
else:
    print(0)
pares = ''
for c in tupla:
    if c % 2 == 0:
        pares += str(c) + ' '
print(f'Apareceram esses números pares: {pares}')
pares = ''

for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        pares += str(tupla[c]) + ' '
print(f'Apareceram esses números pares: {pares}')




