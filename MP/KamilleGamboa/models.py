class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.course_grade = {}


class Course:
    def __init__(self, unit, code):
        self.code = code
        self.unit = unit