class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
students1 = [
    Student("Siva", "S101", 6.8),
    Student("Dinesh", "D102", 5.6),
    Student("Gobi", "G103", 4.4),
    Student("Bharathi", "B104", 3.3),
]

sorted_students1 = sort_students(students1)

print("Sorted List 1:")
for student in sorted_students1:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")