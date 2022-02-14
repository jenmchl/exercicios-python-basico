# Escreva uma função que recebe um objeto de coleção,
# e retorna o maior numero dentro dessa coleção.
# Faça outra função que retorna o menor numero dessa coleção.


def maior(x,y,z):
    max = x

    if y > max:
        max = y
    if z > max:
        max = z

    return max

def menor(x,y,z):
    min = x

    if y < min:
        min = y
    if z < min:
        min = z

    return min

def menu():
    x = int(input('Primeiro número: '))
    y = int(input('Segundo número : '))
    z = int(input('Terceiro número: '))

    print("O maior número é: ", maior(x,y,z))
    print("O menor número é: ", menor(x,y,z))
    print()


print(menu())
