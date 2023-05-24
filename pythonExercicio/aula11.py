# Utilizando cores

"""print('\33[1;31;43mOlá Mundo!')
print('\33[1;31;43mOlá Mundo!\33[m')

a = 3
b = 5
print('Os valores são \33[32m{}\33[m e \33[31m{}\33[m!!!'.format(a, b))

nome = 'Carlos'
print('Olá! {}{}{}!'.format('\33[4;34m', nome, '\33[m'))"""

nome = 'Carlos'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretobranco': '\033[7;40m'}
print('Olá! {}{}{}!'.format(cores['pretobranco'], nome, cores['limpa']))
