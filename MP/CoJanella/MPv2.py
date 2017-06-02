class Student:
    grades = {}
    enrolledCourses = []

    def __init__(self, student_name, id_num):
        self.set_id_num(id_num)
        self.set_name(student_name)

#get the name of the student
    def get_name(self):
        return self.student_name

#get the id number of the student
    def get_id_num(self):
        return self.id_num

#get grades
    def get_grades(self):
        return self.grades

#get list of enrolled courses:
    def get_enrolled_courses(self):
        return self.enrolledCourses

#check and set the name of the student
    def set_name(self, s_name):
        if s_name != '':
            self.student_name = s_name
        else:
            print('\nINVALID INPUT')

#check and set the id number of the student
    def set_id_num(self, id_num):
        if id_num != '' and len(id_num) == 8:
            self.id_num = id_num
        else:
            print('\nINVALID INPUT')

#set the grade for a subject
    def set_grade(self, code):
        for i in range(len(self.enrolledCourses)):
            if str(self.enrolledCourses[i].get_code()) == str(code):
                grade = input('Enter grade for ' + str(code) + ': ')
                self.grades[str(code)] = grade
                print('SUCCESSFULLY SET GRADE FOR STUDENT')

#add a subject to a student's enrolled list
    def add_subject(self, course):
        found = False
        for i in range(len(self.enrolledCourses)):
                if str(course.get_code()) == str(self.enrolledCourses[i].get_code()):
                    found = True
                    print('ALREADY ENROLLED IN ' + course.get_code(), end='\n')

        if not bool(found):
            self.enrolledCourses.append(course)
            self.grades[str(course.get_code())] = -1

        # print(list(self.enrolledCourses))
        # print('SUCCESSFULLY ADDED TO STUDENT\'S ENROLLED COURSES')

#delete a subject from student's enrolled list
    def del_subject(self,  course):
        index = ''
        for i in range(len(self.enrolledCourses)):
            if str(course) == str(self.enrolledCourses[i].get_code()):
                self.enrolledCourses.pop(i)
                break

#print the details of the student lol
    def print_student(self):
        print('NAME: ' + self.get_name(), end=' ')
        print('ID NUMBER: ' + str(self.get_id_num()))

#print the enrolled courses of the student
    def print_enrolled_courses(self):
        self.print_student()
        for i in range(len(self.enrolledCourses)):
            self.enrolledCourses[i].print_course_details()

#print grades of the student
    def print_grades(self):
        if bool(self.grades):
            for key, grade in self.grades.items():
                if grade != -1:
                    print(key + ': ' + grade)
        else:
            print('STUDENT HAS NO GRADES')

class Course:
    students_list = []

    def __init__(self, code, units):
        self.set_units(units)
        self.set_code(code)

#get the course code
    def get_code(self):
        return self.code

#get the number of units
    def get_units(self):
        return self.units

#get student list
    def get_student_list(self):
        return self.students_list

#set the new course code
    def set_code(self, code):
       self.code = code

#set new number of units
    def set_units(self, units):
        self.units = units

#set students list
    def set_students_list(self, students_list):
        for i in range(len(self.students_list)):
                self.students_list[i] = students_list[i]

#drop a student
    def drop_student(self, student):
        if bool(self.students_list):
            for i in range(len(self.students_list)):
                if self.students_list[i].get_id_num() == student.get_id_num():
                    self.students_list.pop(i)
                    print('SUCCESSFULLY DROPPED ' + str(student.get_id_num()) + ': ' + str(student.get_name()))
                    break
        else:
            print('THERE ARE NO STUDENTS ENROLLED IN THIS COURSE')

#print the course details
    def print_course_details(self):
        print('COURSE CODE: ' + self.get_code() + ' UNITS: ' + str(self.get_units()), end='\n')

#print all the students enrolled in this course
    def print_enrolled_students(self):
        if bool(self.students_list):
            for i in range(len(self.students_list)):
                self.students_list[i].print_student()
        else:
            print('THERE ARE NOT STUDENts ENROLLED IN THIS COURSE')

students = [Student('Gabe Villarin', '11363997'), Student('Janella Co', '11524669')]
courses = [Course('HCIFACE', '3'), Course('AUTOMAT', '3')]

# ---- Displays the Main Menu ----
def mainMenu():
    opt_1 = ''
    while opt_1 != '0':
        print('\nMAIN MENU : ')
        print('[1]: Student \n'
              '[2]: Course \n'
              '[0]: Exit\n')
        opt_1 = input('Enter number: ')
        if (opt_1 == '1'):
            subMenu_Student()
        elif (opt_1 == '2'):
            subMenu_Course()

# ---- Add Student to List ----
def addStudent():
    sName = input('\nEnter Student Name: ')
    idNum = input('Enter ID Number: ')
    tempStudent = Student(str(sName), str(idNum))
    students.append(tempStudent)
    tempStudent.print_student()

# ---- Delete Student from List ----
def deleteStudent(index):
    print('DELETE ' + students[index].get_name() + ' (' + students[index].get_id_num() + ')?', end=' ')
    answer = input('[Y/N] ')
    if answer == 'Y' or answer == 'y':
        students.pop(index)
        print('\nSUCCESSFULLY DELETED STUDENT FROM LIST')

# ---- Find a student in a students list ----
def findStudent(idNum):
    if bool(students):
        for i in range(len(students)):
            if str(students[i].get_id_num()) == str(idNum):
                print('STUDENT FOUND')
                return i
    else:
        print('THERE ARE NO STUDENTS\n')
    return None

# ---- Displays all the Students in the list ----
def displayAllStudents():
    if bool(students):
        for i in range(0, len(students)):
            students[i].print_student()
    else:
        print('THERE ARE NO STUDENTS')

#---- Display Student Sub-menu ----
def subMenu_Student():
    opt_2 = ''
    while opt_2 != '0':
        print('\n[1]: Add Student \n'
              '[2]: Delete Student\n'
              '[3]: Edit Student ID Number\n'
              '[4]: Edit Student Name\n'
              '[5]: Set Student Grade\n'
              '[6]: View Report Card\n'
              '[7]: View All Students\n'
              '[0]: Back to Main Menu')
        opt_2 = input('Enter number: ')

        if opt_2 == '1':
            addStudent()

        elif opt_2 == '2':
            print()
            displayAllStudents()
            studentToFind = input('\nEnter Student ID Number: ')
            x = findStudent(studentToFind)
            if x != None:
                deleteStudent(x)

        elif opt_2 == '3':
            print()
            displayAllStudents()
            studentToFind = input('\nEnter Student ID Number: ')
            x = findStudent(studentToFind)
            if x != None:
                print('EDIT ' + students[x].get_name() + ' (' + students[x].get_id_num() + ')?', end=' ')
                answer = input('[Y/N] ')
                if answer == 'Y' or answer == 'y':
                    newIdNum = input('Enter NEW Student ID Number: ')
                    tempStudent = Student(students[x].get_name(), newIdNum)
                    students.pop(x)
                    students.append(tempStudent)
                    print('\nSUCCESSFULLY UPDATED STUDENT ID NUMBER')
            else:
                print('COULD NOT FIND STUDENT')

        elif opt_2 == '4':
            print()
            displayAllStudents()
            studentToFind = input('\nEnter Student ID Number: ')
            x = findStudent(studentToFind)
            if x != None:
                print('EDIT ' + students[x].get_name() + ' (' + students[x].get_id_num() + ')?', end=' ')
                answer = input('[Y/N] ')
                if answer == 'Y' or answer == 'y':
                    newName = input('Enter NEW Student Name: ')
                    tempStudent = Student(newName, students[x].get_id_num())
                    students.pop(x)
                    students.append(tempStudent)
                    print('\nSUCCESSFULLY UPDATED STUDENT NAME')
            else:
                print('COULD NOT FIND STUDENT')

        elif opt_2 == '5':
            studentToFind = input('\nEnter Student ID Number: ')
            x = findStudent(studentToFind)
            if x != None:
                print('ADD GRADE TO ' + students[x].get_name() + ' (' + students[x].get_id_num() + '?', end=' ')
                answer = input('[Y/N] ')
                if bool(students[x].get_enrolled_courses()) and (answer == 'Y' or answer == 'y'):
                    students[x].print_enrolled_courses()
                    subject = input('\nEnter subject code: ')
                    students[x].set_grade(subject)
                else:
                    print('STUDENT IS NOT ENROLLED IN ANY COURSE')
            else:
                print('COULD NOT FIND STUDENT')

        elif opt_2 == '6':
            print()
            displayAllStudents()
            studentToFind = input('\nEnter Student ID Number: ')
            x = findStudent(studentToFind)
            if x != None:
                students[x].print_grades()
            totalGrade = 0
            totalUnits = 0
            grades = students[x].get_grades()
            enrolledCourses = students[x].get_enrolled_courses()
            for i in range(len(enrolledCourses)):
                if grades[enrolledCourses[i].get_code()] != -1:
                    temp = int(grades[enrolledCourses[i].get_code()])
                    totalUnits += int(enrolledCourses[i].get_units())
                    # print(str(grades[enrolledCourses[i].get_code()]))
                    temp *= int(enrolledCourses[i].get_units())
                    # print(str(enrolledCourses[i].get_units()))
                    totalGrade += int(temp)
                    # print(int(temp))
            gpa = totalGrade/totalUnits
            print('GPA: ' + str(gpa))

        elif opt_2 == '7':
            print()
            displayAllStudents()

        else:
            print('INVALID INPUT')

# ---- Add Course to List ----
def addCourse():
    code = input('Input course code: ')
    units = input('Input number of units [floating, 0-4]: ')
    if len(code) == 7 and (str(units) in ('0', '1', '2', '3', '4', 'floating')):
        tempCourse = Course(code, units)
        courses.append(tempCourse)
        print('CREATED COURSE: ', end='\n\t')
        tempCourse.print_course_details()
    else:
        print('\nINVALID INPUT\n')
        addCourse()

# ---- Find a Course in the Courses List ----
def findCourse(code):
    for course in courses:
        if str(course.get_code()) == str(code):
            print('COURSE FOUND\n')
            return courses.index(course)
    return None

# ---- Delete a course from the list
def deleteCourse(index):
    print('DELETE ' + courses[index].get_code() + ' (' + courses[index].get_units() + ')?', end=' ')
    answer = input('[Y/N] ')
    if answer == 'Y' or answer == 'y':
        courses.pop(index)
        print('\nSUCCESSFULLY DELETED COURSE FROM LIST')

# ---- View all courses ----
def displayAllCourses():
    if bool(courses):
        for i in range(0, len(courses)):
            courses[i].print_course_details()
    else:
        print('THERE ARE NO COURSES')

# ---- Display Course Sub-Menu ----
def subMenu_Course():
    opt_2 = ''
    while opt_2 != '0':
        print('\n[1]: Add Course\n'
              '[2]: Delete Course\n'
              '[3]: Edit Course Code\n'
              '[4]: Edit Course Units\n'
              '[5]: Enroll a Student\n'
              '[6]: Drop a Student\n'
              '[7]: View All Courses\n'
              '[8]: View Enrolled Students in Course\n'
              '[0]: Back to Main Menu')
        opt_2 = input('Enter number: ')

        if opt_2 == '1':
            print()
            addCourse()

        elif opt_2 == '2':
            print()
            displayAllCourses()
            if bool(courses):
                courseToFind = input('\nEnter Course Code: ')
                x = findCourse(courseToFind)
                if bool(courses) and x != None:
                    deleteCourse(x)
                else:
                    print('CANNOT FIND COURSE/INVALID COURSE CODE\n')

        elif opt_2 == '3':
            print()
            displayAllCourses()
            if bool(courses):
                courseToFind = input('\nEnter Course Units: ')
                x = findCourse(courseToFind)
                if bool(courses) and x != None:
                    print('EDIT ' + courseToFind + '?', end=' ')
                    answer = input('[Y/N] ')
                    if answer == 'Y' or answer == 'y':
                        newUnits = ''
                        while str(newUnits) not in ('0', '1', '2', '3', '4', 'floating'):
                            newUnits = input('Enter NEW Course Units: ')
                        tempCourse = Course(courses[x].get_code(), newUnits)
                        courses.pop(x)
                        courses.append(tempCourse)
                        print('\nSUCCESSFULLY UPDATED COURSE CODE\n')
                else:
                    print('CANNOT FIND COURSE\n')

        elif opt_2 == '4':
            print()
            displayAllCourses()
            if bool(courses):
                courseToFind = input('\nEnter Course Code: ')
                x = findCourse(courseToFind)
                if x != None:
                    print('EDIT ' + courseToFind + '?', end=' ')
                    answer = input('[Y/N] ')
                    if answer == 'Y' or answer == 'y':
                        newUnits = ''
                        while str(newUnits) not in ('0', '1', '2', '3', '4', 'floating'):
                            newUnits = input('Enter NEW Course Units: ')
                        tempCourse = Course(courses[x].get_code(), newUnits)
                        courses.pop(x)
                        courses.append(tempCourse)
                        print('\nSUCCESSFULLY UPDATED COURSE UNITS\n')
                else:
                    print('CANNOT FIND COURSE\n')

        elif opt_2 == '5':
            print()
            displayAllCourses()
            if bool(courses):
                courseToFind = input('\nEnter Course Code: ')
                x = findCourse(courseToFind)
                if x != None and bool(students):
                    print('Enrolling a student in ' + courseToFind + ': ')
                    displayAllStudents()
                    print()
                    idNum = input('Enter student ID number: ')
                    y = findStudent(idNum)
                    if y != None:
                        print('ENROLL ' + idNum + ' (' + str(students[y].get_name()) + ')?', end=' ')
                        answer = input('[Y/N] ')
                        if answer == 'Y' or answer == 'y':
                            s_list = courses[x].get_student_list()
                            if len(s_list) == 0:
                                s_list.append(students[y])
                                students[y].add_subject(courses[x])
                                courses[x].set_students_list(s_list)
                                print('SUCCESSFULLY ENROLLED ' + str(students[y].get_id_num()) + ': ' + str(
                                    students[y].get_name() + ' TO ' + courseToFind))
                            else:
                                if not students[y] in s_list:
                                    s_list.append(students[y])
                                    print('SUCCESSFULLY ENROLLED ' + str(students[y].get_id_num()) + ': ' + str(
                                        students[y].get_name() + ' TO ' + courseToFind))
                                    students[y].add_subject(courses[x])
                                    courses[x].set_students_list(s_list)
                                else:
                                    print('DUPLICATE STUDENT ' + str(students[y].get_id_num()) + ': ' + str(
                                        students[y].get_name()))
                                    break
                        else:
                            print('\nCANNOT FIND STUDENT')

        elif opt_2 == '6':
            print()
            displayAllCourses()
            if bool(courses):
                courseToFind = input('\nEnter Course Code: ')
                x = findCourse(courseToFind)
                if x != None and bool(courses[x].get_student_list()):
                    courses[x].print_enrolled_students()
                    print()
                    idNum = input('Enter student ID number: ')
                    y = findStudent(idNum)
                    if y != None:
                        print('DROP ' + idNum + ' (' + str(students[y].get_name()) + ')?', end=' ')
                        answer = input('[Y/N] ')
                        if answer == 'Y' or answer == 'y':
                            students[y].del_subject(courses[x].get_code())
                            courses[x].drop_student(students[y])
                else:
                    print('INVALID ID NUMBER/THERE ARE NO STUDENTS ENROLLED IN THIS SUBJECT\n')

        elif opt_2 == '7':
            print()
            displayAllCourses()

        elif opt_2 == '8':
            print()
            displayAllCourses()
            if bool(courses):
                courseToFind = input('\nEnter Course Code: ')
                x = findCourse(courseToFind)
                if x != None:
                    courses[x].print_enrolled_students()

if __name__ == '__main__':
    mainMenu()