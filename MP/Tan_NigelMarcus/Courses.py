class Courses:
    def __init__(self, name, description, units):
        self.name = name
        self.description = description
        self.units = units
        self.studentsList = {}
        self.gradesList = {}
        
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getUnits(self):
        return self.units

    def setCourseCode(self, name):
        self.name = name

    def setUnits(self, units):
        self.units = units
        
    def setDescription(self, description):
        self.description = description
        
    def addStudent(self, name, ID):
        self.studentsList[ID] = name

    def dropStudent(self, name, ID):
        del self.studentsList[ID]

    def getList(self):
        return self.studentsList

    def setGrades(self, grade, ID):
        self.gradesList[ID] = grade
        
    def getGrades(self):
        return self.gradesList
    

