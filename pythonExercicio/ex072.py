extenso = ( 'Zero',
          'Um', 'Dois', 'Tres', 'Quatro',
          'Cinco', 'Seis', 'Sete', 'Oito',
          'Nove', 'Dez', 'Onze', 'Doze',
          'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
          'Dezessete', 'Dezoito', 'Dezenove', 'Vinte' )

while True:
    num = int(input('Digite um número entre 0 a 20: '))

    if num < 0 or num > 20:
        print('Número inválido!')
    else:
        print(extenso[num])
#print(extenso)