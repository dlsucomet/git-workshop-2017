from CourseInfo import *
from CourseGrade import *

class Student:
	def __init__(self, name="", id=""):
		self.setName (name)
		self.setId (id)
		self.courseGrades = []

	def getName(self):
		return self.name

	def getId(self):
		return self.id

	def getCoursesGrades(self):
		return self.courseGrades
		
	def setCourseGrade (self, courseInfo, grade):
		if courseInfo is None:
			raise ValueError ()
	
		for i in range(len(self.courseGrades)):
			if self.courseGrades[i].getCourseInfo () == courseInfo:
				self.courseGrades[i].setGrade (grade)
				print ("student grade recorded")
				print (str(self.courseGrades[i]))
				return
		
		print ("student not enrolled in " + str (courseInfo))

	def setName(self, name):
		if name is None:
			raise ValueError ()
		if name == "":
			raise ValueError ()
		self.name = str (name)

	def setId(self, id):
		if id is None:
			raise ValueError ()
		if id == "":
			raise ValueError ()
		self.id = str (id)

	def addEnrolledCourse(self, courseInfo):
		if courseInfo is None:
			raise ValueError ()

		self.courseGrades.append(CourseGrade(courseInfo))
		courseInfo.addEnrolledStudent (self)
		self.courseGrades.sort(key = lambda x: x.courseInfo.getCode ())
		print(self.id + " " + self.name + " is enrolled in " + str(courseInfo))

	def removeEnrolledCourse(self, courseInfo):
		if courseInfo is None:
			raise ValueError ()
			
		for i in range(len(self.courseGrades)):
			if self.courseGrades[i].getCourseInfo () == courseInfo:
				del self.courseGrades[i]
				courseInfo.removeEnrolledStudent (self)
				print(self.id + " " + self.name + " was drop in " + str(courseInfo))
				return
				
		print ("student is not enrolled in this course")

	def printGPA (self):
		print ("\nprinting grades of " + str(self) + ":\n")
	
		sumUnits = 0.0
		sumFG = 0.0
		gpa = 0.0
		
		for i in range(len(self.courseGrades)):
			try:
				print (str(self.courseGrades[i]))
				sumFG += (float (self.courseGrades[i].getCourseInfo ().getUnits ()) * float (self.courseGrades[i].getGrade ()))
				sumUnits += float (self.courseGrades[i].getCourseInfo ().getUnits ())
			except:
				pass
		
		try:
			gpa = sumFG / sumUnits
		except:
			pass
			
		print ("\nGPA of " + str(self) + ": " + str(gpa))
		print ()
	
	def __str__(self):
		return str(self.id) + " " + str(self.name)
