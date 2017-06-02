class Student:
    def __init__(self, name = "", idNumber = ""):
        self.name = name
        self.idNumber = idNumber
        self.courses = []
        self.grades = []

    def setName(self, name):
        self.name = name

    def setID(self, id):
        self.idNumber = id

    def getName(self):
        return self.name

    def getID(self):
        return self.idNumber

    def enroll(self, course):
        self.courses.append(course)
        self.courses.sort()

    def drop(self, course):
        index = self.courses.index(course)
        del self.courses[index]

    def assign_grade(self, grade):
        self.grades.append(grade)

    def see_grade(self):
        scores = 0
        units = 0
        total_units = 0;
        for x in range(0, len(self.grades)) :
            print(self.grades[x].print_info())
            units = self.grades[x].getCourse().getUnits()
            scores = scores + self.grades[x].getGrade() * units
            total_units += units
        gpa = (scores/total_units)
        print("GPA : %.3f" %gpa)

    def print_info(self):
        return self.idNumber + "  " + self.name

    def print_courses(self):
        for x in range(0, len(self.courses)) :
            print(self.courses[x].print_info())
