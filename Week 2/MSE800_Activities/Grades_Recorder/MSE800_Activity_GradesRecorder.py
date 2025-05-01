class StudentIdentity:
	def __init__(self, student_name, student_number, class_number):
		self.student_name = student_name
		self.student_number = student_number
		self.class_number = class_number

	def __repr__(self):
		return f"Student Name: {self.student_name}\nStudent Number: {self.student_number}\nClass Number: {self.class_number}"

class RecordGrades: 
    def __init__(self, grade_a, grade_b, grade_c):
        self.grade_a = grade_a
        self.grade_b = grade_b
        self.grade_c = grade_c

    def __repr__(self):
        return f"Subject A: {self.grade_a}\nSubject B: {self.grade_b}\nSubject C: {self.grade_c}"

def input_grades():
	grade_a = input("Enter grade for Subject A:")
	grade_b = input("Enter grade for Subject B:")
	grade_c = input("Enter grade for Subject C:")
	return RecordGrades(grade_a, grade_b, grade_c)

all_students = [
	StudentIdentity("Mark", 11001, "11-01"),
	StudentIdentity("Angel", 11002, "11-01"),
	StudentIdentity("Geraldine", 11003, "11-01")
]

grades_sheet = {}
for student in all_students:
	print(f"Enter grades for {student.student_name}:")
	grades_sheet[student.student_name] = input_grades()

for student in all_students:
	print(f"\n{student}\nGrades:\n{grades_sheet[student.student_name]}\n")