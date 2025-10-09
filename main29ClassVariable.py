# class variable = Shared among all instances of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from that class

class Student :

    class_year = 2025
    num_student=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_student += 1

student1 = Student("Spongebob",30)
student2 = Student("Patrick",35)
student3 = Student("Squidward",55)
student4 = Student("Sandy",27)

# kenapa class_year dan num_student tak guna self sebab self adalah untuk specific untuk object
# cth nye name dan age ini hanya specific untuk object sbb they have their own value
# but class_year and num_studentt they are class variable means they shared all object student 1 until 4 
# thats why dkt dlm contructor kita Student.num_student += 1 dia outputkan 4 sebab dia boleh detect count
# object yang buat value dekat constructor tu
print()
print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)