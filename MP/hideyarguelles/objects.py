class Student:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.grades = {}
        self.gpa = 0.0

    # Edits the information of the student.
    def edit_info(self, new_name, new_id):
        self.name = new_name
        self.id_number = new_id

    # Enrols a student in a course.
    def enrol_course(self, course):
        self.grades[course] = 0.0

    # Drops the student from a course.
    def drop_course(self, course):
        del self.grades[course]

    # Views the report card of the student.
    # This should work properly if the setting of grades works.
    def view_grades(self):
        if len(self.grades) != 0:
            print("\nID Number: " + self.id_number + "\nName: " + self.name)
            print("\nCOURSE\t\tGRADE")

            for course in self.grades.items():
                print(course[0].course_code + "\t\t" + str(course[1]))
            print("\nGPA: " + str(self.calculate_gpa()))  # prints the student's GPA
        else:
            print("\nThis student is not enrolled in any course.")

    # Calculates the student's GPA.
    def calculate_gpa(self):
        unit_sum = 0
        grade_sum = 0
        for course in self.grades.items():
            unit_sum += course[0].units
            grade_sum += (course[0].units * course[1])
        return grade_sum / unit_sum


class Course:

    def __init__(self, course_code, units):
        self.course_code = course_code
        self.units = units
        self.students = []

    # Edits the information of the course.
    def edit_info(self, new_code, new_units):
        self.course_code = new_code
        self.units = new_units

    # Enrols a student in the course.
    def enrol_student(self, student):
        self.students.append(student)