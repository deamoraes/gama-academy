print("Amigo oculto")
import random
amigos=input("Digite o nome dos amigos separado por vírgula: ").split(",")
random.shuffle(amigos)


print('Sorteio:')
primeiro = amigos[0]
while len(amigos)>=2:
	print(f'> {amigos[0]} => {amigos[1]}')
	del amigos[0]

print(f'> {amigos[0]} => {primeiro}')

print("**********")







print("*** Bola 8 Mágica ***")
#> Entre com sua pergunta: eu vou aprender Python hoje?
#Resposta aleatória
from random import choice
input("Qual a sua pergunta: ")
print(choice(['não sei','depende de vc','se vc acreditar, tudo pode acontecer', 'parou, vai']))


print('FizzBuzz')
#> Digite o tamanho da lista: 15
#[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
y = int(input("Digite o tamanho da lista:"))
lista = []
for x in range(1,y):
	if x % 3 ==0 and x % 5 ==0:
		lista.append('FizzBuzz')
	elif x%3==0:
		lista.append('Fizz')
	elif x%5==0:
		lista.append('Buzz')
	else:
		lista.append(x)
print(lista)



print("**** Máximo e mínimo ****")
#> Digite os números separados por vírgula: 6,12,8,2,7
#> O maior é 12
#> O menor é 2

lista = input("Digite números separados por vírgula:")
numeros = lista.split(",")

#numeros = [6,12,8,2,7]
#numeros.sort()
#menor = numeros[0]

menor = min(numeros, key=int)

numeros.sort(reverse=True)
maior = numeros[0]

print(f'O maior é {maior}')
print(f'O menor é {menor}')


print("**** Tabuada ****")



number = int(input('Digite um número inteiro:'))


number = int(number)

for x in (range(1,11)):
	resultado = f'{number} * {x} '
	print(f'{resultado[:6]} = ', number * x)




