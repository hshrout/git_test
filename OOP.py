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

'''
s1 = Student("Hanna", 22, 16)
s2 = Student("Haley", 17, 12)
s3 = Student("Finley", 7, 4)

print(Student.get_grade(s1))

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())

'''

#Inheritance

#General 
class Pet: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} ")

    def speak(self): 
        print("???")


#Specific, inherited from Pet
class Cat(Pet): 
    def __init__(self, name, age, color): 
        super().__init__(name, age)
        self.color = color 

    def speak(self): 
         print("Meow")
    
    def show(self): 
        print(f"I am {self.name} and I am {self.age} and I am {self.color} ")

class Dog(Pet): 
        def speak(self): 
            print("Bark")

class Fish(Pet): 
    pass
"""
p = Pet("Radar", 12 )
p.show()
p.speak()

c = Cat("Malcom", 10, "Orange")
c.show()
c.speak()

d = Dog("Finley", 7)
d.speak()

f = Fish("Freddy", 6)
f.speak()

"""

#Class Attributes: Attributes --specific to the class; could be constant 
#Class Methods: Act on class itself, not access any instance 

class Person: 
    number_people = 0     #Class attribute, not use self; 

    def __init__(self, name): 
        self.name = name
        Person.number_people += 1

    @classmethod
    def number_people_(cls): 
        return cls.number_people()
    
    @classmethod
    def add_person(cls): 
        cls.number_people += 1

"""
p1 = Person("hanna")
print(Person.number_people)
p2 = Person("fin")
print(Person.number_people)
"""

#Static Methods: Do something, dont change anything; functions inside class

class Math: 
    @staticmethod
    def add5(x):
        return x + 5 
    
print(Math.add5(3))




