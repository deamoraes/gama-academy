
class VirtualPet:
	
	def __init__(self):
		self.status = "acordado"
		
	def comer(self):
		food = input("Comida: ")
		print(f"Comendo {food}...")

	def dormir(self):
		if self.status == "acordado":
			print("Dormindo...")
			self.status = "dormindo"
			return
		print("Acordei :)")
		self.status="acordado"

	def acordar(self):
		if self.status == "acordado":
			print("Já estou acordado")
			return
		print("Acordei :)")
		self.status="acordado"


my_pet = VirtualPet()		
option = ""

while option != "s":
	option = input("(C)omer (A)cordar (D)ormir ou (S)air: ").lower()

	if option == "c":
		my_pet.comer()
	elif option == "a":
		my_pet.acordar()
	elif option == "d":
		my_pet.dormir()


