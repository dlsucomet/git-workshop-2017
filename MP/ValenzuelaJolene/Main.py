from StudentList import *
from Student import *
from CourseList import *
from CourseInfo import *
from CourseGrade import *

#Students
s_list = StudentList ()

#Courses
c_list = CourseList ()

# ---------------
#    MAIN MENU
# ---------------

def main_menu():
    s_list.addStudent(Student("Celina Brito", 11554321))
    c_list.addCourse(CourseInfo("HCIFACE", "3.0"))

    choice = int(0)
    while (choice != 10):
        print("-----------------------------------\n0. Add students\n1. Edit students\n2. Remove students\n" +
        "-----------------------------------\n3. Add courses\n4. Edit courses\n" +
        "5. Remove courses\n-----------------------------------\n6. Enroll a student in a course\n" +
        "7. Drop a student in a course\n-----------------------------------\n" +
        "8. Set students' grade in a course\n9. View student's report card\n" +
        "10. Exit\n-----------------------------------\n")

        print("Enter index to proceed: ")
        choice = input()

        if choice.isnumeric():
            choice = int(choice)
            if choice == 0:
                add_student_menu()
            elif choice == 1:
                if s_list.students.__len__() > 0:
                    edit_student_menu()
                else:
                    print("Student list is empty.")
            elif choice == 2:
                if s_list.students.__len__() > 0:
                    remove_student_menu()
                else:
                    print("Student list is empty.")
            elif choice == 3:
                add_course_menu()
            elif choice == 4:
                if c_list.courseInfo.__len__() > 0:
                    edit_course_menu()
                else:
                    print("Course list is empty.")
            elif choice == 5:
                if c_list.courseInfo.__len__() > 0:
                    remove_course_menu()
                else:
                    print("Course list is empty.")
            elif choice == 6:
                if s_list.students.__len__() > 0:
                    if c_list.courseInfo.__len__() > 0:
                        enroll_student_menu()
                    else:
                        print("Course list is empty.")
                else:
                    print("Student list is empty.")
            elif choice == 7:
                if s_list.students.__len__() > 0:
                    if c_list.courseInfo.__len__() > 0:
                        drop_student_menu()
                    else:
                        print("Course list is empty.")
                else:
                    print("Student list is empty.")
            elif choice == 8:
                set_grades_menu()
            elif choice == 9:
                view_grades_menu()
            elif choice == 10:
                break
            else:
                print("Input " + str(choice) + " is not valid. Please try again.")
        else:
            print("Input " + choice + " is not valid. Please try again.")

    return

# ---------------
#   ADD STUDENT
# ---------------

def add_student_menu():
	try:
		print("Enter student name: ")
		name = input()
		print("Enter ID number: ")
		id = input()
		if id.isnumeric() and len(id) == 8:
			s_list.addStudent (Student(name, id))
			print(str(Student(name, id)) + " added to student list.")
	except:
		print("invalid student info")
	return

# ---------------
#   EDIT STUDENT
# ---------------

# No error-checking yet for non-numeric input / out-of-bounds
def edit_student_menu():
	try:
		s_list.printStudents()
		print("Enter student index to edit: ")
		index = input()
		currStudent = s_list.getStudent(int(index))

		print("1. Edit student name\n2. Edit ID number")
		choice = input()
		choice = int(choice)
			
		if choice == 1:
			print("Enter student name: ")
			name = input()
			currStudent.setName(name)

		elif choice == 2:
			print("Enter ID number: ")
			id = input()
			id = int(id)
			currStudent.setId(id)

		print("Edited to" + str(currStudent) + ".")
	except:
		print ("invalid input")
	return

# ----------------
#  REMOVE STUDENT
# ----------------

# No error-checking yet for non-numeric input / out-of-bounds
def remove_student_menu():
	try:
		s_list.printStudents()
		print("Enter student index to remove: ")
		index = input()
		currStudent = s_list.getStudent(int(index))
		s_list.removeStudent(currStudent)
		print(str(currStudent) + " removed from student list.")
	except:
		print ("invalid input")
	return

# ---------------
#   ADD COURSE
# ---------------

# No error-checking yet for:
#   1. Not 7-char alphanumeric/hyphenated course code
#   2. Units other than 0.0 - 4.0

def add_course_menu():
	try:
		print("Enter course code: ")
		code = input()
		print("Enter units: ")
		units = input()
		c_list.addCourse(CourseInfo(code, units))
		print(str(CourseInfo(code, units)) + " added to course list.")
	except:
		print ("invalid input")
	return

# ---------------
#   EDIT COURSE
# ---------------

# No error-checking yet for non-numeric input / out-of-bounds

def edit_course_menu():
	try:
		c_list.printCourses()
		print("Enter course index to edit: ")
		index = input()
		currCourse = c_list.getCourse(int(index))
		print("1. Edit course code\n2. Edit units")
		choice = input()
		choice = int(choice)

		if choice == 1:
			print("Enter course code: ")
			code = input()
			currCourse.setCode(code)

		elif choice == 2:
			print("Enter units: ")
			units = input()
			units = float(units)
			currCourse.setUnits(units)

		print("Edited to" + str(currCourse) + ".")
	except:
		print ("invalid input")
	return

# ---------------
#  REMOVE COURSE
# ---------------

# No error-checking yet for non-numeric input / out-of-bounds
def remove_course_menu():
	try:
		c_list.printCourses()
		print("Enter course index to remove: ")
		index = input()
		currCourse = c_list.getCourse(int(index))
		for i in range(len(currCourse.getStudents())):
			try:
				if currCourse.getStudents()[i].getCoursesGrades()[currCourse.getStudents()[i].getCoursesGrades().index(currCourse)].getGrade() == "NGS":
					currCourse.getStudents()[i].removeEnrolledCourse(currCourse)
			except:
				pass
		c_list.removeCourse(currCourse)
		print(str(currCourse) + " removed from course list.")
	except:
		print ("invalid input")
	return

# ----------------
#  ENROLL STUDENT
# ----------------

def enroll_student_menu():
	try:
		s_list.printStudents()
		print("Enter student index to enroll: ")
		student_index = input()
		c_list.printCourses()
		print("Enter course index to enroll: ")
		course_index = input()

		s_list.students[int(student_index)].addEnrolledCourse(c_list.courseInfo[int(course_index)])
	except:
		print ("invalid input")
	return

# ---------------
#  DROP STUDENT
# ---------------

def drop_student_menu():
	try:
		s_list.printStudents()
		print("Enter student index to drop: ")
		student_index = input()
		c_list.printCourses()
		print("Enter course index to drop: ")
		course_index = input()

		s_list.students[int(student_index)].removeEnrolledCourse(c_list.courseInfo[int(course_index)])
	except:
		print ("invalid input")
	return

# --------------
#   SET GRADES
# --------------

    #course = s_list.students[int(student_index)].getCourses()
    #print(len(course))
def set_grades_menu():
	# Choose student from list
	if len(c_list.courseInfo) <= 0:
		print("Course list is empty.")
		return

	try:
		c_list.printCourses()
		course_index = input()
		currCourse = c_list.courseInfo[int(course_index)]

		print("\n" + str(currCourse.code) + "(" + str(currCourse.units) + ")" + " Students: ")
		enrolledStudents = currCourse.getStudents()
		for i in range(len(enrolledStudents)):
			print("[" + str(i) + "] " + enrolledStudents[i].__str__())

		print("Enter student index: ")
		student_index = input()
		currStudent = enrolledStudents[int(student_index)]

		#Enter grade
		print("Enter grade: ")
		grade = input()

		currStudent.setCourseGrade (currCourse, grade)
	except:
		print ("invalid input")
	return

# ---------------
#   VIEW CARD
# ---------------

def view_grades_menu():
	# Choose student from list
	try:
		s_list.printStudents()
		print("Enter student index: ")
		student_index = input()
		currStudent = s_list.getStudent(int(student_index))
		currStudent.printGPA()
	except:
		print ("invalid input")

	return


main_menu()

