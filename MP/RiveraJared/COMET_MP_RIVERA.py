import os
import sys

class Database():
	def __init__(self):
		self.studentList = []
		self.courseList = []
		
	def addStudent(self, name, id):
		self.studentList.append(Student(name,id))
		return "Student -" + self.studentList[-1].getName() + "- Added!"
		
	def addCourse(self, code, units):
		self.courseList.append(Course(code,units))
		return "Course -" + self.courseList[-1].getCode() + "- Added!"
	
	def findStudent(self, id):
		for s in self.studentList:
			if(s.getID() == id):
				return s
		return None
		
	def findCourse(self, code):
		for c in self.courseList:
			if(c.getCode() == code):
				return c
		return None
		
	def checkIfEnrolled(self, id, code):
		s = self.findStudent(id)
		c = self.findCourse(code)
		
		if(s == None or c == None):
			print("\nInvalid Entry!\n")
			return False
		else:
			for s in c.getStudentList():
				if(s.getID() == id): 
					return True
		return False
		
	def deleteStudent(self, id):
		for c in self.courseList:
			for s in c.getStudentList():
				if(s.getID() == id):
					c.getStudentList().remove(s)
					
		for s in self.studentList:
			if(s.getID() == id):
				self.studentList.remove(s)
				return "\nStudent -" + s.getName + "- Removed!\n"
		return "\nStudent Not Found!\n"
		
	def deleteCourse(self, code):
		for s in self.studentList:
			for c in s.getCourseList():
				if(c.getCode() == code):
					s.getCourseList.remove(c)
		for c in self.courseList:
			if(c.getCode() == code):
				self.courseList.remove(c)
				return "\nCourse -" + c.getCode + "- Removed! \n"
		return "\nCourse Not Found!\n"
		
	def getStudent(self, id):
		for s in self.studentList:
			if(id == s.getID()):
				return s 
		return None
	
	def getStudentList(self):
		list = []
		for s in self.studentList:
			list.append(s.getName())
		return list
		
	def getCourseList(self):
		list = []
		for c in self.courseList:
			list.append(c.getCode())
		return list
		
	def enrollStudent(self):
		s = self.findStudent(input("Student ID: "))
		c = self.findCourse(input("Course Code:"))
		
		if(s == None or c == None):
			print("Invalid Entry")
		else:
			c.enrollStudent(s)
			s.enrollCourse(c)
			print(s.getName() + "-" + s.getID())
			print("Courses Enrolled:")
			for c in s.getCourseList():
				print(c.getCode())
			
	def dropStudent(self):
		s = self.findStudent(input("Student ID: "))
		c = self.findCourse(input("Course Code:"))
		
		if(s == None or c == None):
			print("Invalid Entry")
		else:
			c.dropStudent(s)
			s.dropCourse(c)
			print(s.getName() + "-" + s.getID())
			print("Courses Enrolled:")
			for c in s.getCourseList():
				print(c.getCode())
			
	def editStudentInfo(self, id):
		s = findStudent(id)
		if (s == None):
			print("Student Not Found!")
		else:
			s.setName(input("New Name: "))
			s.setID(input("New ID: "))

	def editCourseInfo(self, code):
		c = findCourse(code)
		if (c == None):
			print("Course Not Found!")
		else:
			c.setCode(input("New Code: "))
			s.setUnits(input("New Units: "))
			
	def setGrade(self): 
		s = self.findStudent(input("Student ID: "))
		c = self.findCourse(input("Course Code:"))
		
		if(s == None or c == None):
			print("Invalid Entry")
		else:
			if(not self.checkIfEnrolled(s.getID(),c.getCode())):
				print(s.getName() + " is not enrolled in " + c.getCode)
			else:
				grade = input("Set Grade: ")
				s.getGrades().append([c.getCode, grade])
				
	def viewReportCard(self):
		s = self.findStudent(input("Student ID: "))
		
		if(s == None):
			print("\nStudent Not Found!\n")
		else:
			print(s.getName() + "-" + s.getID())
			print("Grades: ")
			for g in s.getGrades():
				print(g[0] + ": " + g[1])
			
	
class Student():
	def __init__(self, name,id):
		self.name = name
		self.id = id
		self.courseList = []
		self.grades = []
	def getName(self):
		return self.name
	def getID(self):
		return self.id
	def getCourseList(self):
		return self.courseList
	def getGrades(self):
		return self.grades
	def enrollCourse(self, c):
		self.courseList.append(c)
	def dropCourse(self, c):
			self.courseList.remove(c)
	def setname(self, name):
		self.name = name
	def setID(self, id):
		self.id = id
	
class Course():
	def __init__(self, code, units):
		self.code = code
		self.units = units
		self.studentList = []
	def getCode(self):
		return self.code
	def getUnits(self):
		return self.units
	def getStudentList(self):
		print("Students Enrolled: ")
		for s in self.studentList:
			print(s.getName)
	def enrollStudent(self, s):
		self.studentList.append(s)
	def dropStudent(self, s):
		self.studentList.remove(s)
	def setCode(self, code):
		self.code = code
	def setUnits(self, units):
		self.units = units
		
def main():
	mls = Database()
	choice1 = 0
	while choice1 != 5:
		print("\nHello User, what would you like to do Today?:")
		print("1. View Students")
		print("2. View Courses")
		print("3. Student Functions")
		print("4. Course Functions")
		print("5. Exit\n")
		
		choice1 = int(input("Select an Item (Pick a Number): "))
		
		if(choice1 == 1):
			print(mls.getStudentList())
		elif(choice1 == 2):
			print(mls.getCourseList())
		elif(choice1 == 3):
			print("\nStudent Functions")
			print("1. Add Student")
			print("2. Delete Student")
			print("3. Edit Student Info")
			print("4. View Report Card")
			print("5. Back\n")
			
			choice2 = int(input("Select an Item (Pick a Number): "))
			
			if(choice2 == 1):
				print(mls.addStudent(input("Student Name: "), input("Student ID: ")))
			elif(choice2 == 2):
				print(mls.deleteStudent(input("Student ID: ")))
			elif(choice2 == 3):
				mls.editStudentInfo("Student ID: ")
			elif(choice2 == 4):
				mls.viewReportCard()
		elif(choice1 == 4):
			print("\nCourse Functions")
			print("1. Add Course")
			print("2. Delete Course")
			print("3. Edit Course Info")
			print("4. Enroll Student")
			print("5. Drop Student")
			print("6. Set Student Grade")
			print("7. Back\n")
			
			choice2 = int(input("Select an Item (Pick a Number): "))
			
			if(choice2 == 1):
				print(mls.addCourse(input("Course Code: "), input("Units: ")))
			elif(choice2 == 2):
				print(mls.deleteCourse(input("Course Code: ")))
			elif(choice2 == 3):
				mls.editCourseInfo("Course Code: ")
			elif(choice2 == 4):
				mls.enrollStudent()
			elif(choice2 == 5):
				mls.dropStudent()
			elif(choice2 == 6):
				mls.setGrade()
		




if __name__ == "__main__":
	main()