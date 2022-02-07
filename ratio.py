print('------ Vamos comparar a relação das bicicletas! ------')

nome = input('Digite seu nome: ')
coroa = int(input('Quantos dentes tem sua coroa? '))
pinhao = int(input('Quantos dentes tem seu pinhão? '))

nome2 = input('Digite o nome da pessoa a ser comparada: ')
coroa2 = int(input('Quantos dentes tem na coroa dela? '))
pinhao2 = int(input('Quantos dentes tem no pinhão dela? '))

relacao = coroa / pinhao
relacao2 = coroa2 / pinhao2

if relacao > relacao2:
    print ('A relação de', nome,
           'é mais pesada que a de', nome2)

elif relacao < relacao2:
   print ('A relação de', nome2,
          'é mais pesada que a de', nome)

else:
    print ('A relação de', nome,
           'é igual a de', nome2)
