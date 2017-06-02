from Student import *
from Course import *
from Section import *
from Admin import *
'''
INTRSEC = Course("INTRSEC","Introduction to Security", 3.0)
APP_DEV = Course("APP-DEV","Applications Development with PHP",3.0)
DB_ADMI = Course("DB-ADMI","Database Administration",3.0)
SOCTEC2 = Course("SOCTEC2","Science, Techonology, and Society 2",3.0)

S11 = Section("S11","Ms. Laguna","MW",1430,1600,40,INTRSEC)
S12 = Section("S12","Ms.Laguna","MW",1615,1745,40,INTRSEC)
S13 = Section("S13","Mr. Alain","MW",1430,1600,40,APP_DEV)
S14 = Section("S14","Mr. Alain","MW",1615,1745,40,APP_DEV)
S15 = Section("S15","Mr. Oli", "TH",1100,1230,40,DB_ADMI)
S16 = Section("S16","Mr. Oli", "MW",1100,1230,40,DB_ADMI)

ivy = Student(11407530,pw ="shh",LN ="lim",FN = "Ivy")
ico = Student(11500322,pw ="shh",LN ="zabayle",FN = "Ico")
josh = Student(11507907, pw = "shh", LN = "Cruzada", FN = "Josh")
yuta = Student(11508762, pw = "shh", LN = "Inoue", FN = "Yuta", maxUnits = 21)
'''
admin = Admin()
admin.registerStudent(11508762,"shh","Inoue","Yuta",12,maxUnits = 18)
admin.registerStudent(11407530,pw ="shh",LN ="lim",FN = "Ivy",minUnits=3,maxUnits=18)
admin.registerStudent(11500322,pw ="shh",LN ="zabayle",FN = "Ico",minUnits=3,maxUnits=18)
admin.registerStudent(11507907, pw = "shh", LN = "Cruzada", FN = "Josh",minUnits=3,maxUnits=18)
admin.registerStudent(11502987,pw = "shh",LN="Garcia",FN="Carlos",minUnits=3,maxUnits=18)

admin.editStudent(11407530,"Lim","Ivana")

admin.addCourse("INTRSEC","Introduction to Security", 3.0)
admin.addCourse("APP-DEV","Applications Development with PHP",3.0)
admin.addCourse("DB-ADMI","Database Administration",3.0)
admin.addCourse("SOCTEC2","Science, Techonology, and Society 2",3.0)

for i in range(len(admin.getCourses())):
    if(admin.getCourses()[i].getCode() == "INTRSEC"):
        INTRSEC = admin.getCourses()[i]
    elif(admin.getCourses()[i].getCode() == "APP-DEV"):
        APP_DEV = admin.getCourses()[i]
    elif(admin.getCourses()[i].getCode() == "DB-ADMI"):
        DB_ADMI = admin.getCourses()[i]
    elif(admin.getCourses()[i].getCode() == "SOCTEC2"):
        SOCTEC2 = admin.getCourses()[i]
        
admin.openSection("S11","Ms. Laguna","MW",1430,1600,40,"INTRSEC")
admin.openSection("S12","Ms.Laguna","MW",1615,1745,40,"INTRSEC")
admin.openSection("S13","Mr. Alain","MW",1430,1600,40,"APP-DEV")
admin.openSection("S14","Mr. Alain","MW",1615,1745,40,"APP-DEV")
admin.openSection("S15","Mr. Oli", "TH",1100,1230,40,"DB-ADMI")
admin.openSection("S16","Mr. Oli", "MW",1100,1230,40,"DB-ADMI")

admin.editCourse("IntrSeC","INT-SEC","intro to sec", 4.0)
print("EDITED")
c = admin.getCourses()
for i in range(len(c)):
    print( c[i].getCode())

hehe = admin.getAllStudents()
for i in range(len(hehe)):
    if(hehe[i].getID() == 11407530):
        ivy = hehe[i]
    elif (hehe[i].getID() == 11500322):
        ico = hehe[i]
    elif (hehe[i].getID() == 11507907):
        josh = hehe[i]
    print(hehe[i].getID())
admin.setGrade("S11",11407530,4.0)
print("set grade")
print(ivy.getGPA())
S11 = INTRSEC.getSections()[0]
S12 = INTRSEC.getSections()[1]
S13 = APP_DEV.getSections()[0]
S14 = APP_DEV.getSections()[1]
S15 = DB_ADMI.getSections()[0]
S16 = DB_ADMI.getSections()[1]
#print(isinstance(S11.getCourse(),list))
print(len(S11.getCourse()))
S11.setCourse(S11.getCourse()[0])
S15.setCourse(S15.getCourse()[0])
S14.setCourse(S14.getCourse()[0])
print("enlist time")
ivy.enlistSection("APP-DEV","S11")
print("hehe")
ivy.enlistSection(S14)
ivy.enlistSection(S15)

ico.enlistSection(S11)
ico.enlistSection(S14)
ico.enlistSection(S15)

josh.enlistSection(S11)
josh.enlistSection(S14)
josh.enlistSection(S15)

ivy.enroll()
josh.enroll()
ico.enroll()
admin.removeStudent(11407530)

for i in range(len(hehe)):
    print(hehe[i].getID())
print("\n\n\n")
S11
print(len(S11.getStudents()))
print(S11.getName(),"\n\n\n")
for i in range(len(S11.getStudents())):
    print(S11.getStudents()[i].getID())


admin.removeCourse("INT-SEC")
print("done")

for i in range(len(c)):
    print( c[i].getCode())
'''
INTRSEC.addSection(S11)
INTRSEC.addSection(S12)
APP_DEV.addSection(S13)
APP_DEV.addSection(S14)
DB_ADMI.addSection(S15)
DB_ADMI.addSection(S16)

print(SOCTEC2.getSections())

ivy.enlistSection(S11)
ivy.enlistSection(S14)
ivy.enlistSection(S15)
ivy.enlistSection(S11)
ivy.enlistSection(S14)
ivy.enlistSection(S15)
ha = ivy.getEnlistedSections()
for i in range (len(ha)):
    print(ha[i].getCourse().getCode()," ",ha[i].getName())

ivy.viewEAF()
print(len(ivy.getData()))
for row in ivy.getData():
    for i in row:
        print(i, end=" ")
    print()
    
print(ivy.isEnrolled())

ico.enlistSection(S11)
ico.enlistSection(S14)
ico.enlistSection(S15)

josh.enlistSection(S11)
josh.enlistSection(S14)
josh.enlistSection(S15)

ivy.enroll()
josh.enroll()
ico.enroll()
orayt = S11.getStudents()
for i in range(len(orayt)):
    print(orayt[i].getID())
    
print(S11.removeStudent(ivy))

for i in range(len(orayt)):
    print(orayt[i].getID())
'''

'''
S11.setGrade(josh, 4.0)
S11.setGrade(ico, 7)
josh.viewEAF()
print("\njosh enrolled courses:")
for row in josh.getData():
    for i in row:
        print(i, end=" ")
    print()
S14.viewEnrolledStudents()

yuta.viewEAF()

print("JOSH DROPPED A COURSE")
josh.dropCourse("APP-DEV")
josh.viewEAF()

for row in josh.getData():
    for i in row:
        print(i, end=" ")
    print()

'''
