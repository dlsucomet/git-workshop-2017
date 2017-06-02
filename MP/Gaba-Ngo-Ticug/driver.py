# Gaba, Janelle Marie
# Ngo, Jan Bertel
# Ticug, Jonal Ray

from model import *

print("MENU")
print("1. Add Student")
print("2. Edit Student Info")
print("3. Delete Student")
print("4. Add Courses")
print("5. Edit Course")
print("6. Delete Course")
print("7. Enroll Student")
print("8. Drop Student")
print("9. Set Grade")
print("10. View Grade")
choice = int(input(">> "))

students = []
courses = []


while (choice <= 10 and choice >= 0):
	if choice == 1:
		#Add Student
		name = input("Name: ")
		idNum = ''
		while len(idNum) != 8:
			idNum = input("ID#: ")
		students.append(student(name, idNum))
		print("Student Added!\n")

	elif choice == 2:
		#Edit Student
		for i in students:
			print(i.printinfo())

		x = input("Enter ID#: ")
		for i in students:
			if i.getid() == x:
				i.name = input("Enter name: ")
				print("Info Edited!\n")

	elif choice == 3:
		#Delete Student
		for i in students:
			print(i.printinfo())

		x = input("Enter ID#: ")
		for i in students:
			if i.getid() == x:
				students.remove(i)
				print("Student removed!\n")

	elif choice == 4:
		#Add Course
		cc = ''
		while len(cc) != 7:
			cc = input("Course Code: ")
			cc = cc.upper()
		u = float(input("Units: "))
		fl = input("Floating (Y/N): ")

		if fl == 'Y':
			fl = True
		else:
			fl = False

		courses.append(section(cc, u, fl))
		print("Course Added!\n")

	elif choice == 5:
		# Edit Course
		for i in courses:
			print(i.courseinformation.getcode())

		sc = input("Enter Course Code: ")
		for i in courses:
			if i.courseinformation.getcode() == sc:
				i.courseinformation.units = float(input("Units: "))
				i.courseinformation.floating = input("Floating (Y/N): ")
				print("Info Edited!\n")

	elif choice == 6:
		#Delete Course
		for i in courses:
			print(i.courseinformation.getcode())

		x = input("Enter Course Code: ")
		for i in courses:
			if i.courseinformation.getcode() == x:
				courses.remove(i)
				print("Course removed!\n")

	elif choice == 7:
		#Enroll Student
		print("STUDENTS:")
		for i in students:
			i.printinfo()

		print("COURSES:")
		for i in courses:
			print(i.courseinformation.getcode())

		found = False
		x = input("Enter ID#: ")
		for s in students:
			if s.getid() == x:
				found = True
		c = input("Enter course code: ")
		for i in courses:
			if i.courseinformation.getcode() == c and found:
				s.addcourse(course(i.courseinformation))
				i.addstudent(s)
				print("Student Enrolled\n")

	elif choice == 8:
		#Drop Student
		for i in courses:
			print(i.courseinformation.getcode())

		c = input("Enter course code: ")

		for i in courses:
			if i.courseinformation.getcode() == c:
				i.displaystudents()

			x = input("Enter ID#: ")
			for s in i.students:
				if s.getid() == x:
					i.students.remove(s)
					print("Student removed!\n")

	elif choice == 9:
		#set grade

		for i in students:
			i.printinfo()

		x = input("Enter ID#: ")
		for i in students:
			if i.getid() == x:
				i.displaycourses()
				y = input("Enter Course Code: ")
				for c in i.courses:
					if c.courseinformation.getcode() == y:
						c.grade = float(input("Grade: "))
						print("Graded!\n")

	elif choice == 10:
		#View Grade

		for i in students:
			i.printinfo()
			for s in i.courses:
				s.showgrades()

		print("\n")

	elif choice == 0:
		for i in students:
			print("\t")
			i.printinfo()
			i.displaycourses()

		for i in courses:
			print("\t" + i.courseinformation.getcode())
			i.displaystudents()

	print("MENU")
	print("1. Add Student")
	print("2. Edit Student Info")
	print("3. Delete Student")
	print("4. Add Courses")
	print("5. Edit Course")
	print("6. Delete Course")
	print("7. Enroll Student")
	print("8. Drop Student")
	print("9. Set Grade")
	print("10. View Grade")
	choice = int(input(">> "))

