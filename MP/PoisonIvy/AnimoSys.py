'''
CONSOLE INTERFACE

'''
from Admin import *
admin = Admin()
sysCont = True
while(sysCont):
    print("\n--------------------- WELCOME ---------------------\nLogin as:")
    print("1 - Admin \n2 - Student\n3 - Exit")
    main = int(input("Enter option: "))
    if(main == 1):
        adMenuCont = True
        while(adMenuCont):
            '''
            usrName = input("Enter user name:")
            pw = input("Enter password: ")
            if(usrName == "admin" and pw == "DLSU"):'''
            print("\n********* Admin Menu *********")
            #admin = Admin()
            print("1 - Add Student\n2 - Edit Student\n3 - Delete Student\n4 - Add Course\n5 - Edit Course \n6 - Delete Course\n7 - Open Section\n8 - View Class List\n9 - Set Grade\n10 - Exit")
            adMenu = int(input("Enter option: "))
            
            if(adMenu == 1):
                print("\nADD STUDENT\n-----------------------")
                ID = int(input("Enter ID number: "))
                pw = input("Enter password: ")
                LN = input("Enter last name: ")
                FN = input("Enter first name: ")
                minUnits = float(input("Enter minimum units: "))
                maxUnits = float(input("Enter maximum units: "))
                admin.registerStudent(ID,pw,LN,FN,minUnits,maxUnits)
                
            elif(adMenu == 2):
                print("\nEDIT STUDENT\n-----------------------")
                ID = int(input("Enter ID number: "))
                LN = input("Enter last name: ")
                FN = input("Enter first name: ")
                minU = float(input("Enter minimum units: "))
                maxU = float(input("Enter minimum units: "))
                admin.editStudent(ID,LN,FN,minU,maxU)

            elif(adMenu == 3):
                print("\nDELETE STUDENT\n-----------------------")
                ID = int(input("Enter ID number: "))
                admin.removeStudent(ID)
                
            elif(adMenu == 4):
                print("\nADD COURSE\n-----------------------")
                code = input("Enter course code: ")
                desc = input("Enter course description: ")
                units = float(input("Enter number of units: "))
                admin.addCourse(code, desc,units)
                admin.viewCourses()

            elif(adMenu == 5):
                print("\nEDIT COURSE\n-----------------------")
                orig = input("Enter original course code: ")
                code = input("Enter new course code: ")
                desc = input("Enter new course description: ")
                units = float(input("Enter new number of units: "))
                admin.editCourse(orig,code,desc,units)
                admin.viewCourses()

            elif(adMenu == 6):
                print("\nDELETE COURSE\n-----------------------")
                code = input("Enter course code: ")
                admin.removeCourse(code)
                admin.viewCourses()
                
            elif(adMenu == 7):
                print("\nOPEN SECTION\n-----------------------")
                course = input("Enter course code: ")
                name = input("Enter section: ")
                faculty = input("Enter faculty: ")
                sched = input("Enter day schedule: ")
                start = int(input("Enter start time  (0730 - 1930): "))
                end = int(input("Enter end time (0900 - 2115): "))
                capacity = int(input("Enter capacity: "))
                admin.openSection(name, faculty,sched,start,end,capacity,course)
                
            elif(adMenu == 8):
                print("\nVIEW CLASS LIST\n-----------------------")
                #course = input("Enter course: ")
                #section = input("Enter section:")
                admin.viewClassList()
                
            elif(adMenu == 9):
                print("\nSET GRADE\n-----------------------")
                idNo = int(input("Enter ID number: "))
                course = input("Enter course: ")
                section = input("Enter section: ")
                grade = float(input("Enter grade: "))
                admin.setGrade(section, idNo, grade)

            elif(adMenu == 10):
                adMenuCont = False
            '''
            else:
                print("invalid login credentials.")
            '''
    elif(main == 2):
        stMenuCont = True
        while(stMenuCont):
            
            idNo = int(input("Enter ID number: "))
            pw = input("Enter password: ")
            check = False
            for i in admin.getAllStudents():
                if i.getID() == idNo:
                    student = i
                    check = True
            if(check):
                if student.getPW() != pw:
                    print("Invalid password")
            else:
                print("Student number not registered.")
                stMenuCont = False
                
            if(check and pw == student.getPW()):
                print("\n********* Student Menu *********")
                print("1 - Enlist Class\n2 - Remove Class\n3 - Enroll Courses\n4 - Drop Course\n5 - View EAF\n6 - Exit")
                stMenu = int(input("Enter option: "))

                if(stMenu == 1):
                    print("ENLIST SECTION\n-----------------------")
                    student.setAdmin(admin)
                    course = input("Enter course: ")
                    section = input("Enter section: ")
                    student.enlistSection(course, section)
                    
                    
                elif(stMenu == 2):
                    print("REMOVE SECTION\n-----------------------")
                    course = input("Enter course: ")
                    student.removeSection(course)
                    
                elif(stMenu == 3):
                    print("ENROLL\n-----------------------")
                    student.enroll()
                    
                elif(stMenu == 4):
                    print("DROP COURSE\n-----------------------")
                    course = input("Enter course: ")
                    student.dropCourse(course)
                    
                elif(stMenu == 5):
                    print("VIEW EAF\n-----------------------")
                    print("STUDENT NO. ",str(student.getID()))
                    print("Course\tDescription\tSection\tFaculty\tSchedule\tUnits\tGrade")
                    student.viewEAF()
                    data = student.getData()
                    for row in data:
                        for i in row:
                            print(i, end="\t")
                        print()
                    print("GPA: ",student.getGPA())
                    
                elif(stMenu == 6):
                    stMenuCont = False
                    
    elif(main == 3):
        sysCont = False
        print("Have a nice day!")
        
    
