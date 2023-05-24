num = int(input('Informe um número: '))
'''str = '0000' + str(num)
print(str)
str = str[4:-1]
print(str)'''
print('Unidade: {}'.format(num // 1 % 10))
print('Dezena:  {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar:  {}'.format(num // 1000 % 10))