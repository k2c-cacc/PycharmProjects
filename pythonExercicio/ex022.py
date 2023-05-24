nome = input('Digite um nome completo: ').strip() # Tira espaços antes/depois

print('Analisando o nome ...')
print('O nome em maiúsculas é {}'.format(nome.upper()))
print('O nome em minúsculas é {}'.format(nome.lower()))
print('O nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome é {}'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('O primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
