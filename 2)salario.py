salario = float(input('\nInforme seu salário: '))
aumento = float(input('Informe o aumento do salário em porcentagem (%): '))

novo = salario+salario*aumento/100
qtd_aumentada = salario*aumento/100

print('Houve um aumento de: R$',qtd_aumentada)
print('O seu novo salário é:R$',novo)