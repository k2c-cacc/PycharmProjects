times = 'Botafogo','Palmeiras', 'Fluminense', 'Atlético-MG', 'Cruzeiro', 'Flamengo', 'Athletico-PR', 'São Paulo', 'Santos', 'Grêmio', 'Fortaleza', 'Red Bull Bragantino', 'Bahia', 'Cuiabá', 'Internacional', 'Goiás', 'Vasco da Gama', 'Corinthians', 'América-MG', 'Coritiba'

print(times)
print(f'Os 5 primeiros colocados {times[0:5]}')
print(f'Os 4 últimos colocados {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
#print(times.index('Santos'))
print('A {} está na posição: {}a'.format('Santos', times.index('Santos') + 1))
# print(times)