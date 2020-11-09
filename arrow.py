total=int(input("Digite o total: "))

for row in range(1,total+1):
	print("* " * row)

for row in range(total-1, 0, -1):
	print("* " * row)	

