
class Circle():
	def __init__(self, radius):
		self.radius = radius

	def get_area(self):
		return 3.14 * (self.radius ** 2)

	def get_circumference(self):
		return self.radius * 2 * 3.14


radius = float(input("Digite o radius:"))

circle = Circle(radius)

print(f'Área = {circle.get_area():.2f}')
print(f"Circunferência = {circle.get_circumference():.2f}")

		
		