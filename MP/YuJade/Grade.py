from Course import *

class Grade:
    def __init__(self, course, grade):
        self.setCourse(course)
        self.grade = 0.0
        self.setGrade(grade)

    def setCourse(self, course):
        self.course = course

    def setGrade(self, grade):
        grade_list = ["0.0", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0"]

        for x in range(0, len(grade_list)):
            if float(grade) == float(grade_list[x]):
                self.grade = grade

    def getCourse(self):
        return self.course

    def getGrade(self):
        return self.grade

    def print_info(self):
        return self.course.getCourseCode() + "  " + str(self.grade)