import os

students = ['Jared', 'Gary']
idNum = {'Jared': 11500000, 'Gary':11500001}
studCourses = {11500000: [], 11500001: []}

courseList = ['Computer Programming 1', 'Object Oriented Programming']
courseCodes = {'Computer Programming 1': 'COMPRO1', 'Object Oriented Programming': 'OBJECTP'}
courseInfo = {'COMPRO1': [3, []], 'OBJECTP': [3, []]}



#Functions
def pressEnter():
    input('Press Enter to continue...')

#@param nameList is the List that contains the names which serve as the primary reference
#@param codeDictionary is the dictionary that references the nameList    
def changeName(index, nameList, codeDictionary):
    print('Please Enter New Name: ', end = '')
    newName = input()

    oldName = nameList[index]

    codeDictionary[newName] = codeDictionary.pop(oldName)
    
    nameList[index] = newName

#@param nameList is the List that contains the names which serve as the primary reference
#@param codeDictionary is the dictionary that refers to the nameList
#@param refDictionary is the dictionary that refers to the codeDictionary
def changeID(index, nameList, codeDictionary, refDictionary):
    print('Please Enter New ID number: ', end = '')
    newID = input()

    nameIndex = nameList[index]

    codeIndex = codeDictionary[nameIndex]

    codeDictionary[nameIndex] = newID

    refDictionary[newID] = refDictionary.pop(codeIndex)

def getLastListEntry(myList):

    entry = myList[len(myList) - 1]

    return entry

def computeGPA(courses):

    GPA = 0.0
    
    for index in range(len(courses)):
        GPA += courses[index][1]

    GPA = GPA / len(courses)

    return GPA

#Grades Functions
def setGrades():
    print('Set Grades\n')

    viewAllStudents()

    print('Enter index of Student (Enter 0 to return): ', end = '')
    student = input()

    student = int(student)

    if student != 0:
        student -= 1
        displayStudentCourses(student)

        print('Enter which course to set Grade (Enter 0 to return): ', end = '')
        course = input()
        course = int(course)

        if course != 0:
            #Getting Course List for Student
            studName = students[student]
            studID = idNum[studName]
            courses = studCourses[studID]

            #Getting Course Code
            courseName = courseList[course]
            courseCode = courseCodes[courseName]

            print('Enter grade (0.0 - 4.0): ', end = '')
            grade = input()
            grade = float(grade)

            #Setting Grade
            for i in range(len(courses)):
                if courses[i][0] == courseCode: 
                    courses[i][1] == grade

            studCourses[11500000].append(['COMPRO1', 0.0])
            studCourses[11500000][0][1] = 3.5

def viewReportCard():
    print('Generate Report Card\n')

    viewAllStudents()
    print('Enter index of Student (Enter 0 to return): ', end = '')
    student = input()

    student = int(student)

    if student != 0:
        student -= 1

        studName = students[student]
        studID = idNum[studName]
        courses = studCourses[studID]
        GPA = computeGPA(courses)

        print('Name: ' + str(studName))
        print('ID Number: '  + str(studID) + "\n")
        print('Courses being Taken: ')
        for i in range(len(courses)):
            print(str(i + 1) + ' ' + courses[i][0] + ' Grade: ' + str(courses[i][1]))
        print('GPA: ' + str(GPA))
        
        
    
            

#Enrollment functions
def displayStudentCourses(index):
    studName = students[index]
    studID = idNum[studName]
    courses = studCourses[studID]
    print('Courses enrolled by: ' + str(studName) + ', ID number: ' + str(studID) + '\n')
    for i in range(len(courses)):
        print(str(i + 1) + ' ' + courses[i][0])

def displayCoursesStudents(index):
    courseName = courseList[index]
    courseCode = courseCodes[courseName]
    studList = courseInfo[courseCode]
    print('Students (ID number) enrolled in: ' + str(courseName) + ', Course Code: ' + str(courseCode) + '\n')
    for i in range(len(studList[1])):
        print(str(i + 1) + ' ' + str(studList[1][i]))

              
    
def viewCoursesEnrolledByStudents():
    print('View Courses Enrolled by Students\n')

    viewAllStudents()

    print('Enter index of Student (Enter 0 to return): ', end = '')
    student = input()

    student = int(student)

    if student != 0:
        student -= 1
        displayStudentCourses(student)

def viewStudentsEnrolledInCourses():
    print('View Students Enrolled in Courses\n')

    viewAllCourses()

    print('Enter index of Course (Enter 0 to return): ', end = '')
    course = input()

    course = int(course)

    if course != 0:
        course -= 1
        displayCoursesStudents(course)
    
def enrollInCourse():
    print('Enrollment\n')

    viewAllStudents()

    print('Enter index of Student (Enter 0 to return): ', end = '')
    student = input()

    student = int(student)

    while student != 0:
        student -= 1

        viewAllCourses()
        
        print('Enter index of Course to enroll (Enter 0 to return): ', end = '')
        course = input()

        course = int(course)

        if course != 0:
            course -= 1

            #Getting StudentID
            studName = students[student]
            studID = idNum[studName]

            #Getting Course Code
            courseName = courseList[course]
            courseCode = courseCodes[courseName]
            
            #Student Enrolling in Course
            studCourses[studID].append([courseCode, 0.0])

            #Course Registering the Student
            courseInfo[courseCode][1].append(studID)

            student = 0

def dropCourse():
    print('Drop Courses\n')

    viewAllStudents()

    print('Enter index of Student (Enter 0 to return): ', end = '')
    student = input()

    student = int(student)

    while student != 0:
        student -= 1

        displayStudentCourses(student)

        print('Enter index of Course to Drop (Enter 0 to return): ', end = '')
        course = input()
        course = int(course)

        if course != 0:
            course -= 1

            #Data Collection
            studName = students[student]
            studID = idNum[studName]

            courseName = courseList[course]
            courseCode = courseCodes[courseName]

            courses = studCourses[studID]
            studList = courseInfo[courseCode]

            #Dropping
            for i in range(len(courses)):
                if courses[i][0] == courseCode:
                    courses[i][1] = 0
                
            courses.remove([courseCode, 0])

            studList[1].remove(studID)
  

#Course functions
def changeUnits(index):
    print('Please Enter new units: ', end = '')
    newUnits = input()
    newUnits = int(newUnits)

    nameIndex = courseList[index]
    codeIndex = courseCodes[nameIndex]
    
    courseInfo[codeIndex][0] = newUnits
    
def viewAllCourses():
    print('List of All Courses\n')

    for index in range(len(courseList)):
        courseName = courseList[index]
        courseCode = courseCodes[courseName]
        units = courseInfo[courseCode][0]

        print(str(index + 1) + ' Course: ' + str(courseName))
        print('  Course Code: ' + str(courseCode))
        print('  Units: ' + str(units) + '\n')

def addCourse():
    print('Add New Course\n')

    print('Enter New Course (Enter 0 to return): ', end = '')

    name = input()

    if name != 0:
        #Add to courseLists
        courseList.append(name)
        
        code = ''

        #Check for course code length
        while len(code) != 7:
            print('Enter Course Code (7 Characters): ', end = '')
            code = input()

            if len(code) != 7:
                print('Invalid Course Code.')

        #Add to courseCodes
        courseCodes[name] = code

        #Add to courseInfo
        courseInfo[code] = [0, []]

        units = 0

        while units < 1 or units > 3:
            print('Enter units (1 - 3): ', end = '')
            units = input()
            units = int(units)

            if units < 1 or units > 3:
                print('Invalid Input')

        #Add to courseInfo
        courseInfo[code][0] = units

def deleteCourse():
    print('Delete Course\n')

    viewAllCourses()

    print('Enter index of Course (Enter 0 to return): ', end = '')
    choice = input()

    choice = int(choice)

    if choice != 0:
        #Reduce the index by 1 to match zero indexing format
        choice -= 1

        #Collection of course name and code
        name = courseList[choice]
        code = courseCodes[name]

        #Delete from Course Info
        del courseInfo[code]

        #Delete from Course Codes
        del courseCodes[name]

        #Delete from Course List
        del courseList[choice]

def editCourseInfo():
    print('Edit Course Info')

    viewAllCourses()

    choice = -1
    
    while choice != 0:
        print('Enter index of Course (Enter 0 to return): ', end = '')

        choice = input()

        choice = int(choice)

        while choice != 0:

            choice = int(choice) - 1

            choice2 = -1

            while choice2 != 0:
                print('\nSelect the following to edit:')
                print('1 - Change Name')
                print('2 - Change Course Code')
                print('3 - Change Units')
                print('0 - Back\n')

                print('Enter choice: ', end = '')
                choice2 = input()

                choice2 = int(choice2)

                if choice2 == 1:
                    changeName(choice, courseList, courseCodes)
                elif choice2 == 2:
                    changeID(choice, courseList, courseCodes, courseInfo)
                elif choice2 == 3:
                    changeUnits(choice)
                    

#Student functions
def viewAllStudents():
    print ('List of All Students\n')
    
    for index in range(len(students)):
        studName = students[index]
        studID = idNum[studName]

        print(str(index + 1) + ' Name: ' + str(studName))
        print('  ID Number: '  + str(studID) + "\n")


def addStudent():
    print('Add New Student\n')
    
    print('Enter New Student (Enter 0 to return): ', end = '')

    name = input()

   # trueName = False

   # while not trueName:
   #     for index in range(len(students)):
    #        if name == students[index]:
     #           print('Duplicate Name.')
      #          print('Enter New Student (Enter 0 to return): ', end = '')
       #         name = input()
        #if index >= len(students):
         #   trueName = True
          #  print('g')
        
    if name != '0':

        #Add to students List
        students.append(name)
        
        newID = ''

        #Checking that the ID Number is exactly 8 integers
        while len(newID) != 8:
            print('Enter Student ID (8 integers): ', end = '')
            newID = input()

            if len(newID) != 8:
                print('Invalid ID Number.')

        #Add to idNum dictionary
        idNum[name] = newID

        #Creates an empty list of courses for the student
        studCourses[newID] = []

def deleteStudent():
    print('Delete Student\n')
    
    viewAllStudents()

    print('Enter index of Student (Enter 0 to return): ', end = '')
    choice = input()

    choice = int(choice)

    if choice != 0:
        #Reduce the index by 1 to match zero indexing format
        choice -= 1

        #Collection of Student Name and ID for deletion
        name = students[choice]
        ID = idNum[name]

        #Delete from StudCourses
        del studCourses[ID]

        #Delete from IdNum
        del idNum[name]

        #Delete from Students
        del students[choice]

def editStudentInfo():
    print('Edit Student Info')

    viewAllStudents()

    choice = -1
    
    while choice != 0:
        print('Enter index of Student (Enter 0 to return): ', end = '')

        choice = input()

        choice = int(choice)

        if choice != 0:

            choice -= 1

            choice2 = -1

            while choice2 != 0:
                print('\nSelect the following to edit:')
                print('1 - Change Name')
                print('2 - Change ID Number')
                print('0 - Back\n')

                print('Enter choice: ', end = '')
                choice2 = input()

                choice2 = int(choice2)

                if choice2 == 1:
                    changeName(choice, students, idNum)
                elif choice2 == 2:
                    changeID(choice, students, idNum, studCourses)
                elif choice2 == 0:
                    choice = -1

#Actual Thing

print(studCourses[11500000])

studCourses[11500000].append(['COMPRO1', 0.0])
studCourses[11500000][0][1] = 3.5

print(studCourses[11500000][0])

#studList = courseInfo['COMPRO1']

#print(studList[1])


#courseInfo['COMPRO1'][1].append(11502533)




#courseInfo['COMPRO1'][1].append(11502566)







print('Welcome!!!')

toEdit = -1

while toEdit != 0:
    print('Select category: ')
    print('1 - Students')
    print('2 - Courses')
    print('3 - Enrollment')
    print('4 - Grades')
    print('0 - Exit\n')

    print('Enter choice: ', end = '')

    toEdit = input()

    toEdit = int(toEdit)
        
    if toEdit == 1:
        choice = -1

        while choice != 0:
            print('\nPlease Select one of the following:')
            print('1 - View All Students')
            print('2 - Add Student')
            print('3 - Edit Student Info')
            print('4 - Delete Student')
            print('0 - Exit\n')

            print('Enter choice: ', end = '')
            choice = input()

            choice = int(choice)

            print('\n')
            
            if choice == 1:
                viewAllStudents()
                #os.system('cls')
            elif choice == 2:
                addStudent()
            elif choice == 3:
                editStudentInfo()
            elif choice == 4:
                deleteStudent()
    elif toEdit == 2:
        choice = -1

        while choice != 0:
            print('\nPlease Select one of the following:')
            print('1 - View All Courses')
            print('2 - Add Course')
            print('3 - Edit Course')
            print('4 - Delete Course')
            print('0 - Exit\n')

            print('Enter choice: ', end = '')
            choice = input()

            choice = int(choice)

            print('\n')

            if choice == 1:
                viewAllCourses()
            elif choice == 2:
                addCourse()
            elif choice == 3:
                editCourseInfo()
            elif choice == 4:
                deleteCourse()
    elif toEdit == 3:
        choice = -1

        while choice != 0:
            print('\nPlease Select one of the following:')
            print('1 - Enroll Student in Course')
            print('2 - Drop Student in Course')
            print('3 - View Courses Enrolled by Students')
            print('4 - View Students Enrolled in Courses')
            print('0 - Exit\n')

            print('Enter choice: ', end = '')
            choice = input()

            choice = int(choice)

            print('\n') 
    
            if choice == 1:
                enrollInCourse()
            elif choice == 2:
                dropCourse()
            elif choice == 3:
                viewCoursesEnrolledByStudents()
            elif choice == 4:
                viewStudentsEnrolledInCourses()

    elif toEdit == 4:
        choice -= 1

        while choice != 0:
            print('\nPlease Select one of the following:')
            print('1 - Set Grades')
            print('2 - View Report Cards')
            print('0 - Exit\n')

            print('Enter choice: ', end = '')
            choice = input()

            choice = int(choice)

            print('\n')

            if choice == 1:
                setGrades()
            elif choice == 2:
                viewReportCard()
        
