from CourseInfo import *

class CourseGrade:
	def __init__(self, courseInfo, grade = "NGS"):
		self.setCourseInfo(courseInfo)
		self.setGrade (grade, True)

	def getCourseInfo(self):
		return self.courseInfo

	def getGrade(self):
		return self.grade

	def setCourseInfo(self, courseInfo):
		self.courseInfo = courseInfo

	def setGrade(self, grade, b = False):
		g = ["0.0","1.0","1.5","2.0","2.5","3.0","3.5","4.0", "NGS", "passed", "failed"]
		var = grade
		try:
			var = str(float(grade))
		except:
			pass
		
		try:
			i = g.index (var)
			self.grade = g[i]
			if not b:
				print ("input grade successful")
		except:
			print ("invalid input grade")

	def __str__(self):
		return str(self.getCourseInfo()) + " " + str(self.getGrade())
