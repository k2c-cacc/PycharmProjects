lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[1]) # Posição física(nominal)
print(lanche[-2]) # Sempre da direita para esquerda quando negativo, neste exemplo vai de -4 até -1
print(lanche[1:3]) # Sempre desconsidera o último endereço
print(lanche[2:]) # Da posição até a última
print(lanche[:2]) # Da primeira até a posição indicada - 1

print(sorted(lanche)) # Continua imutável
print(lanche)

"""# Tuplas são imutáveis
lanche[1] = 'Refrigerante'
print(lanche[1]) # Posição física(nominal)"""

"""for comida in lanche:
    print(f'Vou comer {comida}')"""
# print(len(lanche))
"""for c in range(0, len(lanche)): # O range sempre desconsidera a última posição
    print(f'Vou comer {lanche[c]}')"""

"""for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

print('Comi bastante!')"""