amount = int(input("Digite o valor do saque: "))

bank_notes = {
	"0": 200,
	"1": 100,
	"2": 50,
	"3": 20,
	"4": 10,
	"5": 5
}

remainder = amount
withdrawal = []
for i,bank_note in enumerate(bank_notes):	
	while remainder >= bank_notes.get(bank_note):
		withdrawal.append(bank_notes.get(bank_note))
		remainder -= bank_notes.get(bank_note)
		
print(f'Notas:{withdrawal}')

if remainder > 0:
	print("Valor inválido, diferença de R$ ",remainder)


