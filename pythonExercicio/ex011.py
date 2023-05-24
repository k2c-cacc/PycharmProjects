largura = float(input('Qual a largura da parede em metros: '))
altura  = float(input('Qual a altura da parede em metros: '))
area = largura * altura
litros = area / 2

print('Para pintar uma parede de {} x {} de área {}m será necessário {} litros de tinta'.format(largura, altura, area, litros))
