# Classes
class Student:
	def __init__(self, name, idnum):
		self.name = name
		self.idnum = idnum
		self.courseGrades = {}
		self.enrolledCourses = {}
		self.floatBasis = {}

	def editInfo(self, newName):
		self.name = newName

	def enrollStud(self, cc, units, fl):
		self.courseGrades[cc] = 0.0
		self.enrolledCourses[cc] = units
		self.floatBasis[cc] = fl

	def dropCourse(self, cc):
		del self.courseGrades[cc]

	def gradeStud(self, cc, grade):
		self.courseGrades[cc] = grade

	def reportCard(self):
		computedGPA = 0.0
		totalUnits = 0

		print("Course\t\tUnits\t\tGrade")
		for course, grade in self.courseGrades.items():
			print(course + "\t\t" + str(self.enrolledCourses[course]) + "\t\t" + str(grade))
			if (self.floatBasis[course] == "False"):
				computedGPA += float(self.enrolledCourses[course]) * float(grade)
				totalUnits += float(self.enrolledCourses[course])
		gpa = computedGPA / totalUnits
		print("GPA = " + str(gpa))

class Course:
	def __init__(self, courseCode, units, floating):
		self.courseCode = courseCode
		self.units = units
		self.floating = floating # Boolean
		self.enrolled = []

	def editInfo(self, units, floating):
		self.units = units
		self.floating = floating

	def addStudent(self, student):
		self.enrolled.append(student)

	def removeStudent(self, student):
		self.enrolled.remove(student)

	def getAllStudents(self):
		return self.enrolled

# Functions
def validID(idnum, allStuds):
	for studs in allStuds:
		if studs.idnum == idnum:
			return True
	return False

def findStud(idnum, allStuds):
	for studs in allStuds:
		if studs.idnum == idnum:
			return studs
	return None	

def validCC(courseCode):
	if len(courseCode) > 7 or courseCode.upper() != courseCode:
		return False
	return True

def validCourse(cc, allCourse):
	for x in allCourse:
		if cc == x.courseCode:
			return True
	return False

def findCourse(cc, allCourse):
	for x in allCourse:
		if cc == x.courseCode:
			return x
	return None

def checkDuplicateCourse(std, crs):
	for course, grade in std.enrolledCourses.items():
		if course == crs:
			return True
	return False

# Start of Program
program = True
allStudents = []
allCourses = []
studCount = 0

while program:
	print("Menu: \n" +
		  "1 - Create Student\n" + 
		  "2 - Edit Student Information\n" + 
		  "3 - Delete Student\n" + 
		  "4 - Create Course\n" + 
		  "5 - Edit Course Information\n" + 
		  "6 - Delete Course\n" + 
		  "7 - Enroll Student to Course\n" + 
		  "8 - Drop Student in Course\n" + 
		  "9 - Give Grade to Student\n" +
		  "0 - View Report Card\n" + 
		  "X - Quit")
	option = input("Option: ")

	print("")
	if option == "X":
		break
	elif option == "1":
		name = input("Enter Name: ")
		studCount += 1
		allStudents.append(Student(name, studCount))
		print("Student is successfully added!")
	elif (option == "2" or option == "3") and len(allStudents) > 0:
		print("ID\t\t\tName")
		for studs in allStudents:
			print(str(studs.idnum) + "\t\t\t" + studs.name)
		if option == "2":
			changeOption = input("Input the ID Number of the student you want to change: ")
		else:
			changeOption = input("Input the ID Number of the student you want to DELETE: ")

		if validID(int(changeOption), allStudents):
			if option == "2":
				newName = input("What is his/her new name? ")
				findStud(int(changeOption), allStudents).editInfo(newName)
				print("Student is successfully changed!")
			else:
				allStudents.remove(findStud(int(changeOption), allStudents))
				print("Student is successfully deleted!")	
	elif option == "4":
		cc = input("Enter Course Code: ")
		units = input("Enter No. of Units: ")
		floating = input("Floating Subject? [True or False]: ")
		
		if validCC(cc) and int(units) >= 0 and int(units) <= 4:
			allCourses.append(Course(cc, int(units), floating))
			print("Course is successfully added!")
	elif (option == "5" or option == "6") and len(allCourses) > 0:
		print("Course\t\t\tUnits\t\t\tFloating")
		for crs in allCourses:
			print(crs.courseCode + "\t\t\t" + str(crs.units) + "\t\t\t" + crs.floating)
		if option == "5":
			changeOption = input("Input the Course Code of the course you want to edit: ")
		else:
			changeOption = input("Input the Course Code of the course you want to DELETE: ")

		if validCourse(changeOption, allCourses):
			if option == "5":
				newUnits = input("New no. of units: ")
				newFloat = input("Still floating? [True or False]: ")
				findCourse(changeOption, allCourses).editInfo(int(newUnits), newFloat)
				print("Course successfully changed!")
			else:
				allCourses.remove(findCourse(changeOption, allCourses))
				print("Course successfully deleted!")		
	elif option == "7" and len(allStudents) > 0 and len(allCourses) > 0:
		print("ID\t\t\tName")
		for studs in allStudents:
			print(str(studs.idnum) + "\t\t\t" + studs.name)
		studOption = input("Input the ID Number of the student you want to enroll: ")

		print("Course\t\t\tUnits\t\t\tFloating")
		for crs in allCourses:
			print(crs.courseCode + "\t\t\t" + str(crs.units) + "\t\t\t" + crs.floating)
		crsOption = input("Input the Course Code of the course: ")

		if validID(int(studOption), allStudents) and validCourse(crsOption, allCourses):
			crsChosen = findCourse(crsOption, allCourses)
			stdChosen = findStud(int(studOption), allStudents)

			if not(checkDuplicateCourse(stdChosen, crsChosen)):
				stdChosen.enrollStud(crsOption, int(crsChosen.units), crsChosen.floating)
				crsChosen.addStudent(stdChosen)
				print("Student is successfully enrolled to " + crsOption)
			else:
				print("Student is already enrolled!")
	elif option == "8" and len(allStudents) > 0 and len(allCourses) > 0:
		print("Course\t\t\tUnits\t\t\tFloating")
		for crs in allCourses:
			print(crs.courseCode + "\t\t\t" + str(crs.units) + "\t\t\t" + crs.floating)
		crsOption = input("Input the Course Code of the course: ")

		if validCourse(crsOption, allCourses):
			print("ID\t\t\tName")
			crsChosen = findCourse(crsOption, allCourses)
			for std in crsChosen.getAllStudents():
				print(str(std.idnum) + "\t\t\t" + std.name)
			studOption = input("Input the ID Number of the student you want to drop: ")

			if validID(int(studOption), crsChosen.getAllStudents()):
				remStd = findStud(int(studOption), allStudents)
				crsChosen.removeStudent(remStd)
				remStd.dropCourse(crsOption)
				print("Successfully dropped!")
	elif option == "9" and len(allStudents) > 0 and len(allCourses) > 0:
		print("ID\t\t\tName")
		for studs in allStudents:
			print(str(studs.idnum) + "\t\t\t" + studs.name)
		studOption = input("Input the ID Number of the student you want to grade: ")

		if validID(int(studOption), allStudents): 
			stdChosen = findStud(int(studOption), allStudents)
			print("Course\t\t\tUnits")
			for crs, units in stdChosen.enrolledCourses.items():
				print(crs + "\t\t\t" + str(units))
			crsOption = input("Input the Course Code of the course: ")

			if validCourse(crsOption, allCourses):
				grade = input("Input the grade: ")
				if float(grade) >= 0 and float(grade) <= 4:
					stdChosen.gradeStud(crsOption, grade)
					print("Student is successfully graded!")
	elif option == "0" and len(allStudents) > 0:
		print("ID\t\t\tName")
		for studs in allStudents:
			print(str(studs.idnum) + "\t\t\t" + studs.name)
		studOption = input("Input the ID Number you want to see the report card: ")

		if validID(int(studOption), allStudents):
			findStud(int(studOption), allStudents).reportCard()

	print("")