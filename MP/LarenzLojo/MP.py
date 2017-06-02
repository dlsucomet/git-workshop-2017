studentList = []
courseList = []
class Student:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        self.classes = []
        self.grades = []
        print(name + ' with ID Number ' + idnumber + ' has been added!')

def addStudent():
    print("Enter student's name: ")
    name = input()
    print("Enter student's id number: ")
    idnumber = input()
    if(not studentExists(idnumber)):
        student = Student(name,idnumber)
        return student;

def studentExists(idnumber):
    for student in studentList:
        if (idnumber == student.idnumber):
            print('ERROR! ID number already exists!')
            return True
        
    return False

def enrolltocourse(idnumber, codein):
    for course in courseList:
        if(course.code == codein):
            tempcourse = course
            tempgrade = [course.code, 'ngs']
            
    for student in studentList:
        if(student.idnumber == idnumber):
            student.classes.append(tempcourse)
            student.grades.append(tempgrade)

class Course:
    def __init__(self, code, units):
        self.code = code
        self.units = units
        print(code + ' (' + units + ' units) has been added!')
	
def addCourse():
    print("Enter course code:")
    code = input()
    print("Enter number of units:")
    units = input()	
            
    validCode = False
    while(not validCode):
        if(len(code) > 7):
            print('WARNING! Code too long. First 7 chars used instead')
            self.code = code[:7]
            validCode = True
        elif (len(code) < 7):
            print('ERROR! Code too short. Code must be 7 characters')
            print('Input new code: ')
            code = input()
        else:
            validCode = True
            
            for course in courseList:
                if(units == course.code):
                    ('ERROR! Code already exists')
                    existsCode = False
                    
            validUnits = False
            while(not validUnits):
                if(not isinstance(units,float)):
                    if(float(units) > 4.0):
                        print('ERROR! Units should be floating or 0 to 4')
                        print('Input new number of Units: ')
                        units = input()
                    elif(float(units) < 0.0):
                        print('ERROR! Units should be floating or 0 to 4')
                        print('Input new number of Units: ')
                        units = input()
                    else:
                        validUnits = True
                elif(not isinstance(units,str)):
                    if(not str(units) == 'floating'):
                        print('ERROR! Units should be floating or 0 to 4')
                        print('Input new number of Units: ')
                        units = input()
                    else:
                        validUnits = True
                else:
                    print('ERROR! Units should be floating or 0 to 4')
                    print('Input new number of Units: ')
                    units = input()
                    
    if(validUnits == True and validCode == True):
        tempcourse = Course(code,units)

        return tempcourse
            


    
    
    

mainmenu = 0;
while(not mainmenu == 14):
    print('< - - MAIN MENU - - >')
    print('       + VIEW +')
    print(' [1] - VIEW ALL STUDENTS')
    print(' [2] - VIEW ALL COURSE')
    print()
    print('     + STUDENT +')
    print(' [3] - ADD STUDENT')
    print(' [4] - EDIT STUDENT')
    print(' [5] - DELETE STUDENT')
    print()
    print('     + COURSES +')
    print(' [6] - ADD COURSE')
    print(' [7] - EDIT COURSE')
    print(' [8] - DELETE COURSE')
    print()
    print('    + ENROLLMENT +')
    print(' [9] - ENROLL A STUDENT')
    print(' [10]- DROP A STUDENT')
    print()
    print('      + GRADE +')
    print(' [11]- SET GRADE FOR STUDENT')
    print(' [12]- VIEW STUDENT\'S REPORT CARD')
    print()
    print(' [14]- END')
    
    mainmenu = input()

    if(int(mainmenu) == 1):
        numbering = 0
        for student in studentList:
            numbering = numbering + 1
            print(str(numbering) + ". " + str(student.idnumber) + " - " + str(student.name))
            
    if(int(mainmenu) == 2):
        numbering = 0
        for course in courseList:
            numbering = numbering + 1
            print(str(numbering) + '. ' + str(course.code) + ' - ' + str(course.units))
            
    if(int(mainmenu) == 3):
        student = addStudent()
        studentList.append(student)

    if(int(mainmenu) == 4):
        edited = False
        while(not edited):
            numbering = 0
            for student in studentList:
                numbering = numbering + 1
                print(str(numbering) + ". " + str(student.idnumber) + " - " + str(student.name))

            print('Input ID number of student')
            idnum = input()

            for student in studentList:
                if(student.idnumber == idnum):
                    print("IDNUMBER: " + student.idnumber + " - NAME: " + student.name)
                
                    print('  + INFO TO CHANGE +')
                    print(' [1] - NAME')
                    print(' [2] - IDNUMBER')

                    editstudent = input()
                
                    if(int(editstudent) == 1):
                        print('Enter new name: ')
                        newName = input()

                        student.name = newName
                        print('Name has been changed')
                        edited = True

                    if(int(editstudent) == 2):
                        print('Enter new ID number: ')
                        newIdnum = input()

                        student.idnumber = newIdnum
                        print('ID number has been changed')
                        edited = True
            

    if(int(mainmenu) == 5):
        numbering = 0
        for student in studentList:
            numbering = numbering + 1
            print(str(numbering) + ". " + str(student.idnumber) + " - " + str(student.name))
        
        print('Enter ID Number of student to delete: ')
        idnum = input()
        for student in studentList:
            if(student.idnumber == idnum):
                studentList.remove(student)
                print('Student has been deleted!')
        
    if(int(mainmenu) == 6):
        tempcourse = addCourse()
        courseList.append(tempcourse)

    if(int(mainmenu) == 7):
        edited = False
        while(not edited):
            numbering = 0
            for course in courseList:
                numbering = numbering + 1
                print(str(numbering) + '. ' + str(course.code) + ' - ' + str(course.units))

            print('Input ID number of student')
            coursecode = input()

            for course in courseList:
                if(course.code == coursecode):
                    print("COURSE CODE: " + course.code + " - UNITS: " + course.units)
                
                    print('  + INFO TO CHANGE +')
                    print(' [1] - CODE')
                    print(' [2] - UNITS')

                    editcourse = input()
                
                    if(int(editcourse) == 1):
                        print('Enter new course code: ')
                        newCode = input()

                        course.code = newCode
                        print('Course code has been changed')
                        edited = True

                    if(int(editcourse) == 2):
                        print('Enter new number of units: ')
                        newUnits = input()

                        course.units = newUnits
                        print('Number of units has been changed')
                        edited = True
        
    if(int(mainmenu) == 8):
        numbering = 0
        for course in courseList:
            numbering = numbering + 1
            print(str(numbering) + '. ' + str(course.code) + ' - ' + str(course.units))
        
        print('Enter ID Number of student to delete: ')
        code = input()
        for course in courseList:
            if(course.code == code):
                courseList.remove(course)
                print('Course has been deleted!')
        
    if(int(mainmenu) == 9):
        print('Enter Student ID Number: ')
        idnumber = input()
        print('Enter Course code:')
        code = input()
        enrolltocourse(idnumber, code)

        

    if(int(mainmenu) == 10):
        print('Enter ID number: ')
        idnum = input()

        for student in studentList:
            if(student.idnumber == idnum):
                numbering = 0
                for classes in student.classes:
                    numbering = numbering + 1
                    print(str(numbering) + '. ' + str(classes.code) + ' - ' + str(classes.units))

            classtodrop = input()
            for classes in student.classes:
                if(classes.code == classtodrop):
                    student.classes.remove(classes)
                    print('Class has been dropped!')
        
    if(int(mainmenu) == 11):
        print('Enter ID number: ')
        idnum = input()
        
        for student in studentList:
            if(student.idnumber == idnum):
                numbering = 0
                for classes in student.classes:
                    numbering = numbering + 1
                    print(str(numbering) + '. ' + str(classes.code) + ' - ' + str(classes.units) + ' units')

            print('Enter class: ')
            classtograde = input()
            print('Enter grade: ')
            grade = input()
            
            for grades in student.grades:
                if(grades[0] == classtograde):
                    grades[1] = grade
                    print('Class has been graded!')

        

        

    if(int(mainmenu) == 12):
        print('Enter ID number: ')
        idnum = input()

        total = 0
        totalunits = 0
        
        for student in studentList:
            if(student.idnumber == idnum):
                numbering = 0
                for grades in student.grades:
                    numbering = numbering + 1
                    print(str(numbering) + '. CODE: ' + str(grades[0]) + ' - GRADE: ' + str(grades[1]))


