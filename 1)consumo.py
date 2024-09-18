dp = float(input('\n\nQual a distância percorrida em Km?: '))
total = float(input('Qual o total gasto em combustível (em R$)?: '))

litro = 4.50

consumo = dp/(total/litro)

print(f'O Consumo Médio é de {consumo:.2f} Km/litro')
