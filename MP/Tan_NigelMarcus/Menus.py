#Run this file

from CourseMenus import CourseMenus
from StudentMenus import StudentMenus

class Menus:
    def students():  
        print ("\nAdd students      (1)")
        print ("Edit students     (2)")
        print ("Delete students   (3)")
        print ("Back to main menu (4)")
        usrData = int(input("Enter number: "))
        
        if (usrData == 1):
            StudentMenus.addStudents()
        elif (usrData == 2):
            StudentMenus.editStudents()
        elif (usrData == 3):
            StudentMenus.deleteStudents()
        if (usrData != 4):
            Menus.students()

    def courses():  
        print ("\nAdd course          (1)")
        print ("Edit course info    (2)")
        print ("Delete courses      (3)")
        print ("Enroll student      (4)")
        print ("Drop student        (5)")
        print ("Set students' grade (6)")
        print ("View student card   (7)")
        print ("View top 5 studnts  (8)")
        print ("Back to main menu   (9)")
        usrData = int(input("Enter number: "))
            
        if (usrData == 1):
            CourseMenus.addCourses()
        elif (usrData == 2):
            CourseMenus.editCourses()
        elif (usrData == 3):
            CourseMenus.deleteCourses()
        elif (usrData == 4):
            CourseMenus.enrollStudent()
        elif (usrData == 5):
            CourseMenus.dropStudent()
        elif (usrData == 6):
            CourseMenus.studentGrade()
        elif (usrData == 7):
            CourseMenus.viewCard()
        elif (usrData == 8):
            CourseMenus.topStudents()
        if (usrData != 9):
            Menus.courses()

    def mainMenu():
        print ("\nStudents (1)")
        print ("Courses  (2)")
        print ("Exit     (3)")
        usrData = int(input("Enter number: "))
        
        if (usrData == 1):
            Menus.students()
        elif (usrData == 2):
            Menus.courses()
        if (usrData != 3):
            Menus.mainMenu()

Menus.mainMenu()
