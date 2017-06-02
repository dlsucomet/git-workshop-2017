from Student import *
from Course import *
from Section import *

class Admin:
    'Base class of the OUR'
    def __init__(self):
        self.__usrName = "admin"
        self.__pw = "DLSU"
        self.__courses = []
        self.__allStudents = []

    
############### Getters ####################
    def getCourses(self):
        return self.__courses
    def getAllStudents(self):
        return self.__allStudents

############### Others ####################
    def registerStudent(self,idNo, pw, LN, FN, minUnits, maxUnits):
                
        if(idNo > 99999999 or idNo < 10000000):
            print("ID number should have 8 digits.")
            
        elif (minUnits > 0 and maxUnits > 0 and minUnits <= maxUnits):
            if len(self.__allStudents) == 0:
                s = Student(idNo,pw,LN,FN,minUnits,maxUnits)
                s.setAdmin(self)
                self.__allStudents.append(s)
                print("Successful Registration!")
            else:
                
                check = True
                for i in range (len(self.__allStudents)):
                    if(self.__allStudents[i].getID() == idNo):
                        check = False
                if(check):
                    self.__allStudents.append(Student(idNo,pw,LN,FN,minUnits,maxUnits))
                    
                    print("Successful! Student added!")
                    return True
                else:
                    print("The student is already registered.")
                    return False
        else:
            print("Invalid inputs.")
            return False

    def editStudent(self,idNo, LN, FN,minU,maxU):
        check = False
        for i in range (len(self.__allStudents)):
            if(self.__allStudents[i].getID() == idNo):
                self.__allStudents[i].setFN(FN)
                self.__allStudents[i].setLN(LN)
                self.__allStudents[i].setMin(minU)
                self.__allStudents[i].setMax(maxU)
                check = True
        if(check):
            print("Successful! Student info edited: ")
            return True
        else:
            print("Could not find student with ID no. "+str(idNo)+".")
            return False

    def removeStudent(self,idNo):#remove part not done
        check = False
        s = None
        for i in range (len(self.__allStudents)):
            if(self.__allStudents[i].getID() == idNo):
                s = self.__allStudents[i]
                for j in range (len(s.getEnlistedSections())):
                    ss = s.getEnlistedSections()[j].getStudents()
                    ss.remove(s)
                check = True
        if(check):
            print("Successful! Student deleted!")
            self.__allStudents.remove(s)
            return True
        else:
            print("Could not find student with ID no. "+str(idNo)+".")
            return False
    
    def addCourse(self,code, name, units):
        if (len(code) == 7 and (units >= 0.0 and units <= 4.0)):
            check = True
            for i in range(len(self.__courses)):
                if(self.__courses[i].getCode().lower() == code.lower()):
                    print("The course already exists.")
                    check = False
                    return
            if(check):
                self.__courses.append(Course(code, name, units))
                print("Successful! Course Added!")
                return True
        else:
            print("Invalid input(s). Course code should be 7 characters long and units between 0.0 and 4.0.")
            return False

    def editCourse(self,code,newCode,newDesc,newUnits):
        check = False
        if(len(newCode) != 7 and (newUnits < 0.0 or newUnits > 4.0)):
            print("Course codes should be 7 characters only and units between 0.0 and 4.0.")
            return False
        for i in range (len(self.__courses)):
            if(self.__courses[i].getCode().lower() == code.lower()):
                self.__courses[i].setCode(newCode)
                self.__courses[i].setDesc(newDesc)
                self.__courses[i].setUnits(newUnits)
                check = True
        if(check):
            print("Successful! Course edited!")
            return True
        else:
            print("Could not find course with course code no. "+str(code)+".")
            return False

    def removeCourse(self,code):
        check = False
        c = None
        for i in range (len(self.__courses)):
            if(self.__courses[i].getCode().lower() == code.lower()):
                c = self.__courses[i]
                #ci = i
                check = True
        if(check):
            print("Successful! Course deleted!")
            self.__courses.remove(c)
            return True
        else:
            print("Could not find course with course code: "+str(code)+".")
            return False
    
    def openSection(self,name, faculty,sched,start,end,capacity,course):
        if(len(name) <= 3):
            for i in range (len(self.__courses)):
                if(self.__courses[i].getCode().lower() == course.lower()):
                    self.__courses[i].addSection(Section(name, faculty,sched,start,end,
                                                         capacity,self.__courses[i]))
                    return True
        else:
            print("Invalid section format.")
            return False

    def viewClassList(self):#,course, section):
        hehe = self.getAllStudents()
        for i in range(len(hehe)):
            print(hehe[i].getID(),"\t",hehe[i].getLN(),", \t",hehe[i].getFN())
        '''
        for i in range (len(self.__courses)):
            c = self.__courses[i]
            strCode = c.getCode()
            if(strCode.lower() == course.lower()):
                for j in range(len(c.getSections())):
                    s = c.getSections()[j]
                    sectName = c.getSections()[j].getName()
                    if(sectName().lower() == section.lower()):
                        section.viewEnrolledStudents()
        '''
    def viewCourses(self):
        hehe = self.getCourses()
        for i in range(len(hehe)):
            print(hehe[i].getCode(),"\t",hehe[i].getDesc(),"\t",hehe[i].getUnits())

    def setGrade(self, section, idNo, grade):
        check = False
        for i in range(len(self.getAllStudents())):
            if self.__allStudents[i].getID() == idNo:
                for j in self.__allStudents[i].getEnlistedSections():
                    if j.getName().lower() == section.lower():
                        j.setGrade(idNo, grade)
                        check = True
        if(check):
            print("")
        else:
            print("No such section or student.")
############### BONUS ####################
    def saveAllStudents(self):
        #
        return
    def saveAllCourses(self):
        #
        return
    def saveAllSections(self):
        #
        return
    def saveEnrolledStudents(self):
        #
        return
    def loadAllStudents(self):
        #
        return 
    def loadAllCourses(self):
        #
        return
    def loadAllSections(self):
        #
        return
    def loadEnrolledStudents(self):
        #
        return
    
