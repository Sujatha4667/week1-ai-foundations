class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name,self.marks)

s1 = Student("Akash",91)
s1.display()