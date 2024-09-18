dp = int(input('\nDigite a quantidade de Km percorrido: '))
dias = int(input('Digite a quantidade de dias que você ficou com o carro alugado: '))

tp = dias*60
consumo = 0.15*dp

print('O valor totl do aluguel foi de:R$',tp)
print('O consumo total foi de: ',consumo,'L')