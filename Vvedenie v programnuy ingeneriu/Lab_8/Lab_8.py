### LAB NUMBER 8 PEP8 ###

class Student():


    ###Description of students
    def __init__(self, Name, Surname, Patronymic, Course, Years):
        self.Name = Name
        self.Surname = Surname
        self.Patronymic = Patronymic
        self.Course = Course
        self.years = Years


    ###Student
    def get_full_name(self):
        name = f"Студент {self.Course} курса - {self.Surname} {self.Name} {self.Patronymic} {self.Years} г.р."
        return name.title()

###                   Name --- Surname --- Patronymic - Course - Year of birth
Student_1 = Student('Михаил', 'Кузьмин', 'Константинович', '1', '2000')
Student_2 = Student('Василий', 'Василев', 'Васильевич', '2', '2002')
Student_3 = Student('Николай', 'Николаев', 'Николаевич', '3', '2001')
Student_4 = Student('Дмитрий', 'Дмитреев', 'Дмитриевич', '4', '1998')
Student_5 = Student('Михаил', 'Мишин', 'Михайлович', '1', '2003')

###Output
print(Student_1.get_full_name())
print(Student_2.get_full_name())
print(Student_3.get_full_name())
print(Student_4.get_full_name())
print(Student_5.get_full_name())
