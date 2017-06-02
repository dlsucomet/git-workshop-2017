from classes import *


def is_match_student(idnum):
	for y in students:
		if y.get_id() == idnum:
			return True
	return False

def find_student(idnum):
	for y in students:
		if y.get_id() == idnum:
			return y
	return None

def print_students():
	print("ID#\t\tName")
	for y in students:
		print(y.get_student_info())
	print()


def is_match_course(ccode):
	for y in courses:
		if y.get_ccode() == ccode:
			return True
	return False

def find_course(ccode):
	for y in courses:
		if y.get_ccode() == ccode:
			return y
	return None

def print_courses():
	print("Course Code \tUnits")
	for y in courses:
		print(y.get_course_info())
	print()


students = []
courses = []

cont = True

while cont:
	print("Enter number of choice")
	print("1. Add Student\n2. Edit Student Info\n3. Delete Student\n4. See Student List\n5. Add Course")
	print("6. Edit Course Info\n7. Delete Course\n8. View Course List\n9. Enroll Student\n10. Drop Student")
	print("11. See Students in a Course\n12. See Courses of a Student\n13. Set Grade\n14. See Report Card\n15. Exit")
	x = input(">")
	if x == "15":
		cont = False
	else:
		#Add student
		if x == "1":
			name = input("Name: ")
			idnum = input("ID#: ")
			while len(idnum) != 8:
				idnum = input("ID#: ")
			if not is_match_student(idnum):
				students.append(student(name, idnum))
				print("Student added\n")
			else: 
				print("ID# exists already\n")

		#Edit student info
		elif x == "2":
			idnum = input("Enter ID#: ")
			success = False
			y = find_student(idnum)
			if y != None:
				new_name = input("Enter new name: ")
				y.change_name(new_name)
				print("Name changed\n")
				success = True
			if not success:
				print("Student does not exist\n")

		#Delete student
		elif x == "3":
			idnum = input("Enter ID#: ")
			success = False
			y = find_student(idnum)
			if y != None:
				students.remove(y)
				success = True
				print("Student Deleted\n")

			if not success:
				print("Student does not exist\n")

		#View student list
		elif x == "4":
			print_students()

		#Add course
		elif x == "5":
			ccode = ""
			while len(ccode) != 7:
				ccode = input("Enter Course Code: ")
			ccode = ccode.upper()

			if not is_match_course(ccode):
				units = float(input("Enter # of Units (0-4, 5 - floating): "))

				courses.append(course(ccode, units))
				print("Course Added\n")
			else:
				print("Course already exists\n")

		#Edit course info
		elif x == "6":
			ccode = input("Enter Course Code: ")
			ccode = ccode.upper()
			success = False
			y = find_course(ccode)
			if y != None:
				choice = input("1 - Change Code, 2 - Change Units: ")
				if choice == "1":
					new_ccode = ""
					while len(new_ccode) != 7:
						new_ccode = input("Enter Course Code: ")
					new_ccode = new_ccode.upper()				
					if not is_match_course(new_ccode):
						y.change_ccode(new_ccode)
						success = True
						print("Course Code Changed\n")
				elif choice == "2":
					new_units = float(input("Enter # of Units (0-4, 5 - floating): "))
					y.change_units(new_units)
					success = True
					print("Units Changed\n")

			if not success:
				print("Course not found or course already exists\n")

		#Remove course
		elif x == "7":
			ccode = input("Enter Course Code: ")
			ccode = ccode.upper()
			success = False
			y = find_course(ccode)
			if y != None:
				courses.remove(y)
				success = True
				print("Course Deleted\n")

			if not success:
				print("Course does not exist\n")

		#View course list
		elif x == "8":
			print_courses()

		#Enroll student	
		elif x == "9":
			print_students()
			print_courses()
			if len(students) != 0 and len(courses) != 0:
				idnum = input("Enter ID#: ")
				studEnroll = find_student(idnum)
				if studEnroll != None:
					ccode = input("Enter course: ")
					ccode = ccode.upper()
					courseEnroll = find_course(ccode)
					if courseEnroll != None and not studEnroll.find_course(courseEnroll):
						studEnroll.add_course(courseEnroll)
						courseEnroll.add_student(studEnroll)
						print("Enrollment successful\n")
					else:
						print("Invalid course\n")
				else:
					print("Invalid ID#\n")
			else:
				print("No student or courses\n")

		#Drop student
		elif x == "10":
			if len(courses) != 0:
				print_courses()
				ccode = input("Enter course: ")
				ccode = ccode.upper()
				courseChosen = find_course(ccode)
				if courseChosen != None:
					courseChosen.display_students()
					idnum = input("Enter ID#: ")
					studEnroll = find_student(idnum)
					if studEnroll != None and courseChosen.find_student(studEnroll) and not studEnroll.find_in_grades(courseChosen.get_ccode()):
						studEnroll.remove_course(courseChosen)
						courseChosen.remove_student(studEnroll)
						print("Removed Successfully\n")
					else:
						print("Student not enrolled\n")
				else:
					print("Invalid Course Code\n")

		#See students in a course
		elif x == "11":
			if len(courses) != 0:
				print_courses()
				ccode = input("Enter course: ")
				ccode = ccode.upper()
				courseChosen = find_course(ccode)
				if courseChosen != None:
					courseChosen.display_students()

		#See courses of student
		elif x == "12":
			if len(students) != 0:
				print_students()
				idnum = input("Enter ID#: ")
				studentChosen = find_student(idnum)
				if studentChosen != None:
					studentChosen.display_courses()

		#Set grade
		elif x == "13":
			if len(students) != 0:
				print_students()
				idnum = input("Enter ID#: ")
				studentChosen = find_student(idnum)
				if studentChosen != None:
					studentChosen.display_courses()
					ccode = input("Enter Course Code: ")
					ccode = ccode.upper()
					courseGraded = find_course(ccode)
					if courseGraded != None and studentChosen.find_course(courseGraded) and not studentChosen.find_in_grades(courseGraded.get_ccode()):
						grade = float(input("Enter grade (0-4): "))
						studentChosen.add_grade(courseGraded.get_ccode(), grade)
						print("Grade set\n")
					else:
						print("Invalid course\n")
				else:
					print("Invalid ID#\n")

		elif x == "14":
			if len(students) != 0:
				print_students()
				idnum = input("Enter ID#: ")
				studentChosen = find_student(idnum)
				if studentChosen != None:
					studentChosen.display_courses()
					print(studentChosen.print_grade())


