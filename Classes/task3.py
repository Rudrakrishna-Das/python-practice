# Task: Create a class Student and another class Course.

# Student attributes: name, roll_number

# Course attributes: course_name, students (a list)

# Course methods:

# add_student(student)

# list_students()

# Practice:

# Create 3 students

# Add them to a course

# List all enrolled students


class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    
class Course:
    def __init__(self, course_name, students=None):
        self.course_name = course_name
        self.students = students if students is not None else []
        
    def add_student(self, student:Student):
        if isinstance(student, Student) and student.name.strip() != "":
            if student not in self.students:
                self.students.append(student)
        else:
            print("Student needs to have a name")
            
    def list_students(self):
        for i in self.students:
            print(f"{i.roll_number} is for {i.name}")
            
            
student1 = Student('Erik', 1)
student2 = Student('Rudra', 2)
student3 = Student('Mark', 3)

course1 = Course('Chem', [student3])
course1.add_student(student1)
course1.add_student(student2)
course1.students.sort(key=lambda student: student.roll_number)

course1.list_students()