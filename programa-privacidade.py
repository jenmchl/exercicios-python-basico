
lista_censurada = []
adicionar = 'sim'

while adicionar == 'sim':
    palavra_bloqueada = input('Digite a palavra a ser bloqueada: ')
    lista_censurada.append(palavra_bloqueada)

    adicionar = input('Deseja adicionar mais uma palavra? ')

texto = input('Digite o texto que deseja analisar: ')

censurado = False
for item in lista_censurada:
    if item in texto:
        censurado = True
        break

if censurado :
    print('#### CENSURADO ####')
else:
    print(texto)
