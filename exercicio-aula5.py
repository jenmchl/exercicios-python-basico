
# Exercicio: Faça um programa que leia a quantidade de pessoas que
# serao convidadas para uma festa.
# Após isso o programa ira perguntar o nome de todas as pessoas e colocar numa
# lista de convidados
# Após isso ira imprimir todos os nomes da lista


lista_convidados = ['Jean', 'Bárbara', 'Adriane', 'Gustavo', 'Ana', 'Giovane',
                    'Samanta', 'Janete', 'Mayara', 'Murilo', 'Vitória', 'Angela', 'Márcio']
lista_convidados.sort()

print(len(lista_convidados),'pessoas estão convidadas para a festa!')

print('Os convidados são:')
for i in range(len(lista_convidados)):
    print(lista_convidados[i])
