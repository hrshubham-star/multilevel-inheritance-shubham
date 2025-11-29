# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Derived class Student (from Person)
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        super().display()
        print(f"Course: {self.course}")


# Derived class Exam (from Student)
class Exam(Student):
    def __init__(self, name, age, course, mark1, mark2, mark3):
        super().__init__(name, age, course)
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.total = mark1 + mark2 + mark3

    def display(self):
        super().display()
        print(f"Marks: {self.mark1}, {self.mark2}, {self.mark3}")
        print(f"Total Marks: {self.total}")


# Creating an object of Exam class
student1 = Exam("Alice", 20, "Computer Science", 85, 90, 88)

# Displaying details
student1.display()
