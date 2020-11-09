amount = int(input("Digite o valor do saque: "))

bank_notes = [200,100,50,20,10,5]

remainder = amount
withdrawal = []
for bank_note in bank_notes:	
	while remainder >= bank_note:
		withdrawal.append(bank_note)
		remainder -= bank_note

if remainder > 0:
	print(f"Valor inválido, diferença de R$ {remainder:.2f}")
else:
	print(f'Notas:{withdrawal}')

