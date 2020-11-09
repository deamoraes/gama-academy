#number=int(input("Digite o number: "))

#line = ""
#for row in range(1,number+1):
#	for col in range(1,row+1):
#		line += str(col) + " "
#	print(line)
#	line = ""  
#

number=int(input("Digite o number: "))

line=""
for x in range(1,number+1):
    line+=str(x)+" "
    print(line)

print()

for row in range(number, 0, -1):
    for column in range(row, 0, -1):
        print(column, end=" ")
    print()
    


