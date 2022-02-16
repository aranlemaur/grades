class Student():

    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree

    def grade(self, grade1, grade2, grade3):  
        average = (grade1 + grade2 + grade3) / 3
        return f"Their course average is {round(average, 2)}\n********  *********  ********  *********"

num = 3
for i in range(num):
    stud1 = Student(
        name = input("Please add your student's name: "),
        age = int(input("Please add your student's age: ")),
        degree = input("Please add their degree: ")
    )
    

    print(f"{stud1.name} is {stud1.age} and they are studying {stud1.degree}")
    print(stud1.grade(float(input("Please enter their first exam grade: ")), float(input("Please enter their essay grade: ")), float(input("Please enter their final exam grade: "))))
