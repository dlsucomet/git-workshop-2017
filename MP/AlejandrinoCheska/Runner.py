from Grade import*
from Student import *
from Course import *
studentList = []
courseList = []

#courseList = Course ()

def Driver():

    choice = 0

    while (choice != 10):
        print("0 - Add Student" +
              "\n1 - Edit Student Info" +
              "\n2 - Delete Student" +
              "\n3 - Add Course " +
              "\n4 - Edit Course Info" +
              "\n5 - Remove courses" +
              "\n6 - Enroll student in a course" +
              "\n7 - Drop student in a course" +
              "\n8 - Set student's grade"+
              "\n9 - View student's report card"+
              "\n10 - Exit"
              )
        print("Enter number: ")
        choice = int(input())

        if choice == 0:
            add_student()

        elif choice == 1:
            if studentList.__len__() > 0:
                edit_student()
            else:
                print("Student list is empty\n")

        elif choice == 2:
            if studentList.__len__() >0:
                remove_student()
            else:
                print("Student list is empty\n")

        elif choice == 3:
            add_course()

        elif choice == 4:
            if courseList.__len__() > 0:
                editCourse()
            else:
                print("Course list is empty\n")

        elif choice == 5:
            if courseList.__len__() > 0:
                removeCourse()
            else:
                print("Course list is empty\n")

        elif choice == 6:
            if studentList.__len__() > 0:
                if courseList.__len__() > 0:
                    enrollStudent()
                else:
                    print("Course list is empty\n")
            else:
                print("Student list is empty\n")

        elif choice == 7:
            if studentList.__len__() > 0:
                if courseList.__len__() > 0:
                    dropStudent()
                else:
                    print("Course list is empty\n")
            else:
                print("Student list is empty\n")

        elif choice == 8:
            setGrade()

        elif choice == 9:
            viewGrade()

        elif choice == 10:
            break

        else:
            print("Invalid Input! Enter Again")

    return

#Add Student
def add_student():
    print("Enter name of student : ")
    name = raw_input()
    print("Enter ID number: ")
    id = raw_input()
    studentList.append(Student(name, id))
    print("Successfully added new student")
    return

#Print Student List
def print_student_list():
    for i in range(len(studentList)):
        print ("[" + str(i) + "] " + str(studentList[i].print_info()))
    return

#Edit Student
def edit_student():
    print_student_list()
    print("Enter index to edit: ")
    index = int(input())
    edit_student = studentList[index]
    print("Choose an option:\n1. Edit student name\n2. Edit ID number")
    choice = int(input())

    if choice == 1:
        print("Enter new student name: ")
        name = raw_input()
        edit_student.setName(name)

    elif choice == 2:
        print("Enter new ID number: ")
        id = raw_input()
        edit_student.setId(id)

    print("Successfully Edited")
    return

#del Student
def remove_student():
    print_student_list()
    print("Enter index to be removed: ")
    index = int(input())
    remove_student = studentList[index]
    studentList.remove(remove_student)

    print("Successfully Removed")
    return

#add Course
def add_course():
    print("Enter course code: ")
    code = raw_input()
    print("Enter units: ")
    units = float(raw_input())
    courseList.append(Course(code,units))
    print("Successfuly added")
    return

#Print Course List
def print_course_list():
    for i in range(len(courseList)):
        print ("[" + str(i) + "] " + str(courseList[i].print_info()))
    return

#edit CourseInfo
def editCourse():
    print_course_list()
    print("Enter course index to edit: ")
    index = int(input())
    edit_course = courseList[index]

    print("Choose an option\n1. Edit course code\n2. Edit units")
    choice = int(input())

    if choice == 1:
        print("Enter course code: ")
        code = raw_input()
        edit_course.setCode(code)

    elif choice == 2:
        print("Enter units: ")
        units = float(raw_input())
        edit_course.setUnits(units)

    print("Successfully edited")
    return

#remove Course
def removeCourse():
    print_course_list()
    print("Enter index to be removed: ")
    index = int(input())
    remove_course = courseList[index]
    courseList.remove(remove_course)

    print("Successfully Removed")

    return

#enroll Student
def enrollStudent():
    print_student_list()
    print("Enter index of student to be enrolled: ")
    s_index = int(input())

    print_course_list()
    print("Enter index of course to be enrolled by student: ")
    c_index = int(input())

    student = studentList[s_index]
    course = courseList[c_index]

    student.enroll(course)
    course.enrollStudent(student)

    print("Successfully Enrolled")

    return

#drop Student
def dropStudent():
    print_course_list()
    print("Enter index of course: ")
    c_index = int(input())
    course = courseList[c_index]

    print_student_list()
    print("Enter index of student to be removed: ")
    s_index = int(input())
    student = studentList[s_index]

    course.dropStudent(student)
    student.drop(course)

    print("Successfully Dropped")

    return

#Set Student Grade
def setGrade():
    print_course_list()
    print("Enter index of course: ")
    c_index = int(input())
    course = courseList[c_index]

    print_student_list()
    print("Enter index of student to be given a grade: ")
    s_index = int(input())
    student = studentList[s_index]

    print("Enter grade of student: ")
    grade = float(raw_input())

    student.assign_grade(Grade(course, grade))

    return

#view Student Report Card
def viewGrade():
    print_student_list()
    print("Enter index of student to view grade: ")
    s_index = int(input())
    student = studentList[s_index]

    student.see_grade()

    return

Driver()