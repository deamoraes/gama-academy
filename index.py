

frase = input('Digite uma frase:').split(" ")

#print(frase)
#print(enumerate(frase))

emojis = {
	":)": "🙂",
	":(": "🙁",
	":P": "😜",
	"B)": "😎"
}

for indice, palavra in enumerate(frase):
	frase[indice] = emojis.get(palavra) or palavra
#	if emojis.get(palavra) != None:
#		frase[indice] = emojis[palavra]

print(" ".join(frase))
input(".") 

################################################

knights = {'gallahad': 'the brave', 'robin': 'the pure'}
print(knights.items())
print(list(knights.items()))

print(knights['gallahad'])
input(".")

################################################
conjunto = {1,2,3}
pessoa = {"nome": "Nardini"}
dicionario = {'a': pessoa, 'b':2, 'c':3}

#print(dicionario)
#print(dicionario["a"])
#print(dicionario["b"])

for d in dicionario.values():
	print(d)

print(list(dicionario.values()))

input(".")


################################################
#{} conjuntos / set : sempre é ordenado e sempre é chave, não repete
#() tupla / tuple   : funciona como um enum
#[] lista / list    : array com mais coisas
#conjuntos/set => sempre é ordenado e sempre é chave
status = set(['ativo','desligado'])
numbers = {3,6,3,3,8,2,5,2,2,2}

numbers.add(1)

print(type(status))
print(numbers)

for s in numbers:
	print(s)

n1,n2,n3,n4,n5,n6 = numbers
print(n1)

input(".")
################################################

#tupla são listas que não queremos alterar o valor
friend_list = "joe", "monica"

friend1, friend2 = friend_list
print(friend1)
print(friend2)
input(".")

################################################

friend_list = ["joe","monica","rachel","ross"]
friend_tuple = ("joe","monica","rachel","ross")

#print(type(friend_list))
#print(type(friend_tuple))

friend_list[2] = 'phoebe'

print(friend_list)
print(friend_tuple)

################################################

from random import randint, random, choice
print(randint(10,20))
print(random())
print(choice([1,2,3,4,5]))

print('-----')
for x in range(0,10,2):
	print(x)

print('-----')
for x in "python":
	print(x)


print('-----')
for x in (range(10)):
	print(x)

print('-----')

x = 0
while x<10:
	print(x)
	x += 1
print('-----')	

lista = ['a','b','c']
for x in lista:
	print(x)

langs = ["python", 'js', 'go', 'php']
langs2 = langs.copy() #quando criamos uma variavel = a outra ele cria apenas uma referencia,entao tem que copiar se vc quiser seguir a vida com a nova
langs2.reverse()
numbers = [1,2,3,4,5,6]

print(" - ".join(langs))

langs.append("C")
langs.insert(0,"Java")
#print(len(langs))

langs.sort(reverse=True)
new_langs = sorted(langs, reverse=True)


print(langs.index('js'))
print(new_langs)
print(new_langs.reverse())
new_langs.remove('go')
del langs[1]
print(new_langs)
print(langs.pop())

counter = 0
new_list = []
while counter < len(langs):
	new_list.append(langs[counter])
	new_list.append(numbers[counter])
	counter+=1

#print(new_list)


#print(langs)
#print(langs[0])

#print(langs[1])

#texto = 'abcd'

#print(texto[1:])
#print(texto[:-2])

#numbers = [1,2,3,4,5]
#print(len(numbers))

#print(langs + numbers)
#print([1,2,3] + [4,5,6])

