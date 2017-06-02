class Section:
    'base class for all course sections'
    def __init__(self, name, faculty, sched, start, end, capacity, course):
        self.__students = []
        self.__grades = [] 
        self.__name = name
        self.__faculty = faculty
        self.__sched = sched
        self.__start = start
        self.__end = end
        if(capacity > 0):
            self.__capacity = capacity
        else:
            self.__capacity = 0
        self.__course = course
############### Getters ####################
    def getName(self):
        return self.__name
    def getFaculty(self):
        return self.__faculty
    def getSched(self):
        return self.__sched
    def getStart(self):
        return self.__start
    def getEnd(self):
        return self.__end
    def getCapacity(self):
        return self.__capacity
    def getCourse(self):
        return self.__course
    def getStudents(self):
        return self.__students
    def setCourse(self,course):
        self.__course = course
############### Others ####################
    def addStudent(self,student):
        check = True
        if(len(self.__students) == 0):
            self.__students.append(student)
            self.__grades.append(0.0)

        else:
            for i in range (len(self.__students)):
                if(self.__students[i].getID() == student.getID()):
                    check = False

            if (check):
                self.__students.append(student)
                self.__grades.append(0.0)
                #print("student added to section!")

            else:
                print("Student is already enlisted in this section.")
        return check
    
    def removeStudent(self,student):
        isRemoved = False
        for i in range(len(self.__students)):
            if(student.getID() == self.__students[i].getID()):
                s = self.__students[i]
                #ind = i
                isRemoved = True
        if(isRemoved):
            self.__students.remove(s)
            #print("Successful!")
        else:
            print("Could not find student.")
        #del self.__students[ind]
                               
        return isRemoved
    
    def getStudents(self):
        return self.__students
    
    def getGrade(self, student):
        for i in range(len(self.__students)):
            if (self.__students[i].getID() == student.getID()):
                #print("found student")
               # print(len(self.__grades))
                #print(len(self.__students))
                return self.__grades[i]
        return
    
    def setGrade(self, student, grade):
        isGradeSet = False
        if(grade > 4.0 or grade < 0.0):
            print("Enter a grade between 0.0 and 4.0 only.")
            return False
        for i in range(len(self.__students)):
            if (self.__students[i].getID() == student):
                self.__grades[i] = grade
                isGradeSet = True
        if(isGradeSet):
            print("Grade changed!")
            return True
        else:
            print("Grade not changed.")
            return False
        return isGradeSet
    
    def isConflict(self,section):
        check = False
        if (self.getSched().lower() == section.getSched().lower()):
            if(section.getStart() <= self.getEnd() and
               section.getStart() >= self.getStart() or
               section.getEnd() >= self.getEnd() and
               section.getEnd() <= self.getEnd()):
                check = True
                
        return check
    
    def viewEnrolledStudents(self):
        print("\nCOURSE CODE:\t",self.getCourse().getCode())
        print("SECTION:\t",self.getName())
        print("list List of Enrolled Students:\n")

        for k in range(len(self.__students)):
            print(str(self.__students[k].getID())+"\t"+self.__students[k].getLN()+", "+self.__students[k].getFN())
        print("\nList of students enroled:\t",str(len(self.__students)))
        print("Total number of slots:\t\t",str(self.getCapacity()))
        print("number of slots remaining:\t", str(self.getCapacity()-len(self.__students)))
        return
