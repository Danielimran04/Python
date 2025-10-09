# class method = Allow operations related to the class itself 
#                Take (clf) as the first parameter, which represent the class itself

class Student:
    count = 0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count += 1 # class method so dia akan jadi Student.(variable yang di create dlm class)
        Student.total_gpa += gpa # class method so dia akan jadi Student.(variable yang di create dlm class)

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):# untuk print 
        return f"Total # students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):# untuk print 
        if cls.count==0:
            return 0
        else:
            return f"Average of gpa {cls.total_gpa/cls.count:.2f}"
    
student1=Student("daniel",3.9)
student2=Student("leman",3.5)
student3=Student("manaf",3.6)
student4=Student("sandy",3.9)
    
print(Student.get_count())
print(Student.get_average_gpa())

# cls nih memang untuk kelas sahaja bukan untuk object sbb cls nih hanya boleh tahu nilai bila object masuk nilai
# and then buat variable untuk masukkan nilai object tu and then boleh kira
# self nih hanya untuk object sahajaaaaaa

#  Imagine your class Student is a university:
#  self = one specific student in the university (e.g., "Daniel").
#  Knows their own name and GPA.
#  cls = the university itself.
#  Knows how many total students are enrolled and what the average GPA is.