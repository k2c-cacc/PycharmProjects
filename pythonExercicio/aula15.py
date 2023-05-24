n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma é: %d ' %(s)) # a partir até python 2
print('A soma é: {}'.format(s)) # a partir do python 3
print(f'A soma é: {s}') # a partir do python 3.6+