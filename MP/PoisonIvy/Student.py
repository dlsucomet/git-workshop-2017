class Student:
    'Base class for all students'
    def __init__(self, idNo, pw, LN, FN, minUnits, maxUnits, isEnrolled = False):
        self.__idNo = idNo
        self.__pw = pw
        self.__FN = FN
        self.__LN = LN
        self.__units = 0.0
        if(minUnits > 0):
            self.__minUnits = minUnits
        else:
            self.__minUnits = 3
        if(maxUnits > 0):
            self.__maxUnits = maxUnits
        else:
            self.__maxUnits = 18
        self.__isEnrolled = isEnrolled
        self.__enlistedSections = []
        self.__data = []
        self.__admin = None
############### Getters ####################
    def getID(self):
        return self.__idNo
    def getPW(self):
        return self.__pw
    def getFN(self):
        return self.__FN
    def getLN(self):
        return self.__LN
    def getMin(self):
        return self.__minUnits
    def getMax(self):
        return self.__maxUnits
    def getEnlistedSections(self):
        return self.__enlistedSections
    def getData(self):
        return self.__data
    def getGPA(self):
        gpa = 0
        units = 0
        for section in self.__enlistedSections:
            gpa += (float(section.getGrade(self)) * section.getCourse().getUnits())
            units += section.getCourse().getUnits()
        if(units == 0):
            units = 1
        gpa = (gpa/units)
        return gpa
############### Setters ####################
    def setFN(self,str):
        self.__FN = str
    def setLN(self,str):
        self.__LN = str
    def setMin(self,n):
        if(n > 0):
            self.__minUnits = n
    def setMax(self,n):
        if(n > 0):
            self.__maxUnits = n
    def setAdmin(self,admin):
        self.__admin = admin
############### Others ####################     
    def isEnrolled(self):
        return self.__isEnrolled
    
    def enlistSection(self,course,sect):
        bCheck = False
        #print(len(self.__admin.getCourses()))####
        for i in self.__admin.getCourses():
            if(course.lower() == i.getCode().lower()):
                for j in i.getSections():
                    if j.getName().lower() == sect.lower():
                        x = j
                        section = x
                        bCheck = True
        if(bCheck):
            if(self.__isEnrolled == False and section.getCapacity() != len(section.getStudents())):
                check = True
                
                for i in range (len(self.__enlistedSections)):
                    if(section.getCourse().getCode().lower() == self.__enlistedSections[i].getCourse().getCode().lower()):
                        check = False
                        print("Unsuccessful enlistment: The student has has duplicate courses.")
                        return False
                    
                for i in range (len(self.__enlistedSections)):
                    if(section.isConflict(self.__enlistedSections[i])):
                        check = False
                        print("Unsuccessful enlistment: The student has conflicts in schedule.")
                        return False
                if (check):
                    self.__enlistedSections.append(section)
                    
                    print("Successful Enlistment:",section.getCourse().getCode(),section.getName())
                    return True
            else:
                print("Unsuccessful enlistment: Student is already enrolled or the section is closed.")
                return False
        else:
            print("No such course or section.")
            return False
        
    def removeSection(self, course):
        if(self.__isEnrolled == False):
            for i in range (len(self.__enlistedSections)):
                if (course.lower() == self.__enlistedSections[i].getCourse().getCode().lower()):
                    print("Remove Enslistment","Successful! Enlistment removed: "+
							self.__enlistedSections[i].getCourse().getCode()+" "+self.__enlistedSections[i].getName())

                    self.__enlistedSections[i].removeStudent(self.__ID)
                    return True
        print("Unsuccessful.")
        return False
     
    def enroll(self):
        totalUnits = 0
        if(self.__isEnrolled == False):
            
            for i in range (len(self.__enlistedSections)):
                totalUnits += self.__enlistedSections[i].getCourse().getUnits()
                
            if (totalUnits >= self.__minUnits and totalUnits <= self.__maxUnits):
                self.__isEnrolled = True
                for i in range(len(self.__enlistedSections)):
                    self.__enlistedSections[i].addStudent(self)
                print("Successful Enrollment!")

            elif(totalUnits < self.__minUnits):
                print("Unsuccessful Enrollment: Student has not reach the minimum number units.")

            elif(totalUnits > self.__maxUnits):
                print("Unsuccessful Enrollment: Student has overloaded maximum number of units.")
            return True
        else:
            print("Unsuccessful Enrollment: Student has already enrolled.")
            return False

    def dropCourse(self, course):
        isDropped = False
        for i in range (len(self.__enlistedSections)):
            if(course.lower() == self.__enlistedSections[i].getCourse().getCode().lower()):
                self.__enlistedSections[i].removeStudent(self)
                del self.__enlistedSections[i]
                print("Course",course.upper(),"successfully dropped!")
                isDropped = True
                self.__isEnrolled = False
                self.viewEAF()
                return True
        return isDropped
    
    def viewEAF(self):
        units = 0
        self.__data = []
        if(not self.isEnrolled()):
            print("Please enroll first to view EAF.")
            return
        for i in range(len(self.__enlistedSections)):
            code = self.__enlistedSections[i].getCourse().getCode()
            course = self.__enlistedSections[i].getCourse().getDesc()
            section = self.__enlistedSections[i].getName()
            faculty = self.__enlistedSections[i].getFaculty()
            sched = (self.__enlistedSections[i].getSched().upper() + " " +
                                 str(self.__enlistedSections[i].getStart()) + " - " +
                                 str(self.__enlistedSections[i].getEnd()))
            units = self.__enlistedSections[i].getCourse().getUnits()
            grade = self.__enlistedSections[i].getGrade(self)
            
            self.__data.append([code, course, section, faculty, sched, units, grade])

        return
        '''
        for i in range(len(self.__enlistedSections)):
            for j in range (7):
                if j == 0:
                    data[i[j]].append(self.__enlistedSections[i].getCourse().getCode())                                                                                                                                                                __enlistedSections[i].getCourse().getCode()
                elif j == 1:
                    data[i[j]] = self.__enlistedSections[i].getCourse().getName()
                elif j == 2:
                    data[i[j]] = self.__enlistedSections[i].getName()
                elif j == 3:
                    data[i[j]] = self.__enlistedSections[i].getFaculty()
                elif j == 4:
                    data[i[j]] = (self.__enlistedSections[i].getSchedule() + " " +
                                 self.__enlistedSections[i].getStart() + " - " +
                                 self.__enlistedSections[i].getEnd())
                elif j == 5:
                    data[i][j] = self.__enlistedSections[i].getCourse().getUnits()
                elif j == 6:
                    data[i][j] = self.__enlistedSections[i].getGrade()

                self.__units += self.__enlistedSections[i].getCourse().getUnits()
                
        
        return
'''
