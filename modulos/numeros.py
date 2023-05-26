from uteis import numeros

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro do número {num} é {numeros.dobro(num)}')
print(f'O triplo do número {num} é {numeros.triplo(num)}')

