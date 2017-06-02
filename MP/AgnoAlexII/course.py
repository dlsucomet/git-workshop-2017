class Course:
    #attributes
    __courseCode = None
    __units = None

    def __init__(self, courseCode, units):
        self.__courseCode = courseCode
        self.__units = units

    def getCourseCode(self):
        return self.__courseCode

    def getUnits(self):
        return self.__units

    def setCode(self, code):
        self.__courseCode = code

    def setUnits(self, units):
        self.__units = units
    
    
