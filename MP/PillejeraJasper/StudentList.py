from Student import *

class StudentList:
	def __init__ (self):
		self.students = []
		
	def addStudent (self, student):
		if student is None:
			raise ValueError ()
			
		self.students.append (student)
		self.students.sort (key = lambda x: x.id)
		
		print (str(student) + " was successfully added")
		
	def removeStudent (self, student):
		try:
			i = self.students.index(student)
			del self.students[i]
			for x in student.getCoursesGrades ():
				student.removeEnrolledCourse (x.getCourseInfo ())
			print (str(student) + " was successfully removed")
		except:
			print (str(student) + " does not exist")
		
	def getStudent (self, index):
		try:
			return self.students[index]
		except:
			print ("invalid index for student list")
		
	def printStudents (self):
		for i in range(len (self.students)):
			print ("[" + str(i) + "] " + str(self.students[i]))