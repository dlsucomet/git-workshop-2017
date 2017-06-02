class Student:

    #attributes
    __name = None
    __idNum = None
    __courseDict = None
    __courseEnrolled = None

    #Constructor
    def __init__(self, name, idNum):
        self.__name = name
        self.__idNum = idNum
        self.__courseDict = {}
        self.__courseEnrolled = []

    #Methods
    def getName(self):
        return self.__name

    def getIdNum(self):
        return self.__idNum

    def setName(self, name):
        self.__name = name

    def setIdNum(self, idNum):
        self.__idNum = idNum

    def getCourseDict(self):
        return self.__courseDict

    def setCourseDict(self, courseDict):
        self.__courseDict = courseDict

    def isMyCourse(self, courseCode):
        for x in self.__courseDict:
            if x == courseCode:
                return courseCode

        return "No"

    def enlistACourse(self, courseCode, course):
        if self.isMyCourse(courseCode) == "No":
            print("Enrolled!")
            self.__courseDict[courseCode] = "NGS"
            self.__courseEnrolled.append(course)
        else:
            print("Course is already enrolled.")

    def getCourseCount(self):
        return len(self.__courseDict)

    def getCourseUnits(self, courseCode):
        x = 0
        while x < len(self.__courseEnrolled):
            if self.__courseEnrolled[x].getCourseCode() == courseCode:
                return self.__courseEnrolled[x].getUnits()
            x = x + 1
        return 0
    #
    def displayCoursesEnrolled(self):
        count = 1

        if len(self.__courseDict) is not 0:
            print("Course#: Course Code ; Grade")
            for cs in self.__courseDict:
                print("%d: %s ; %.1f ; %s" %(count, cs, self.getCourseUnits(cs),self.__courseDict.get(cs)))
                count += 1
        else:
            print("The student currently has no courses.")

    def dropCourse(self, courseCode):
        if self.isMyCourse(courseCode) == "No":
            print("Cannot drop %s, because the student is not enrolled in it" % (courseCode))
        else:
            del self.__courseDict[courseCode]
            print("Successfully dropped %s" % (courseCode))

    def addGrade(self, courseCode, grade):
        if self.isMyCourse(courseCode) == "No":
            print("%s does not exist/Student is not currently enrolled in it." %(courseCode))
        else:
            self.__courseDict[courseCode] = grade

    def calculateGPA(self):
        unitsAndGradeProd = 0
        sumOfUnits = 0
        
        #check first if there are no NGS
        for x in self.__courseDict:
            if self.__courseDict.get(x) == "NGS":
                return "TBD"

        #if no ngs, proceed
        for x in self.__courseDict:
            unitsAndGradeProd = unitsAndGradeProd + (float(self.__courseDict.get(x)) * self.getCourseUnits(x))
            sumOfUnits = sumOfUnits + self.getCourseUnits(x)

        return unitsAndGradeProd / sumOfUnits

    def viewReportCard(self):

        if len(self.__courseDict) is not 0:
            for myCourse in self.__courseDict:
                print("-" * 10)
                print("Course: %s" %(myCourse))
                print("Units: %.1f" %(self.getCourseUnits(myCourse)))
                print("Grade: %s" %(self.__courseDict.get(myCourse)))
                

            print("*" * 10)
            print("TERM GPA: ", end=" ")
            print(self.calculateGPA())

