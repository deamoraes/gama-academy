def get_student_notes():
	notes= []
	for i in range(1,5):
		notes.append(float(input(f"Digite a {i}ª nota: "))) 
	return notes


def show_curriculum_result(notes):
	avg = sum(notes)/len(notes)
	return avg


notes = get_student_notes()
print("A média é: ", round(show_curriculum_result(notes),2))