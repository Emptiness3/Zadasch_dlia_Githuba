class Student():
    """Описание студента"""
    def __init__(self, Imia, Vamilia, Otchestvo, kurs, years):
        """Инициализирует атрибуты"""
        self.Imia = Imia
        self.Vamilia = Vamilia
        self.Otchestvo = Otchestvo
        self.kurs = kurs
        self.years = years


    def get_full_name(self):
        """Студент"""
        name = f"Студент {self.kurs} курса -  {self.Vamilia} {self.Imia} {self.Otchestvo};  {self.years} года рождения"
        return name.title()


Student_1 = Student('Михаил', 'Кузьмин', 'Константинович', '1', '2000')
Student_2 = Student('Василий', 'Василев', 'Васильевич', '2', '2002')
Student_3 = Student('Николай', 'Николаев', 'Николаевич', '3', '2001')
Student_4 = Student('Дмитрий', 'Дмитреев', 'Дмитриевич', '4', '1998')
Student_5 = Student('Михаил', 'Мишин', 'Михайлович', '1', '2003')


print(Student_1.get_full_name())
print(Student_2.get_full_name())
print(Student_3.get_full_name())
print(Student_4.get_full_name())
print(Student_5.get_full_name())
