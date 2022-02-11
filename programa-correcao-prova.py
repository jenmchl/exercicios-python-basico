
lista_aprovados  = []
lista_reprovados = []

aluno = {}
sala  = {}
nota  = {}

adicionar = 'sim'

while adicionar == 'sim':
    aluno = input('Digite o nome do aluno: ')
    sala  = input('Digite o número ou letra da sala: ')
    nota  = int(input('Digite a nota: '))

    if  nota >= 50:
        lista_aprovados.extend([aluno, sala, nota])
    else:
        nota < 50
        lista_reprovados.extend([aluno, sala, nota])

    adicionar = input('Deseja adicionar mais uma nota? ')

print('Os alunos aprovados são:')
for aprovado in lista_aprovados:
    print(aprovado)

print('Os alunos reprovados são:')
for reprovado in lista_reprovados:
    print(reprovado)
