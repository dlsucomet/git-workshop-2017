#Santiago, Gabriel

import os
import re

#Student class
class Student:
	#initialize Student object
	def __init__(self, name, idNum):
		self.name = name
		self.idNum = idNum
		self.courses = []
		self.gpa = float(0)

	#enroll Student to a Course
	def enrollCourse(self, course):
		self.courses.append(course)

	#drop a Course
	def dropCourse(self, index):
		self.courses.remove(self.courses[index])

	#set Student's name
	def setName(self, name):
		self.name = name

	#set Student's ID number
	def setIDNum(self, idNum):
		self.idNum = idNum

	#view Student's report card
	def viewCard(self):
		print("Name: " + self.name)
		print("ID number: " + self.idNum)
		print("Grades:")
		for c in courses:
			c.viewCourseInfo()

			for c in courses:
				gpa += c.grade

			gpa /= len(self.courses)

			print("GPA = " + gpa)

#Course class
class Course:
	#initialize Course
	def __init__(self, code, units, grade):
		self.code = code
		self.units = units
		self.grade = grade

	#set Course's course code
	def setCourseCode(self, code):
		self.code = code

	#set Course's units
	def setUnits(self, units):
		self.units = units

	def setGrade(self, grade):
		self.grade = grade

	#view Course code, units, and grade
	def viewCourseInfo(self):
		print(code + "Units: " + units + "Grade: " + grade)

#User
#initialize vars
students = []
numStudents = 0
courses = []
choice = 0

#Menu
while choice != 11: #while choice not exit
	#initial screen
	print("Welcome to My Enrollment System!")
	print("What would you like to do?")
	print("1. Add student")
	print("2. Edit student info")
	print("3. Delete student")
	print("4. Add course")
	print("5. Edit course info")
	print("6. Delete course")
	print("7. Enroll student")
	print("8. Drop course")
	print("9. Set grade")
	print("10. View student's report card")
	print("11. Save/Load Data")
	print("12. Exit")

	choice = int(input())
	os.system('cls')

	#add student
	if choice == 1:
		print("Add Student")
		confirm = 0
		while confirm != 1:
			name = str(input("Enter name: "))

			if(name == ""):
				confirm = int(input("Invalid input. [0] Retry [1] Cancel"))
				os.system("cls")
			else:
				confirm = 1
				students.append(Student(name, numStudents))
				numStudents += 1
				os.system("cls")

	#edit student info
	elif choice == 2:
                print("Edit Student info")
                print("Search for student by: [1] Name [2] ID Number [Any other] Exit")
                searchChoice = int(input())

                if searchChoice == 1: #search by name
                        print("Enter name of Student:")
                        name = str(input())

                        for s in students:
                                if s.name == name:
                                	temp = str(input("Enter new name for Student: "))
                                	s.setName(temp)
                                	input("Name changed successfully to " + s.name)
                                	break
                                else:
                                        input("Name not found.")


                elif searchChoice == 2: #search by idnum
                        print("Enter ID number of student: ")
                        idNum = int(input())

                        if not isinstance(idNum, int):
                        		print("Invalid input.")
                        else:
                                for s in students:
                                        if s.idNum == idNum:
                                                temp = str(input("Enter new name for Student: "))
                                                s.setName(temp)
                                                input("Name changed successfully to " + s.name)
                                                break
                                        else:
                                               input("ID number not found.")

                else:
                        os.system("cls")

                os.system("cls")


	#delete student
	elif choice == 3:
		searchChoice = 0
		print("Delete Student")
		print("Search for student by: [1] Name [2] ID Number [Any other] Exit")
		searchChoice = int(input())

		if searchChoice == 1: #search by name
			print("Enter name of Student:")
			name = str(input())

			for s in students:
				if s.name == name:
					temp = s.name
					students.remove(s)
					print(temp + "has successfully been deleted.")
					input("Press any key to exit.")
					break
				else:
					print("Name not found.")


		elif searchChoice == 2: #search by idnum
			print("Enter ID number of student: ")
			idNum = int(input())

			if not isinstance(idNum, int):
				print("Invalid input.")
			else:
				for s in students:
					if s.idNum == idNum:
						temp = s.name
						students.remove(s)
						print(temp + "has successfully been deleted.")
						input("Press any key to exit.")
						break
					else:
						print("ID number not found.")

		else:
			os.system("cls")

		os.system("cls")


	#add course
	elif choice == 4:
		print("Add Course")
		confirm = 0
		while confirm != 1:
			code = str(input("Enter course code (capital letters, numbers, and dash only): "))
			units = float(input("Enter number of units (0-4 only): "))

			if len(code) != 7 or not code.isupper() or not re.match("^[A-Z0-9-]*$", code) or units < 0 or units > 4:
				confirm = int(input("Invalid input. [0] Retry [1] Cancel"))
				os.system("cls")
			else:
				for c in courses:
					if c.code == code:
						confirm = int(input("Course already exists. [0] Retry [1] Cancel"))
						os.system("cls")
						break
					else:
						courses.append(Course(str(code), units, 0.0))
						confirm = 1
						os.system("cls")

	#edit course info
	elif choice == 5:
		print("Edit Course info")
		print("Enter name of Course: ")
		name = str(input())

		for c in courses:
			if c.code == name:
				print(c.code + "-" + c.units)
				option = int(input("[1] Edit course code  [2] Edit number of units [Any other] Exit"))

				if option == 1:
					temp = str(input("Enter new code for the course:"))

					if len(temp) != 7 or not temp.isupper() or not re.match("^[A-Z0-9-]*$", temp):
						input("Invalid input.")
					else:
						c.setCourseCode(temp)
						input("Successfully renamed to" + c.code)

				elif option == 2:
					temp = int(input("Enter new number of units for the course:"))

					if temp < 0 or temp > 4:
						input("Invalid Input.")
					else:
						c.setUnits(temp)
						input("Successfully changed number of units to" + c.code)

				break
			else:
				print("Course not found.")
				input()

		os.system("cls")

	#delete course
	elif choice == 6:
		print("Delete Course")
		print("Enter name of Course:")
		name = str(input())

		for c in courses:
			if c.name == name:
				temp = c.name
				courses.remove(c)
				print(temp + "has been successfully deleted.")
				input("Press any key to exit.")
				break
			else:
				print("Course not found.")
				input()

		os.system("cls")

	#enroll student
	elif choice == 7:
		searchChoice = 0
		print("Enroll Student")
		print("Search for student by: [1] Name [2] ID Number [Any other] Exit")
		searchChoice = int(input())

		if searchChoice == 1: #search by name
			print("Enter name of Student:")
			name = str(input())

			for s in students:
				if s.name == name:
					#enroll student to a course
					print("Select course to enroll:")
					for x in range (1, len(courses)):
						print(x + "." + courses[x].viewCourseInfo())
						print("[Any other] Back")
						option = input()
						valid = 1

						if option < len(courses):
							for c in s.courses:
								if c.code == courses[option - 1].code:
									input("Cannot enroll; student is already enrolled.")
									valid = 0
									break
							
							if valid == 1:						
								s.enrollCourse(courses[option - 1])
								input(courses[option - 1].code + "successfully enrolled!")

					break
				else:
					input("Name not found.")


		elif searchChoice == 2: #search by idnum
			print("Enter ID number of student: ")
			idNum = int(input())

			if not isinstance(idNum, int):
				print("Invalid input.")
			else:
				for s in students:
					if s.idNum == idNum:
						#enroll student to a course
						print("Select course to enroll:")
						for x in range (1, len(courses)):
							print(x + "." + courses[x].viewCourseInfo())
							print("[Any other] Back")
							option = input()
							valid = 1

							if option < len(courses):
								for c in s.courses:
									if c.code == courses[option - 1].code:
										input("Cannot enroll; student is already enrolled.")
										valid = 0
										break
							
								if valid == 1:						
									s.enrollCourse(courses[option - 1])
									input(courses[option - 1].code + "successfully enrolled!")

						break
					else:
						print("ID number not found.")

		else:
			os.system("cls")

		os.system("cls")
        
	#drop course
	elif choice == 8:
		print("Drop Course")
		print("Search for student by: [1] Name [2] ID Number [Any other] Exit")
		searchChoice = int(input())

		if searchChoice == 1: #search by name
			print("Enter name of Student:")
			name = str(input())

			for s in students:
				if s.name == name:
					#drop student's course
					print("Select course to drop:")
					for x in range (1, len(s.courses)):
						print(x + "." + s.courses[x].viewCourseInfo())
						print("[Any other] Back")
						option = input()
						valid = 1
						option -= 1

						if option < len(s.courses):
							temp = s.courses[option].code
							s.courses.pop(option)
							input(temp + " successfully dropped.")

					break
				else:
					input("Name not found.")


		elif searchChoice == 2: #search by idnum
			print("Enter ID number of student: ")
			idNum = int(input())

			if not isinstance(idNum, int):
				print("Invalid input.")
			else:
				for s in students:
					if s.idNum == idNum:
						#drop student's course
                                                print("Select course to drop:")
                                                for x in range (1, len(s.courses)):
                                                	print(x + "." + s.courses[x].viewCourseInfo())
                                                	print("[Any other] Back")
                                                	option = input()
                                                	option -= 1

                                                if option < len(s.courses):
                                                        temp = s.courses[option].code
                                                        s.courses.pop(option)
                                                        input(temp + " successfully dropped.")

						#break
					else:
						print("ID number not found.")

		else:
			os.system("cls")

		os.system("cls")

	#set grade
	elif choice == 9:
		print("Set Student's grade for a Course")
		print("Search for student by: [1] Name [2] ID Number [Any other] Exit")
		searchChoice = int(input())

		if searchChoice == 1: #search by name
			print("Enter name of Student:")
			name = str(input())

			for s in students:
				if s.name == name:
					#grade course
					print("Select course to grade:")
					for x in range (1, len(s.courses)):
						print(x + ". " + s.courses[x].viewCourseInfo())
						print("[Any other] Back")
						option = input()
						valid = 1
						option -= 1

						if option < len(s.courses):
							temp = int(input("Enter grade: "))

							if temp < 0 or temp > 4:
								input("Invalid input.")
							else:
								s.courses[option].setGrade(temp)
								input(s.courses[option].code + " successfully graded " + s.courses[option].grade)

					break
				else:
					input("Name not found.")


		elif searchChoice == 2: #search by idnum
			print("Enter ID number of student: ")
			idNum = int(input())

			if not isinstance(idNum, int):
				print("Invalid input.")
			else:
				for s in students:
					if s.idNum == idNum:
						#grade course
						print("Select course to grade:")
						for x in range (1, len(s.courses)):
							print(x + ". " + s.courses[x].viewCourseInfo())
							print("[Any other] Back")
							option = input()
							valid = 1
							option -= 1

							if option < len(s.courses):
								temp = int(input("Enter grade: "))
							
								if temp < 0 or temp > 4:
									input("Invalid input.")
								else:
									s.courses[option].setGrade(temp)
									input(s.courses[option].code + " successfully graded " + s.courses[option].grade)

						break
					else:
						print("ID number not found.")

		else:
			os.system("cls")

		os.system("cls")

        
	#view report card
	elif choice == 10:
		searchChoice = 0
		print("View Student's Report Card")
		print("Search for student by: [1] Name [2] ID Number [Any other] Exit")
		searchChoice = int(input())

		if searchChoice == 1: #search by name
			print("Enter name of Student:")
			name = str(input())

			for s in students:
				if s.name == name:
					s.viewCard()
					input("Press any key to exit.")
					break
				else:
					print("Name not found.")
					input()


		elif searchChoice == 2: #search by idnum
			print("Enter ID number of student: ")
			idNum = int(input())

			if not isinstance(idNum, int):
				print("Invalid input.")
			else:
				for s in students:
					if s.idNum == idNum:
						s.viewCard()
						input("Press any key to exit.")
						break
					else:
						print("ID number not found.")
						input()

		else:
			os.system("cls")

		os.system("cls")
	
	#save and load
	elif choice == 11:
		print("Save/Load data")
		dataChoice = int(0)
		while dataChoice < 3:
			dataMenu = {1: "[1] Save Data", 2: "[2] Load Data", 3: "[3] Back"}
			for x in range (0, len(dataMenu)):
				print(dataMenu[x+1])
				
			dataChoice = int(input("Choice: "))
			
			#Save
			if dataChoice == 1:
				import pickle	
				pickle.dump(students, open("Students.p", "wb"))
				pickle.dump(courses, open("Courses.p", "wb"))
				os.system('cls')
				dataChoice = 3
			
			#Load
			elif dataChoice == 2:
				try:
					import pickle
					students = pickle.load(open("Students.p", "rb"))
					courses = pickle.load(open("Courses.p", "rb"))
					dataChoice = 3
					nStudents = len(studentList)
				except IOError:
					print("Save file does not exist")
					input("Press Enter...")
					dataChoice = 3
			os.system('cls')

