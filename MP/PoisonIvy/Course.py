class Course:
    'base class for all courses'
    def __init__(self, code, desc, units = 0.0):
        self.__sections = []
        self.__code = code
        self.__desc = desc
        if(units > 0):
            self.__units = units
        else:
            self.__units = 0
############### Getters ####################
    def getCode(self):
        return self.__code
    def getDesc(self):
        return self.__desc
    def getUnits(self):
        return self.__units
    def getSections(self):
        return self.__sections
    
############### Setters ####################
    def setCode(self,code):
        self.__code = code.upper()
    def setDesc(self,desc):
        self.__desc = desc.upper()
    def setUnits(self,units):
        if(units > 0):
            self.__units = units
############### Others ####################
    def addSection(self,section):
        check = True
        for i in range(len(self.__sections)):
            if(section.getName().lower() == self.__sections[i].getName()):
                check = False
                print("The course already has",section.getName().upper())
                return
        self.__sections.append(section)
        print("Successful! Section Opened!")
        
    def removeSection(selfsection):
        #
        sections.remove(section)
    def getTop5():
        #
        return
