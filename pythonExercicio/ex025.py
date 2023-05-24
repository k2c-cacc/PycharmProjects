nome = str(input('Nome completo: ')).strip()

print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
print('Seu nome tem Silva? {}'.format(nome.lower().count('silva') > 0))
