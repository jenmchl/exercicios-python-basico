# EXERCICIO: Faça um programa que pergunte a idade, o peso, e a altura
# de uma pessoa e decide se ela esta apta a ser do exercito. Para entrar
# exercito é preciso ter mais de 18 anos, pesar mais ou igual a 60 kilos,
# e medir mais ou igual que 1,70 metros.

print('------ ALISTE-SE JÁ ------')

nome = input('Nome completo: ')
sexo = input('Sexo: ').lower().replace('masculino','m')
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: ').replace(',','.'))

if sexo == 'm' and idade >= 18 and peso >= 60 and  altura >= 1.70:
    print('Você já pode se alistar!')
else:
    print('Você não está apto para alistar-se')
