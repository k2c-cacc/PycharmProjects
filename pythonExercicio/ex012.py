vp = float(input('Informar o valor do produto R$ '))
vcd = vp * (95 / 100) # vcd = vp - (vp * 5 / 100)

print('O produto comprado por {:.2f} ficará com valor final {:.2f}'.format(vp, vcd))
