
numbers = []

while True:
    resposta = input("Digite um numero (ou escreva 'Sair'): ")
    if (resposta.lower() == "sair"):
        break

    number = int(resposta)
    numbers.append(number)


numbers.sort()

print("O menor número da lista é o ", numbers[0])
print("O maior número da lista é o ", numbers[-1])
