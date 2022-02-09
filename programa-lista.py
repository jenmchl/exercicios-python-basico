
lista_convidados = []

adicionar = 'sim'

while adicionar == 'sim':
    nome = input('Nome convidado: ')
    lista_convidados.append(nome)

    adicionar = input('Deseja adicionar mais um convidado? ')

lista_convidados.sort()

print('Os convidados são:')
for convidado in lista_convidados:
    print(convidado)
