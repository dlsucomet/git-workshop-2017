from Courses import Courses
from StudentMenus import StudentMenus

class CourseMenus:
    def GPE(usrData):
        if usrData < 60 :
            print("0.0")
        elif usrData >= 60 and usrData < 66 :
            print("1.0")
        elif usrData >= 66 and usrData < 72 :
            print("1.5")
        elif usrData >= 72 and usrData < 78 :
            print("2.0")
        elif usrData >= 78 and usrData < 83 :
            print("2.5")
        elif usrData >= 83 and usrData < 89 :
            print("3.0")
        elif usrData >= 89 and usrData < 94 :
            print("3.5")
        elif usrData >= 94 :
            print("4.0")
            
    def readFile():
        courseList = []
        
        file = open("courses.txt", "r")

        i = -1
        
        for line in file:
            if (line[0: line.find(">")] == "Course"):
                course = Courses(line[line.find(">") + 1: line.find(":")],
                                 line[line.find(":") + 1: line.find("=")],
                                 line[line.find("=") + 1: line.find("\n")])
                courseList.append(course)
                i += 1
            else:
                courseList[i].addStudent(line[line.find(",") + 1: line.find("=")], line[0: line.find(",")])
                courseList[i].setGrades(line[line.find("=") + 1: line.find("\n")], line[0: line.find(",")]) 

        for i in range(len(courseList)):
            print (courseList[i].getName())

        file.close()            

        return courseList
        
    def wcourseStudents(courses):
        courseList = courses
        file = open("courses.txt", "w")

        for i in range(len(courseList)):
            file.write("Course>" + courseList[i].getName())
            file.write(":" + courseList[i].getDescription())
            file.write("=" + courseList[i].getUnits())
            file.write("\n")
            studentList = courseList[i].getList()
            gradesList = courseList[i].getGrades()
            
            for val in studentList:
                file.write(val)
                file.write(",")
                file.write(studentList[val])
                file.write("=")
                try:
                    file.write(gradesList[val])
                except Exception:
                    pass
                file.write("\n")

        file.close()
        
    def addCourses():
        courseCode = input("\nEnter course code: ")
        description = input("Enter course description: ")
        units = input("Enter course units: ")

        if (len(courseCode) == 7):
            file = open("courses.txt", "a")

            file.write("Course>" + courseCode)
            file.write(":" + description)
            file.write("=" + units)
            file.write("\n")
                        
            file.close()

        usrData = input("Add another course? (Y/N) ")

        if (usrData.upper() != "N"):
            CourseMenus.addCourses()
            
    def editCourses():
        courseList = CourseMenus.readFile()
        code = input("Enter course code: ")

        for i in range(len(courseList)):
            if (courseList[i].getName() == code):
                code = input("Enter new course code: ")           
                courseList[i].setCourseCode(code)
                description = input("Enter new description: ")           
                courseList[i].setDescription(description)
                units = input("Enter new # of units: ")           
                courseList[i].setUnits(units)

        CourseMenus.wcourseStudents(courseList)

        usrData = input("Edit another course? (Y/N) ")

        if (usrData.upper() != "N"):
            CourseMenus.editCourses()


    def deleteCourses():
        courseList = CourseMenus.readFile()
        code = input("Enter course code: ")

        for i in range(len(courseList)):
            if (courseList[i].getName() == code):
                del courseList[i]
                break    

        CourseMenus.wcourseStudents(courseList)

        usrData = input("Delete another course? (Y/N) ")

        if (usrData.upper() != "N"):
            CourseMenus.deleteCourses()

    def enrollStudent():
        courseList = CourseMenus.readFile()
        studentList = StudentMenus.readStudents()

        studentID = input("Enter student ID: ")
        courseCode = input("Enter course code: ")
        
        for i in range(len(courseList)):
            if (courseList[i].getName() == courseCode):
                for val in studentList:
                    if (val == studentID):
                        j = 0
                        
                        for val2 in courseList[i].getList():
                            if (studentID == val2):
                                break
                            j += 1

                        if (j == len(courseList[i].getList())):
                            courseList[i].addStudent(studentList[val], studentID)
                        else:
                            print ("Already enrolled")
                            
        CourseMenus.wcourseStudents(courseList)

        usrData = input("Enroll another student? (Y/N) ")

        if (usrData.upper() != "N"):
            CourseMenus.enrollStudent()
            
    def dropStudent():
        courseList = CourseMenus.readFile()
        
        studentID = input("Enter student ID: ")
        courseCode = input("Enter course code: ")
        
        for i in range(len(courseList)):
            if (courseList[i].getName() == courseCode):
                studentList = courseList[i].getList()
                j = 0
                
                for val in studentList:
                    if (val == studentID):
                        break
                    j += 1
                        
                if (j != len(studentList)):
                    courseList[i].dropStudent(studentList[val], studentID)
                else:
                    print ("Student does not exist in this class")
                
        CourseMenus.wcourseStudents(courseList)

        usrData = input("Drop another student? (Y/N) ")

        if (usrData.upper() != "N"):
            CourseMenus.dropStudent()

    def studentGrade():
        courseList = CourseMenus.readFile()

        studentID = input("Enter student ID: ")
        courseCode = input("Enter course code: ")

        for i in range(len(courseList)):
            if (courseList[i].getName() == courseCode):
                studentList = courseList[i].getList()
                gradesList = courseList[i].getGrades()
                
                for val in studentList:
                    if (val == studentID):
                        grade = input("Enter student grade: ")
                        courseList[i].setGrades(grade, studentID)
                        break
                    
        CourseMenus.wcourseStudents(courseList)

        usrData = input("Edit another grade? (Y/N) ")

        if (usrData.upper() != "N"):
            CourseMenus.studentGrade()
            
    def viewCard():
        courseList = CourseMenus.readFile()

        studentID = input("Enter student ID: ")

        print ("Courses  Grade  GPA")
        
        for i in range(len(courseList)):
            studentList = courseList[i].getList()
            gradesList = courseList[i].getGrades()

            for val in studentList:
                if (val == studentID):
                    print (courseList[i].getName() + "     ", end = "")
                    print (gradesList[val] + "  ", end = "")
                    CourseMenus.GPE(int(gradesList[val]))
                    break
            
    def topStudents():
        courseList = CourseMenus.readFile()

        course = input("Enter course: ")

        print ("Grade  StudentID  StudentName")
        
        for i in range(len(courseList)):
            if (courseList[i].getName() == course):
                studentList = courseList[i].getList()
                gradesList = courseList[i].getGrades()
                sortedList = {}
                sortedKey = sorted(gradesList)
                sortedVal = sorted(gradesList.values())
                topGrades = {}

                for val in sortedKey:
                    for val2 in gradesList:
                        if (val == val2):
                            sortedList[val] = gradesList[val]
                            break
                
                for val in sortedVal:
                    if (len(topGrades) < 5):
                        for val2 in sortedList:
                            if (sortedList[val2] == val):
                                topGrades[val2] = val
                                del sortedList[val2]
                                break
                break


        for val in topGrades:
            for val2 in studentList:
                if (val == val2):
                    print ("   " + topGrades[val], end = "")
                    print ("   " + val, end = "")
                    print ("  " + studentList[val])
                    break
