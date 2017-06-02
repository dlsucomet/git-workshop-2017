class Course:
    def __init__(self, courseCode, units):
        self.setCourseCode(courseCode)
        self.units = 0.0
        self.setUnits(units)
        self.students = []

    def setCourseCode(self, courseCode):
        if len(courseCode) == 7:
            self.courseCode = courseCode
            return True
        else:
            return False

    def setUnits(self, units):
        unit_list = ["0.0", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0"]

        for x in range(0, len(unit_list)):
            if float(units) ==float(unit_list[x]):
                self.units = units

    def getCourseCode(self):
        return self.courseCode

    def getUnits(self):
        return self.units

    def enrollStudent(self, student):
        self.students.append(student)
        self.students.sort(key = lambda student: student.idNumber)

    def dropStudent(self, id):
        for i in range(0,len(self.students) ) :
            if id == self.students[i].idNumber:
                del self.students[i]

    def print_info(self):
        return self.courseCode + "  " + str(self.getUnits())

    def print_students(self):
        for x in range(0, len(self.students)) :
            print(+ str(x) + self.students[x].print_info())