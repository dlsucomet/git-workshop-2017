from student import Student
from course import Course



#Functions
#-----------------------------------------------

#Just prints
def displayOption():
    print("(1)Student option")
    print("(2)Course option")
    print("(3)Enrollment")
    print("(4)Grading/Academic option")
    print("(5)Exit")
    print("Choose your action: ", end="")


#Prints the list of students added
def displayStudentList():
    x = 1;
    if len(student_list) is not 0:
        print("Student#: Name ; ID Number")
        for std in student_list:
            print("%d: %s ; %d" %(x, std.getName(), std.getIdNum()))
            x += 1
    else:
        print("No students available.")

#Contains all action for the student option              
def studentOption():
    name = None
    idNum = None
    choice = None
    studentChoice = None
    
    print("\n\n*Student Option*")

    print("(1)Add students")
    print("(2)Edit students")
    print("(3)Delete Students")
    print("(4)Display Students")
    print("(5)Back")
    print("Choose your action: ", end="")
    choice = int(input())
  

    #Add students
    if choice is 1:
        print("Enter name:  ", end="")
        name = input()
        print("Enter Id Number: ", end="")
        idNum = int(input())
        student_list.append(Student(name, idNum))
        print("Successfully added %s!" %(name))

    #Edit student info
    elif choice is 2:
              
        displayStudentList()
        if len(student_list) is not 0:
            print("Choose student (through their number): ", end="")
            studentChoice = int(input())

            print("What shall we do: ")
            print("(1) Edit name.")
            print("(2) Edit IdNum.")
            choice = int(input())

            if choice is 1:
                print("Enter new name: ", end="")
                name = input()
                print("Before: %s" % (student_list[studentChoice-1].getName()))
                student_list[studentChoice-1].setName(name)
                print("After: %s" %(name))
            elif choice is 2:
                print("Enter ID Number: ", end="")
                idNum = int(input())
                print("Before: %d" % (student_list[studentChoice-1].getIdNum()))
                student_list[studentChoice-1].setIdNum(idNum)
                print("After: %d" %(IdNum))
            else:
                print("Input was not a part of the given choices.")
                
    elif choice is 3:
        displayStudentList()
        if len(student_list) is not 0:
            print("Choose student (through their number): ", end="")
            studentChoice = int(input())
            del student_list[studentChoice-1]
              
        
    elif choice is 4:
        displayStudentList()
              
    elif choice is 5:
        print("going back...\n")

    else:
        print("invalid choice.")

#Displays the added courses
def displayCourseList():
    x = 1
    if len(course_list) is not 0:
        print("Course#: Code ; units")
        for i in course_list:
            print("%d: %s ; %.1f" % (x, i.getCourseCode(), i.getUnits()))
            x = x + 1
    else:
        print("There are no courses available.")
    

#Everything regarding the course option is in here
def courseOption():
    code = None
    units = None
    choice = None
    courseChoice = None
    
    print("\n\n*Course option*")
    print("(1)Add Course")
    print("(2)Edit Course")
    print("(3)Delete Course")
    print("(4)Display Course list")
    print("(5)back")
    print("What shall we do: ", end="")
    choice = int(input())

    #Add course
    if choice is 1:
        print("Enter Course code:  ", end="")
        code = input()
        print("Enter Units: ", end="")
        units = float(input())
        course_list.append(Course(code, units));

    #Edit course info
    elif choice is 2:
        displayCourseList()
        if len(course_list) is not 0:
            print("Choose course (through their number): ", end="")
            courseChoice = int(input())

            print("What shall we do: ")
            print("(1) Edit code.")
            print("(2) Edit units.")
            choice = int(input())

            if choice is 1:
                print("Enter new code: ", end="")
                code = input()
                print("Old course code: %s" %(course_list[courseChoice-1].getCourseCode()))
                course_list[courseChoice-1].setCode(code)
                print("New course code: %s" %(code))
                
                
            elif choice is 2:
                print("Enter new units: ", end="")
                units = float(input())
                print("Old units: %.1f" %(course_list[courseChoice-1].getUnits()))
                course_list[courseChoice-1].setUnits(units)
                print("New units: %.1f" %(units))
            else:
                print("Input was not among the choices.")
            
    elif choice is 3:
        displayCourseList()
        if len(course_list) is not 0:
            print("Choose course (through their number): ", end="")
            courseChoice = int(input())
            del course_list[courseChoice-1]
            
            
    elif choice is 4:
        displayCourseList()
              
    elif choice is 5:
        print("going back...\n")

    else:
        print("invalid choice")


def enrollmentOption():
    studentChoice = None
    courseChoice = None
    tempCourseList = []
    
    if len(student_list) is not 0 and len(course_list) is not 0:
        print("\n\n*Enrollment option*")
        print("(1) Enroll Student")
        print("(2) Drop Student")
        print("What is your desire?: ", end="")
        choice = int(input())

        displayStudentList()
        print("Choose a student: ", end="")
        studentChoice = int(input())


        if choice is 1:
            displayCourseList()
            print("Choose course to add(by number): ")
            courseChoice = int(input())
            student_list[studentChoice-1].enlistACourse(course_list[courseChoice-1].getCourseCode(), course_list[courseChoice-1])
            

        elif choice is 2:
            print("\nStudent's Courses:")
            student_list[studentChoice-1].displayCoursesEnrolled()

            if student_list[studentChoice-1].getCourseCount() is not 0: 
                print("Select course to drop (By name): ", end="");
                courseChoice = input()
                student_list[studentChoice-1].dropCourse(courseChoice)

        elif choice is 3:
            student_list[studentChoice-1].displayCoursesEnrolled()
            
        else:
            print("Choice not even in range.")

    else:
        print("\n\nThere aren't enough students or courses available.")
    

def gradeOption():
    action = None
    studentChoice = None
    grade = None
    
    print("\n\n*Grade Option*")
    print("(1) Set a grade on a Student's course")
    print("(2) View report card")
    print("Choose action: ", end="")
    action = int(input())

    displayStudentList()
    print("Choose a student: ", end="")
    studentChoice = int(input())
    
    if action is 1:
        student_list[studentChoice-1].displayCoursesEnrolled()

        if student_list[studentChoice-1].getCourseCount() is not 0:
            print("Select course (by name): ", end="");
            courseChoice = input()
            print("Enter grade: ")
            grade = input()
            student_list[studentChoice-1].addGrade(courseChoice, grade)

    elif action is 2:
        print("\n\n%s's Report card: " % (student_list[studentChoice-1].getName()))
        student_list[studentChoice-1].viewReportCard()
    else:
        print("Chosen action is not among the choices.")

#----------------------------------------------------

#Variables
#----------------------------------------------------
out = False
option = None

student_list = [] 
course_list = [] 
option_dict = {1:studentOption,
               2:courseOption,
               3:enrollmentOption,
               4:gradeOption}
#----------------------------------------------------

#Where the code really starts:
print("Welcome to University 101!")

while(out is False):
    displayOption()

    #check if valid option was chosen
    option = int(input())

    if 1 <= option <= 5:
        
        #Proceed with the desired option
        if(option != 5):
            option_dict[option]()
        else:
            out = True

    else:
        print("Wrong option")

    print("\n\n")

print("GoodBye!")
