import os
import sys

class Database():
	def __init__(self):
		self.studentList = []
		self.courseList = []
		self.reportCards = []
		
	def addStudent(self, name, id):
		self.studentList.append(Student(name,id))
		
	def addCourse(self, code, units):
		self.courseList.append(Course(code,units))
	
	def deleteStudent(self, id):
		while s in self.studentList:
			if(s.getID() == id):
				self.studentList.remove(s)
				return "\nStudent Removed!\n"
		return "\nStudent Not Found!\n"
		
	def deleteCourse(self, code):
		while c in self.courseList:
			if(c.getID() == code):
				self.courseList.remove(c)
				return "\nStudent Removed!\n"
		return "\nStudent Not Found!\n"
		
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
				
	
	
class Student():
	def __init__(self, name,id):
		self.name = name
		self.id = id
	def getName(self):
		return self.name
	def getID(self):
		return self.id
	def setname(self, name):
		self.name = name
	def setID(self, id):
		self.id = id
	
class Course():
	def __init__(self, code, units):
		self.code = code
		self.units = units
	def getCode(self):
		return self.code
	def getUnits(self):
		return self.units
	def setCode(self, code):
		self.code = code
	def setUnits(self, units):
		self.units = units

class Grade():
	def __init__(self, course, student, grade):
		self.course = course
		self.student = student
		self.grade = grade

		
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
				mls.addStudent(input("Student Name: "), input("Student ID: "))
			elif(choice2 == 2):
				print("")
			elif(choice2 == 3):
				print("")	
			elif(choice2 == 4):
				print("")
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
				mls.addCourse(input("Course Code: "), input("Units: "))
			elif(choice2 == 2):
				print("")
			elif(choice2 == 3):
				print("")
			elif(choice2 == 4):
				print("")
			elif(choice2 == 5):
				print("")
			elif(choice2 == 6):
				print("")
		




if __name__ == "__main__":
	main()