from CourseInfo import *

class CourseList:
	def __init__(self):
		self.courseInfo = []

	def addCourse (self, course):
		if course is None:
			raise ValueError ()
			
		self.courseInfo.append(course)
		self.courseInfo.sort(key=lambda x: x.code)

	def removeCourse (self, course):
		if course is None:
			print ("null input course")
			return
			
		try:
			for i in (0, course.courseInfo.getStudents().__len__()):
				del course.courseInfo.getStudents()[i]

			i = self.courseInfo.index(course)
			del self.courseInfo[i]
			print (str (course) + " successfully removed")
		except:
			print (str (course) + " does not exist")
			
	def getCourse(self, index):
		try:
			return self.courseInfo[index]
		except:
			print ("invalid index selected")
			
	def printCourses(self):
		for i in range(len(self.courseInfo)):
			print("[" + str(i) + "] "  + str(self.courseInfo[i]))
