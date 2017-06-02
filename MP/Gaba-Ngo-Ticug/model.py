class section:

	def __init__(self, code, units, floating):
		self.courseinformation = courseinfo(code, units, floating)
		self.students = []

	def addstudent(self, student):
		self.students.append(student)

	def displaystudents(self):
		for i in self.students:
			i.printinfo()

class courseinfo:

	def __init__(self, code, units, floating):
		self.__code = code
		self.units = units
		self.floating = floating

	def getcode(self):
		return self.__code

class course:

	def __init__(self, c):
		self.courseinformation = c
		self.grade = 0.0

	def showgrades(self):
		print(self.courseinformation.getcode() + ":" + str(self.grade))


class student:

	def __init__(self, name, id):
		self.name = name
		self.__id = id
		self.courses = []

	def addcourse(self, course):
		self.courses.append(course)

	def displaycourses(self):
		for i in self.courses:
			print(i.courseinformation.getcode())

	def getid(self):
		return self.__id

	def printinfo(self):
		print(self.__id + " - " + self.name)
