import student

class course:
    
    def __init__(self,c,u):
        self.ccode = ""
        self.units = ""
        self.students = []
        self.ccode = c
        self.units = u
    
    def getCode(self):
        return self.ccode

    def getUnits(self):
        return self.units

    def setCode(self, c):
        self.ccode = c

    def setUnits(self, u):
        self.units = u
    
    def addStudent(self, x,y):
        self.students.append(x)
        x.addClass(self,y)
    def dropStudent(self, x):
        stud = None
        for i in self.students:
            if (i == x):
                i.removeClass(self.ccode)
                self.students.remove(i)
                return True
        return False
    def dropStudent2(self, x):
        stud = None
        for i in self.students:
            if (i == x):
                self.students.remove(i)
                return True
        return False
    def getGrade(self, x):
        return self.students[x]

    def getTopNotchers(self):
        midgets = list(map(lambda x: x.getGrade(self.ccode),self.students))
        overAchievers = sorted(range(len(midgets)), key=lambda i: midgets[i], reverse=True)[:5]
        print('Here are the top Notchers:')
        lop = min(5,len(overAchievers))
        for i in overAchievers:
            print(self.students[i].getName()+' with a Grade of '+str(self.students[i].getGrade(self.ccode)))
