class StupidExeption(Exception):
    def __init__(self, ExeptionReason):
        self.ExeptionReason = ExeptionReason

class NotNegVal:
    def __set_name__(self, owner,  name):
        self.name = name

    def __get__(self, instance):
         return instance.__dict__[self.name]
    
    def __set__(self, instance, val):
        if int(val) < 0:
            raise StupidExeption("Значение маловато, чел")
        instance.__dict__[self.name] = val


class University:  
    years = NotNegVal()
    salary = NotNegVal()
    def __init__(self, name, years, place, salary):
        self.salary = salary
        self.name = name
        self.place = place
        self.years = years
        
    def EducationPlace(self):
        print(str(self.name) + " связан с ВУЗом " + str(self.place))

    
class Teatcher(University):
    def __init__(self,name, years, place, salary, post):
        University.__init__(self, name, years, place, salary)
        self.post = post
    def Post(self):
        print(str(self.name) + " работает на кафедре " +str(self.post))

class Student(University):
    def __init__(self, name, years, place, salary, programm):
        University.__init__(self, name, years, place, salary)
        self.programm = programm
    
    def EducationProgramm(self):
        print(str(self.name) + " учится на кафедре "+str(self.programm))

    def EducatSalary(self):
        print(str(self.salary))

    def EducatYears(self):
        print(str(self.years))

    @property
    def years(self):
        return self._years
    @years.setter
    def years(self, ChangeVal):
        if ChangeVal > 5:
            raise StupidExeption("Дохрена лет обучения, чел")
        self._years = ChangeVal    # показывает, что переменная приватная и ее не стоит менять"
     
Edik = Student("fe", -3, "be", -9000, "neb")
Edik.EducatYears()