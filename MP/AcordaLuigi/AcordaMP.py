import re
class Course:
	def __init__(self, code, units):
		self.code = code
		self.units = float(units)
		
	def setCode(self, code):
		self.code = code
		
	def setUnits(self, units):
		self.units = float(units)
	
	def getCode(self):
		return self.code
		
	def getUnits(self):
		return self.units
class Grade:
	def __init__(self, code, grade):
		self.code = code
		self.grade = float(grade)
		
	def setCode(self, code):
		self.code = code
		
	def setGrade(self, grade):
		self.grade = float(grade)
		
	def getCode(self):
		return self.code
		
	def getGrade(self):
		return self.grade
class ReportCard:
	def __init__(self):
		self.courseList = []
		self.gradeList = []
		self.gpa = float(0)
		
	def getCourseList(self):
		return self.courseList
		
	def getGradeList(self):
		return self.gradeList
		
	def getGPA(self):
		for i in range(0, len(self.courseList)):
			print(self.courseList[i].getCode(), self.gradeList[i].getCode(), self.gradeList[i].getGrade(), self.courseList[i].getUnits() * self.gradeList[i].getGrade())
		try:
			product = float(0)
			sum = float(0)
			for i in range(0, len(self.courseList)):
				product += (self.courseList[i].getUnits()) * (self.gradeList[i].getGrade())
				sum += self.courseList[i].getUnits()
			self.gpa = product / sum
			return self.gpa
		except ZeroDivisionError:
			return 0
		
class Student:
	def __init__(self, name, id):
		self.name = name
		self.id = id
		self.reportCard = ReportCard()
		
	def setName(self, name):
		self.name = name
		
	def setId(self, id):
		self.id = id
		
	def getName(self):
		return self.name
	
	def getID(self):
		return self.id
		
	def enroll(self, code, units):
		self.reportCard.getCourseList().append(Course (code, float(units)))
		self.reportCard.getGradeList().append(Grade (code, float(0)))
		
	def drop(self, code):
		for i in range(0, len(self.reportCard.getCourseList()) - 1):
			if code == self.reportCard.getCourseList()[i].getCode():
				del self.reportCard.getCourseList()[i]
				
		for i in range(0, len(self.reportCard.getGradeList()) - 1):
			if code == self.reportCard.getGradeList()[i].getCode():
				del self.reportCard.getGradeList()[i]
	
	def setGrade(self, code, grade):
		for i in range(0, len(self.reportCard.getGradeList()) - 1):
			if code == self.reportCard.getGradeList()[i].getCode():
				self.reportCard.getGradeList()[i].setGrade(grade)
				
def checkList(list, item):
	for i in range(0, len(list)):
		if item == list[i]:
			return 1
	return 0
				
def addStudent():
	confirm = 1
	while confirm != 2:
		name = str(input("Name: "))
		id = int(input("ID: "))
		
		if name == "" or id == "" or len(str(id)) != 8:
			confirm = int(input("Invalid input\n[1]Try again\n[2]Cancel\n"))
		elif checkList(idList, id) == 1:
			confirm = int(input("Invalid ID\n[1]Try again\n[2]Cancel\n"))
		else:
			studentList.append(Student(name, id))
			idList.append(id)
			confirm = 2
			
def addCourse():
	confirm = 1
	while confirm != 2:
		code = str(input("Course: "))
		units = float(input("Units: "))
		
		if len(code) != 7 or not (units <= 4 and units >= 0) or not re.match("^[A-Z0-9-]*$", code):
			confirm = int(input("Invalid input\n[1]Try again\n[2]Cancel\n"))
		elif checkList(codeList, code) == 1:
			confirm = int(input("Invalid course\n[1]Try again\n[2]Cancel\n"))
		else:
			courseList.append(Course(code, units))
			codeList.append(code)
			confirm = 2

def editStudent(index):
	confirm = 0
	while confirm != 3:
		eMenu = {1: "[1]Edit name",
				 2: "[2]Edit ID",
				 3: "[3]Return"}
		for i in range(0, len(eMenu)):
			print(eMenu[i + 1])
		
		confirm = int(input())
		if confirm == 1:
			name = str(input("Name: "))
			studentList[index].setName(name)
		elif confirm == 2:
			id = int(input("ID: "))
			
			if id == "" or len(str(id)) != 8:
				confirm = int(input("Invalid input\n[1]Try again\n[3]Cancel\n"))
			elif checkList(idList, id) == 1:
				confirm = int(input("Invalid ID\n[1]Try again\n[3]Cancel\n"))
			else:
				studentList[index].setId(id)
				idList[index] = id
				
def checkCourse(list, item):
	for i in range(0, len(list)):
		if item == list[i].getCode():
			return 1
	return 0
				
def enrollStudent(index):
	confirm = 0
	while confirm != len(courseList) + 1:
		for i in range(0, len(courseList)):
			print("[{}]".format(i + 1), "{}".format(courseList[i].getCode()), sep = "")
	
		print("[{}]".format(len(courseList) + 1), "Return", sep = "")
		confirm = int(input())
		
		if confirm <= len(courseList):
			if checkCourse(studentList[index].reportCard.getCourseList(), codeList[confirm - 1]) == 1:
				confirm = int(input("Invalid course\n[1]Try again\n[2]Cancel\n"))
			else:
				studentList[index].enroll(courseList[confirm - 1].getCode(), courseList[confirm - 1].getUnits())
			
def dropStudent(index):
	confirm = 0
	while confirm != len(studentList[index].reportCard.getCourseList()) + 1:
		for i in range(0, len(studentList[index].reportCard.getCourseList())):
			print("[{}]".format(i + 1), "{}".format(studentList[index].reportCard.getCourseList()[i].getCode()), sep = "")
	
		print ("[{}]".format(len(studentList[index].reportCard.getCourseList()) + 1), "Return", sep = "")
		confirm = int(input())
		
		if confirm <= len(studentList[index].reportCard.getCourseList()):
			studentList[index].drop(studentList[index].reportCard.getCourseList()[confirm - 1].getCode())

def deleteStudent(index):
	studentList.remove(studentList[index])
	del idList[index]
	
def editGrade(index, courseIndex):
	confirm = 0
	while confirm != 2:
		print("Course:", studentList[index].reportCard.getCourseList()[courseIndex].getCode(), "\nUnits:", studentList[index].reportCard.getCourseList()[courseIndex].getUnits(), "\nGrade:", studentList[index].reportCard.getGradeList()[courseIndex].getGrade())
		grade = float(input("Grade: "))
		if grade % 0.5 != 0 or (grade > 4 or grade < 0):
			confirm = int(input("Invalid grade\n[1]Try again\n[2]Cancel\n"))
		else:
			studentList[index].reportCard.getGradeList()[courseIndex].setGrade(grade)
			confirm = 2
	
def gradeMenu(index, courseIndex):
	confirm = 0
	while confirm != 2:
		print("Course:", studentList[index].reportCard.getCourseList()[courseIndex].getCode(), "\nUnits:", studentList[index].reportCard.getCourseList()[courseIndex].getUnits(), "\nGrade:", studentList[index].reportCard.getGradeList()[courseIndex].getGrade())
		gMenu = {1: "[1]Edit grade in {}".format(studentList[index].reportCard.getCourseList()[courseIndex].getCode()),
				 2: "[2]Return"}
		for i in range(0, len(gMenu)):
			print(gMenu[i + 1])
			
		confirm = int(input())
		if confirm == 1:
			editGrade(index, courseIndex)
			
def enrolledCourses(index):
	confirm = 0
	while confirm != len(studentList[index].reportCard.getCourseList()) + 1:
		for i in range(0, len(studentList[index].reportCard.getCourseList())):
			print("[{}]".format(i + 1), "{}".format(studentList[index].reportCard.getCourseList()[i].getCode()), sep = "")
	
		print("[{}]".format(len(studentList[index].reportCard.getCourseList()) + 1), "Return", sep = "")
		confirm = int(input())
		
		if confirm <= len(studentList[index].reportCard.getCourseList()):
			gradeMenu(index, confirm - 1)
		
def computeGPA(index):
	if studentList[index].reportCard.getGPA() != 0:
		print ("GPA of {} is".format(studentList[index].getName()), studentList[index].reportCard.getGPA())
	else:
		print("GPA is N/A")
			
def studentMenu(index):
	confirm = 0
	while confirm != 7:
		print("Name:", studentList[index].getName(), "\nID:", studentList[index].getID())
		sMenu = {1: "[1]Edit {}".format(studentList[index].getName()),
				 2: "[2]Enroll a course for {}".format(studentList[index].getName()),
				 3: "[3]Drop a course for {}".format(studentList[index].getName()),
				 4: "[4]Delete {}".format(studentList[index].getName()),
				 5: "[5]Enrolled courses of {}".format(studentList[index].getName()),
				 6: "[6]GPA of {}".format(studentList[index].getName()),
				 7: "[7]Return"}
		for i in range(0, len(sMenu)):
			print(sMenu[i + 1])
			
		confirm = int(input())
		if confirm == 1:
			editStudent(index)
		elif confirm == 2:
			enrollStudent(index)
		elif confirm == 3:
			dropStudent(index)
		elif confirm == 4:
			deleteStudent(index)
			return
		elif confirm == 5:
			enrolledCourses(index)
		elif confirm == 6:
			computeGPA(index)
			
			
def viewStudents():
	confirm = int(0)
	while confirm != len(studentList) + 1:
		for i in range(0, len(studentList)):
			print("[{}]".format(i + 1), "{}".format(studentList[i].getName()), sep = "")
		
		print ("[{}]".format(len(studentList) + 1), "Return", sep = "")
		confirm = int(input())
		
		if confirm <= len(studentList):
			studentMenu(confirm - 1)
			
def editCourse(index):
	confirm = 0
	while confirm != 3:
		eMenu = {1: "[1]Edit code",
				 2: "[2]Edit units",
				 3: "[3]Return"}
		for i in range(0, len(eMenu)):
			print(eMenu[i + 1])
		
		confirm = int(input())
		if confirm == 1:
			code = str(input("Code: "))
			
			if len(code) != 7 or not re.match("^[A-Z0-9-]*$", code):
				confirm = int(input("Invalid input\n[1]Try again\n[2]Cancel\n"))
			elif checkList(codeList, code) == 1:
				confirm = int(input("Invalid course\n[1]Try again\n[2]Cancel\n"))
			else:
				courseList[index].setCode(code)
				codeList[index] = code
				
				for i in range(0, len(studentList)):
					if checkCourse(studentList[i].reportCard.getCourseList(), codeList[index]) == 1:
						for j in range(0, len(studentList[i].reportCard.getCourseList())):
							if studentList[i].reportCard.getCourseList()[j].getCode() == codeList[index]:
								studentList[i].reportCard.getCourseList()[j].setCode(code)
			
		elif confirm == 2:
			units = float(input("Units: "))
			
			if not (units <= 4 and units >= 0):
				confirm = int(input("Invalid input\n[1]Try again\n[2]Cancel\n"))
			else:
				courseList[index].setUnits(units)
				
				for i in range(0, len(studentList)):
					if checkCourse(studentList[i].reportCard.getCourseList(), codeList[index]) == 1:
						for j in range(0, len(studentList[i].reportCard.getCourseList())):
							if studentList[i].reportCard.getCourseList()[j].getCode() == codeList[index]:
								studentList[i].reportCard.getCourseList()[j].setUnits(units)
					
					

def deleteCourse(index):
	courseList.remove(courseList[index])
	del codeList[index]

def courseMenu(index):
	confirm = 0
	while confirm != 3:
		print("Course:", courseList[index].getCode(), "\nUnits:", courseList[index].getUnits())
		sMenu = {1: "[1]Edit {}".format(courseList[index].getCode()),
				 2: "[2]Delete {}".format(courseList[index].getCode()),
				 3: "[3]Return"}
		for i in range(0, len(sMenu)):
			print(sMenu[i + 1])
			
		confirm = int(input())
		if confirm == 1:
			editCourse(index)
		elif confirm == 2:
			deleteCourse(index)
			return
			
def viewCourses():
	confirm = 0
	while confirm != len(courseList) + 1:
		for i in range(0, len(courseList)):
			print("[{}]".format(i + 1), "{}".format(courseList[i].getCode()), sep = "")
			
		print ("[{}]".format(len(courseList) + 1), "Return", sep = "")
		confirm = int(input())
		
		if confirm <= len(courseList):
			courseMenu(confirm - 1)
			
choice = 0
studentList = []
idList = []
courseList = []
codeList = []

while choice != 7:
	menu = {1: "[1]Add Student",
			2: "[2]Add Courses",
			3: "[3]View All Students",
			4: "[4]View All Courses",
			5: "[5]Save Data",
			6: "[6]Load Data",
			7: "[7]Exit"}
	for i in range(0, len(menu)):
		print(menu[i + 1])
		
	choice = int(input())
	if choice == 1:
		addStudent()
	elif choice == 2:
		addCourse()
	elif choice == 3:
		viewStudents()
	elif choice == 4:
		viewCourses()
	elif choice == 5:
		import pickle
		pickle.dump(studentList, open("studentList.p", "wb"))
		pickle.dump(idList, open("idList.p", "wb"))
		pickle.dump(courseList, open("courseList.p", "wb"))
		pickle.dump(codeList, open("codeList.p", "wb"))
	elif choice == 6:
		try:
			import pickle
			studentList = pickle.load(open("studentList.p", "rb"))
			idList = pickle.load(open("idList.p", "rb"))
			courseList = pickle.load(open("courseList.p", "rb"))
			codeList = pickle.load(open("codeList.p", "rb"))
			print(studentList[0].getName())
		except IOError:
			print("Save file does not exist")
