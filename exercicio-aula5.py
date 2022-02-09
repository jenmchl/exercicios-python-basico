
# Exercicio: Faça um programa que leia a quantidade de pessoas que
# serao convidadas para uma festa.
# Após isso o programa ira perguntar o nome de todas as pessoas e colocar numa
# lista de convidados
# Após isso ira imprimir todos os nomes da lista

numero_convidados = int(input('Qual o número de convidados?  '))

lista_convidados = []

i = 0

while i < numero_convidados:
    nome = input('Nome convidado: ')
    lista_convidados.append(nome)
    i += 1

lista_convidados.sort()

print('Os convidados são:')
for convidado in lista_convidados:
    print(convidado)
