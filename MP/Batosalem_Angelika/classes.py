class student:
	def __init__(self, name, idnum):
		self.name = name
		self.idnum = idnum
		self.courses = []
		self.grades = {}

	def change_name(self, name):
		self.name = name

	def get_id(self):
		return self.idnum

	def get_student_info(self):
		return self.idnum + " \t" +self.name 

	def add_course(self, course):
		self.courses.append(course)

	def remove_course(self, course):
		self.courses.remove(course)

	def display_courses(self):
		print("Course Code \tUnits")
		for y in self.courses:
			print(y.get_course_info())
		print()

	def find_in_grades(self, ccode):
		try:
			self.grades[ccode]
			return True
		except:
			return False

	def find_course(self, course):
		if course in self.courses:
			return True
		return False

	def add_grade(self, ccode, grade):
		self.grades[ccode] = grade

	def print_grade(self):
		transcript = "Course Code \tGrade\n"
		grade = 0
		totalUnits = 0
		gpa = 0
		subj = False
		for x in self.courses:
			try:
				transcript = transcript + x.get_ccode() + " \t" + str(self.grades[x.get_ccode()]) + "\n"
				grade = grade + ((self.grades[x.get_ccode()]) * x.get_units())
				totalUnits = totalUnits + x.get_units()
				subj = True
			except:
				pass
		if subj:
			gpa = grade/totalUnits
			transcript = transcript + "\nGPA:" + str(gpa) +"\n"
		return transcript





class course:
	def __init__(self, code, units):
		self.code = code
		self.units = units
		self.students = []

	def get_course_info(self):
		if self.units != 5:
			return self.code + " \t" + str(self.units)
		return self.code + " \tfloating"

	def get_ccode(self):
		return self.code

	def get_units(self):
		return self.units

	def change_ccode(self, code):
		self.code = code

	def change_units(self, units):
		self.units = units

	def add_student(self, student):
		self.students.append(student)

	def remove_student(self, student):
		self.students.remove(student)

	def display_students(self):
		print("ID#\t\tName")
		for y in self.students:
			print(y.get_student_info())
		print()

	def find_student(self, student):
		if student in self.students:
			return True
		return False

