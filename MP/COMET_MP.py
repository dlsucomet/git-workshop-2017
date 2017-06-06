#BASIC >> ALGORITHM #Di ko na save ung nagawa ko na maayos so sad life :(
#Prepared by: John Edel B. Tamani ,11544376
from time import gmtime, strftime
class Student:
    def __init__(self,name,ID):
        self.enlistedCourses = []
        self.enlistedGrades = []
        self.full_name = name
        self.id_number = ID
        
    def Enroll_Course(self,student):
        print("\nList of All Available Courses! \nCourse Name     Course ID")
        for i in range(0,len(Courses)):
            print(Courses[i].Get_CourseName() , "       " , Courses[i].Get_CourseID())
        user_input = int(input("\nEnter Course ID:"))
        for i in range(0,len(Courses)):
            if(user_input == Courses[i].Get_CourseID()):
                Courses[i].Add_Student(student)
                self.enlistedCourses.append(Courses[i])
                self.enlistedGrades.append(0)
                print("COURSE SUCCESSFULLY ENROLLED!")
                
    def Drop_Course(self,student):
        print("\nList of All Enrolled Courses! \nCourse Name     Course ID")
        for i in range(0,len(self.enlistedCourses)):
            print(self.enlistedCourses[i].Get_CourseName() , "       " , self.enlistedCourses[i].Get_CourseID())
        user_input = int(input("\nEnter Course ID:"))
        for i in range(0,len(self.enlistedCourses)):
            if(user_input == self.enlistedCourses[i].Get_CourseID()):
                self.enlistedCourses[i].Remove_Student(student)
                del self.enlistedCourses[i]
                del self.enlistedGrades[i]
                print("COURSE SUCCESSFULLY DROPPED!")
                
    def View_ReportCard(self):
        print("\nList of All Enrolled Courses! \nCourse Name     Course Grade")
        currentGPA = 0
        courses = 0
        for i in range(0,len(self.enlistedCourses)):
            currentGPA = currentGPA + self.enlistedGrades[i]
            courses = courses + 1
            print(self.enlistedCourses[i].Get_CourseName() , "       " , self.enlistedGrades[i])
        print("\nSTUDENT GPA:" , currentGPA/courses)
        
    def Set_Grade(self,student):
        print("\nList of All Enrolled Courses! \nCourse Name     Course ID")
        for i in range(0,len(self.enlistedCourses)):
            print(self.enlistedCourses[i].Get_CourseName() , "       " , self.enlistedCourses[i].Get_CourseID())
        user_input = int(input("\nEnter Course ID:"))
        for i in range(0,len(self.enlistedCourses)):
            if(user_input == self.enlistedCourses[i].Get_CourseID()):
                user_input = float(input("Enter Course Grade:"))
                self.enlistedGrades[i] = user_input
                self.enlistedCourses[i].Get_Grade(student,self.enlistedGrades[i])
                print("COURSE SUCCESSFULLY GRADED!")
    
    def Set_FullName(self):
        self.full_name = str(input("Enter new name:"))
        
    def Get_FullName(self):
        return self.full_name
    
    def Set_ID(self):
        self.id_number = int(input("Enter new ID number:"))
        
    def Get_ID(self):
        return self.id_number

class Course:
    def __init__(self, name, unit, ID):
        self.studentsEnrolled = []
        self.studentsGrade = []
        self.course_name = name
        self.course_unit = unit
        self.course_ID = ID
    
    def Add_Student(self,student):
        self.studentsEnrolled.append(student)
        self.studentsGrade.append(0)
        
    def Get_Grade(self,student,grade):
        for i in range(0,len(self.studentsEnrolled)):
            if(self.studentsEnrolled[i].Get_ID() == student.Get_ID()):
                self.studentsGrade = grade
    
    def Remove_Student(self,student):
        for i in range(0,len(self.studentsEnrolled)):
            if(self.studentsEnrolled[i].Get_ID() == student.Get_ID()):
                del self.studentsEnrolled[i]
                del self.studentsGrade[i]

    def Show_Top(self):
        for i in range(0,len(studentsEnrolled)):
            print(studentsEnrolled[i].Get_Name(),studentsGrade[i])
            
    def Set_CourseName(self):
        self.course_name = input("Enter a new course name:")
        
    def Get_CourseName(self):
        return self.course_name

    def Set_CourseUnit(self):
        self.course_unit = input("Enter a new course unit:")
        
    def Get_CourseUnit(self):
        return self.course_unit
    
    def Set_CourseID(self):
        self.course_ID = input("Enter a new course ID:")
        
    def Get_CourseID(self):
        return self.course_ID
   
def Add_Student():
    user_input = str(input("Enter Full Name:"))
    user_input2 = int(input("Enter ID number:"))
    new_student = Student(user_input, user_input2)
    Students.append(new_student)
    print("NEW STUDENT SUCCESSFULLY ADDED!")
    
def Add_Course():
    user_input = str(input("Enter Course Name:"))
    user_input2 = int(input("Enter Course Unit:"))
    user_input3 = int(input("Enter Course ID:"))
    new_course = Course(user_input, user_input2, user_input3)
    Courses.append(new_course)
    print("NEW COURSE SUCCESSFULLY ADDED!")

def Delete_Student():
    user_input = int(input("Enter ID Number:"))
    for i in range(0,len(Students)):
        if(user_input == Students[i].Get_ID()):
            del Students[i]
            print("STUDENT HAS BEEN SUCCESSFULLY DELETED!")
            
def Delete_Course():
    user_input = str(input("Enter Course Name:"))
    for i in range(0,len(Courses)):
        if(user_input == Courses[i].Get_CourseName()):
            del Courses[i]
            print("COURSE HAS BEEN SUCCESSFULLY DELETED!")
           
def Edit_Student():
    user_input = int(input("Enter ID Number:")) 
    for i in range(0,len(Students)):
        if(user_input == Students[i].Get_ID()):
            print("Previous Name:", Students[i].Get_FullName())
            print("Previous ID:", Students[i].Get_ID())
            Students[i].Set_FullName()
            Students[i].Set_ID()
            print("UPATED Name:", Students[i].Get_FullName())
            print("UPATED ID:", Students[i].Get_ID())
            print("STUDENT HAS BEEN SUCCESSFULLY EDITED!")
    
def Edit_Course():
    user_input = str(input("Enter Course Name:"))
    for i in range(0,len(Courses)):
        if(user_input == Courses[i].Get_CourseName()):
            print("Previous Name:", Courses[i].Get_CourseName())
            print("Previous ID:", Courses[i].Get_CourseID())
            print("Previous Unit:", Courses[i].Get_CourseUnit())
            Courses[i].Set_CourseName()
            Courses[i].Set_CourseID()
            Courses[i].Set_CourseUnit()
            print("UPATED Name:", Courses[i].Get_CourseName())
            print("UPATED ID:", Courses[i].Get_CourseID())
            print("UPATED Unit:", Courses[i].Get_CourseUnit())
            print("COURSE HAS BEEN SUCCESSFULLY EDITED!")
    
def Print_Only():
    print("============================================\nBASIC JET TAMANI SCHOOL MANAGEMENT SYSTEM \n")
    print("CURRENT TIME: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())) 
    print("\n*To Terminate the program, type POGIniJET \n ")
    print("Student Setup: \n [1] Add Student \n [2] Edit Student Information \n [3] Delete Student \n")
    print("Course Setup: \n [4] Add Course \n [5] Edit Course Information \n [6] Delete Course \n")
    print("Student Services: \n [7] Enroll Course \n [8] Drop Course \n [9] Set Course Grade  \n [10]View Report Card \n")

Students = []
Courses = []

while(True):
    Print_Only()
    user_input = input("ENTER A NUMBER:")
        
    if(user_input == "1"):
        Add_Student()
      
    elif(user_input == "2"):
        Edit_Student()
        
    elif(user_input == "3"):
       Delete_Student()
        
    elif(user_input == "4"):
        Add_Course()
        
    elif(user_input == "5"):
        Edit_Course()
				   
    elif(user_input == "6"):
        Delete_Course()
        
    elif(user_input == "7"):
        user_input = int(input("Enter ID Number:"))
        for i in range(0,len(Students)):
            if(user_input == Students[i].Get_ID()):
                Students[i].Enroll_Course(Students[i])
    
    elif(user_input == "8"):
        user_input = int(input("Enter ID Number:"))
        for i in range(0,len(Students)):
            if(user_input == Students[i].Get_ID()):
                Students[i].Drop_Course(Students[i])
        
    elif(user_input == "9"):
        user_input = int(input("Enter ID Number:"))
        for i in range(0,len(Students)):
            if(user_input == Students[i].Get_ID()):
                Students[i].Set_Grade(Students[i])
       	 
    elif(user_input == "10"):
        user_input = int(input("Enter ID Number:"))
        for i in range(0,len(Students)):
            if(user_input == Students[i].Get_ID()):
                Students[i].View_ReportCard()
          
    elif(user_input == "POGIsiJET"):
        print("Thank you for using JET School Management System! Come Again! Comet MP Mo to! :) Add Me on Facebook: John Edel B. Tamani!")
        break
    
    else:
        print("Error Invalid Input!")
