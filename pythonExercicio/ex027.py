n = str(input('Digite seu nome: ')).strip()

nome = n.split()
print(nome)
print(nome[0])
print(nome[len(nome) - 1])
# print(nome.find(' '))
# print(nome.rfind(' '))

# Solução k2c
'''primeiro = nome[0: nome.find(' ')]
ultimo = nome[nome.rfind(' ') + 1:]
print(nome.rfind(' ') + 1)
print(len(nome) - nome.rfind(' ') - 1)
print(primeiro)
print(ultimo)'''


# Carlos Augusto Cavalcante Correia
