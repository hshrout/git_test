class Student: 
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self): 
        return self.grade 
    
class Course: 
    def __init__(self, name, max_students): 
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student): 
        if len(self.students) < self.max_students: 
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self): 
        value = 0 
        for student in self.students: 
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Hanna", 22, 16)
s2 = Student("Haley", 17, 12)
s3 = Student("Finley", 7, 4)

print(Student.get_grade(s1))

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())


