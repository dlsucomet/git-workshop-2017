from functools import reduce #for extreme lazyness, praise lambda
from tkinter import *
class student:
    
    def __init__(self,n,d):
        self.courses = {}
        self.name = ""
        self.idno = ""
        self.floating = 0
        self.name = n
        self.idno = d

    def getName(self):
        return self.name
    def getCode(self):
        return self.idno
    def setName(self,x):
        self.name = x

    def setId(self,x):
        self.idno = x

    def addClass(self,x,y):
        if(x.getUnits() == 'floating'):
            self.floating = self.floating+1
        self.courses[x.getCode()] = [x, y]
    def checkIfStudentIsHere(self,x):
        for i in self.courses:
            if (i == x):
                return True
        return False
    def getClass(self, x):
        for i in self.courses:
            if (str(x) == str(self.courses[i][0].getCode())):
                return self.courses[x][0]
        return None
    def removeClass(self, x):
        hehe = self.courses
        self.courses.pop(x,None)
        #del self.courses[x]
        
    def getClasses(self):
        return self.courses
    def checkEnroll(self,x):
        try:
            self.courses[x]
            return True
        except:
            return False
    def editGrade(self, x, y):
        self.courses[x][1] = y
        return True

    def getGrade(self, x):
        return self.courses[x][1]
    def cantLambdaThisSad(self,x):
        if(x[0].getUnits() != 'floating'):
            return (float)(x[0].getUnits())
        else:
            return 0
    def displayGrade(self):
        print('REPORT CARD LOL:')
        GPA = 0
        floaters = 0
        try:
            totalUnits = reduce(lambda x,y: (float)(x)+(float)(y), list(map(self.cantLambdaThisSad, list(self.courses.values()))))
            screen = Tk()
            screen.title(self.idno)
            lab0 = Label(screen, text = 'ID number: '+str(self.idno), borderwidth=2, relief="solid")
            lab0.grid(row = 0)
            lab1 = Label(screen, text = 'Student name: '+str(self.name), borderwidth=2, relief="solid")
            lab1.grid(row = 1)
            labx = Label(screen, text = 'Course', borderwidth=2, relief="solid")
            labx.grid(row = 2, column = 0)
            labx = Label(screen, text = 'Grade', borderwidth=2, relief="solid")
            labx.grid(row = 2, column = 1)
            labx = Label(screen, text = 'Unit', borderwidth=2, relief="solid")
            labx.grid(row = 2, column = 2)
            cnt = 3
            for i in self.courses:

                corth = self.courses[i][0]
                lab = Label(screen, text = str(corth.getCode()))
                lab2 = Label(screen, text = str(corth.getUnits()))
                CCCCComboBREAKER = Label(screen, text = str(self.courses[i][1]))
                lab.grid(row = cnt, column = 0)
                CCCCComboBREAKER.grid(row = cnt, column = 1)
                lab2.grid(row = cnt, column = 2)
                
                print(str(corth.getCode())+'\t\t\t'+str(corth.getUnits())+'\t\t\t'+str(self.courses[i][1]))
                if(corth.getUnits() != 'floating'):
                    GPA = float(GPA) + float(self.courses[i][1]) * (float(corth.getUnits())/float(totalUnits))

                cnt = cnt+1
            lab3 = Label(screen, text = 'Total units: '+str(totalUnits), borderwidth=2, relief="solid")
            lab3.grid(row =cnt)
            lab4 = Label(screen, text = 'GPA: '+str(GPA), borderwidth=2, relief="solid")
            lab4.grid(row =cnt+1)
            print('Total units: '+str(totalUnits))
            print('Ll your GPA is: '+str(GPA))
        except Exception as inst:
            print('Not yet enrolled')


