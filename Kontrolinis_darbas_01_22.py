class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):     # Nera super funkcijos "super().__init__(name, age)"
        super().__init__(name, age)    # Truksta super funkcijos (TASK 1)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self):
        for course in self.enrolled_courses:            # TASK 3
            grade = self.grades.get(course, "N/A")      # Sita papildoma funkcija spauzdins Varda, Kursa, ir Balus
            print(f"Student: {self.name}, Course: {course.name}, Grade: {grade}")

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade   # Sitoje vietoje reikia kintamojo grade

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # Task 4 Cia taip pat turejome prideti super funkcija
        self.subject = subject
        self.courses = []

    def list_courses(self):
        return [course.name for course in self.courses] # Vietoj "None" Padarome kad sarasas griztu

class Lesson:
    def __init__(self, lection, data, information):    # 2 Exercizes
        self.lection = lection                         # Reikia sukurti clase Leason
        self.data = data
        self.information = information

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        self.lessons = []
        teacher.courses.append(self)  # Add this course to the teacher's course list

    def add_lesson(self, lesson):
        self.lessons.append(lesson)      # reikejo prideti dar append fukcija kad pridetu dar viena Lectiona

    def get_lessons(self):                                          # Exercizes 2
        return [lesson.lection for lesson in self.lessons]          # Dar reikejo prideti sita funkcija kuri grazina sarasa su pamokos pavadinimu

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:                               # Task 5
            attendance_record = self.attendance.get(student, [])    # Reikejo pasalinti viena eilute, nes jinai Baggino
            print(f"Mokinys: {student.name}, Dalyvavimas: {attendance_record}")


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']

Lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
Lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])


math_course.add_lesson(Lesson1)
math_course.add_lesson(Lesson2)


math_course.get_lessons()