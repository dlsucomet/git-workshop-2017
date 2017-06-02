

import student
import course
import atexit
from tkinter import *
students = []
courses = []
sno = 11700000
ExitNaPo = False
def viewList():
    print('id no.\tName')
    screen = Tk()
    lab0 = Label(screen, text = str('Student I.D.'), borderwidth=2, relief="solid")
    lab0.grid(row=0,column = 0)
    lab1 = Label(screen, text = 'Student Name', borderwidth=2, relief="solid")
    lab1.grid(row=0,column = 1)
    cnt = 1
                
    for i in students:
        print('[{}]\t{}'.format(i.getCode(),i.getName()))
        lab0 = Label(screen, text = str(i.getCode()))
        lab0.grid(row=cnt,column = 0)
        lab1 = Label(screen, text = str(i.getName()))
        lab1.grid(row=cnt,column = 1)
        cnt = cnt+1

def editStudent():
    viewList()
    inpt = input('Enter Student ID to edit his/her info: ')
    try:
        stud = checkIfExist(inpt,students)
        
        if (stud is None) == False:
            print('''
1 - Edit Name
2 - Edit student ID number
''')
            command = input('Enter command: ')
            if (command == '1'):
                newname = input('Enter new name for ['+inpt+']')
                stud.setName(newname)
            elif (command == '2'):
                try:
                    idno = int(input('Enter new ID number:'))
                    ghoststud = checkIfExist(idno,students)
                    if(ghoststud is None):
                        print('Name changed')
                        stud.setId(idno)
                    else:
                        print('Student already exists!')
                except:
                    print('Please enter an integer')
        else:
            print('Error: the student does not exist!')
    except:
        print('Error: something went wrong :)')
def deleteStudent():
    idno = input('Enter I.D. number: ')
    stud = checkIfExist(idno,students)
    if(stud is None):
        print('Student does not exist')
        return False
    for i in courses:
        if stud.checkIfStudentIsHere(i.getCode()):
            i.dropStudent2(stud)
    students.remove(stud)
        
        
def studentEdit():
    global sno,students
    command = ''
    while(command.lower() != 'x'):
        print('''
1 - Create student account
2 - Edit student info
3 - Delete student
4 - View students
X - Cancel
''')
        command = input('Enter command: ')
        if (command == '1'):
            try:
                idno = int(input('Enter id of student: '))
                name = input('Enter name of student: ')
                if(checkIfExist(idno, students) is None):
                    newst = student.student(name,idno)
                    students.append(newst)
                else:
                    print('Student already exists')
            except:
                print('please enter an ID number')
            
        elif (command == '2'):
            editStudent();
        elif (command == '3'):
            deleteStudent()
        elif (command == '4'):
            viewList()
        else:
            print('invalid po')


def followsFormat(chicken,nuggets):
    for i in chicken:
        if(i not in nuggets):
            return False
    return True

#yez i agree I can use contains method but [insert excuse here]
def checkIfExist(chicken,nuggets):
    for i in nuggets:
        if(str(chicken) == str(i.getCode())):
            return i
    return None

def removeFromList(obj, lst):
   print('') 

def GetTriggeredWithMyMethodNames():
    ccode = input('Enter course code:')
    corth = checkIfExist(ccode,courses)
    if(corth is None):
        print('Course does not exist!')
        return None,None
    studid = input('Enter I.D. number:')
    stud = checkIfExist(studid,students)
    if(stud is None):
        print('Student does not exist!')
        return None,None
    return corth,stud

    
#the spaghetti starts here hehe xd ingay ksi ng prof    
def courseEdit():
    command = ''
    while(command.lower() != 'x'):
        print('''
1 - Create course
2 - Edit course info
3 - Delete course
4 - Enroll student
5 - Drop student
6 - Edit Grade
7 - Dsiplay CRF of student
8 - View top Notchers of a course
X - Cancel
''')
        norm = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','-']
        command = input('Enter command: ')
        if(command == '1'):
            ccode = input('Enter course code: ')
            if(len(ccode) != 7 or  followsFormat(ccode, norm) == False):
                print('Invalid input')
                return False
            try:
                units = float(input('Enter unit: '))
                if(units > 4 or units < 0 or units%0.5 != 0):
                    print('Invalid input')
                    return False
                
                if (checkIfExist(ccode, courses) is not None):
                    print('Course code already taken!') 
                    return False
                courses.append(course.course(ccode,units))
                print('Course Added!')
            except:
                print('please put a floating number for units.')
        elif (command == '2'):
            ccode = input('Enter course code: ')
            corth = checkIfExist(ccode, courses)
            if (corth is None):
                print('Course does not exist!')
                return False
            print('''
1. Edit Course Code
2. Edit Units
''')
            command2 = input('Enter command: ')
            if(command2 == '1'):
                
                IamStressed = input('Enter Mo to: ')
                if(len(IamStressed) != 7 or  followsFormat(IamStressed, norm) == False):
                    print('Invalid input')
                    return False
                if (checkIfExist(IamStressed, courses) is not None):
                    print('Course code already taken!') 
                    return False
                corth.setCode(IamStressed)
                print('Course Code changed!')
            elif(command2 == '2'):
                IamStressed = input('Enter units: ')
                if(IamStressed != 'floating' and IamStressed != '0' and IamStressed != '0.5' and IamStressed != '1' and IamStressed != '2' and IamStressed !='3' and IamStressed != '4'):
                    print('Invalid input')
                    return False
                corth.setUnits(IamStressed)
                print('Course unit changed!')
            else:
                print('Invalid input!')
        elif (command == '3'):
            ccode = input('Enter course code of the couse you want to remove: ')
            corth = checkIfExist(ccode,courses)
            if (corth is None):
                print('Course does not exist!')
                return False

            for i in students:
                if(i.getClass(ccode) is not None):
                    i.removeClass(ccode)
            courses.remove(corth)
            
        elif (command == '4'):
            
            corth,stud = GetTriggeredWithMyMethodNames()
            if(corth is None or stud is None): return False
            if(stud.checkIfStudentIsHere(corth.getCode())):
                print('Student is already enrolled!')
                return False
            print(str(stud.getCode()) + ' is now enrolled to '+str(corth.getCode()))
            corth.addStudent(stud,0)
        elif(command == '5'):
            corth,stud = GetTriggeredWithMyMethodNames()
            if(corth is None or stud is None): return False
            truth = corth.dropStudent(stud)
            if (truth == True):
                print ('Student dropped!')
            else:
                print ('Student is not enrolled in that course.')
        elif(command == '6'):
            corth,stud = GetTriggeredWithMyMethodNames()
            if(corth is None or stud is None): return False
            if(stud.checkEnroll(corth.getCode()) == False):
                print('Student is not enrolled in that course!')
                return False
            try:
                grade = float(input('Enter grade for student: '))
                if((grade == 0.0 or grade <= 4.0 and grade >= 1.0) and (grade%0.5==0)):
                    if(stud.editGrade(corth.getCode(),grade)):
                        print('Grades changed!')
                else:
                    print('Invalid grade, please choose a legit Lasallian grade ;)')
            except:
                print('you gave an invalid character input lol')
        elif(command == '7'):
            studid = input('Enter ID # of the student you want to enlist po:')
            stud = checkIfExist(studid,students)
            if(stud is None):
                print('Student does not exist!')
                return False
            stud.displayGrade()
            
        elif(command == '8'):
            ccode = input('Enter course you want a student to enlist into po:')
            corth = checkIfExist(ccode,courses)
            if(corth is None):
                print('Course does not exist!')
                return False
            corth.getTopNotchers()
        elif(command == '9'):
            #y the nuggets doesnt python have RelativeToNull? what is this complicated stuff for making a gui centered? o.o
            screen = Tk()
            lab0 = Label(screen, text = str('Course code'), borderwidth=2, relief="solid")
            lab0.grid(row=0,column = 0)
            lab1 = Label(screen, text = 'Units', borderwidth=2, relief="solid")
            lab1.grid(row=0,column = 1)
            cnt = 1
            for i in courses:
                lab0 = Label(screen, text = str(i.getCode()))
                lab0.grid(row=cnt,column = 0)
                lab1 = Label(screen, text = str(i.getUnits()))
                lab1.grid(row=cnt,column = 1)
                cnt = cnt+1
        else:
            print('invalid po')
            
def main():
    if(1+1==2):
        command = ''
        while (command.lower() != 'x'):
            print('''
1 - Student commands
2 - Course commands
X - Exit
    ''')
            command = input('Enter command: ')
            if(command == '1'):
                studentEdit()
            elif(command == '2'):
                courseEdit()
            elif(command != 'x'):
                print('Invalid input! you have inputed: '+command)
    #except:
       # print('yes')
@atexit.register
def goodbye():
    global ExitNaPo
    if(ExitNaPo == False):
        ExitNaPo = True
        sad = open('Courses.txt', 'w') ##too lazy to append po
        for i in courses:
            sad.write(str(i.getCode())+','+str(i.getUnits()))
            sad.write('\n')

        sad = open('Students.txt', 'w') ##too lazy to append po
        for i in students:
            sad.write(str(i.getCode())+','+str(i.getName()))
            cortheth = list(i.getClasses().values())
            for i in cortheth:
                sad.write(',')
                sad.write(str(i[0].getCode()))
                sad.write(',')
                sad.write(str(i[1]))
            sad.write('\n')
        sad.close()
        

atexit.register(goodbye)
try:
    lishy = open('Courses.txt','r').read().splitlines()
    for i in lishy:
        lishy2 = i.split(',')
        courses.append(course.course(lishy2[0],lishy2[1]))

    lishy = open('Students.txt', 'r').read().splitlines()
    for i in lishy:
        lishy2 = i.split(',')
        stud = student.student(lishy2[1],lishy2[0])
        students.append(stud)
        for i in range(2,len(lishy2)):
            if(i%2 == 0):
                corth = checkIfExist(lishy2[i],courses)
                corth.addStudent(stud,lishy2[i+1])
except:
    None
main()



