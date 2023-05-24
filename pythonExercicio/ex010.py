real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27

print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
print('Você tem equivalente a {:.2f} dolares'.format(dolar))
