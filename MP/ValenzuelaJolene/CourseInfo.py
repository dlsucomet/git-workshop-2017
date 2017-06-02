from Student import *
from CourseGrade import *

class CourseInfo:
	def __init__(self, code, units):
		self.setCode(code)
		self.setUnits(units)
		self.students = []

	def getCode(self):
		return self.code

	def getUnits(self):
		return self.units

	def getStudents(self):
		return self.students

	def setCode(self, code):
		if len(code) != 7:
			raise ValueError()
		self.code = code

	def setUnits(self, units):
		var = units
		try:
			var = str(float(units))
		except:
			pass
			
		try:
			u = ["0.0", "0.5", "1.0", "2.0", "3.0", "4.0"]
			index = u.index(var)
		except:
			raise ValueError()
		self.units = var

	def addEnrolledStudent(self, student):
		self.students.append(student)
		self.students.sort(key=lambda x: x.id)

	#except clause doesn't actually execute  
	#but keeping for precautionary measures
	#can never be too safe in python
	def removeEnrolledStudent(self, student):
		try:
			i = self.students.index(student)
			del self.students[i]
		except:
			pass

	def __cmp__ (self, other):
		return self.getCode == other.getCode () and self.getUnits () == other.getUnits ()
			
	def __str__(self):
		return str(self.code) + " " + str(self.units)