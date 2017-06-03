class StudentMenus:
    def readStudents():
        studentList = {}

        file = open("students.txt", "r")

        for line in file:
            studentList[line[line.find(",") + 1: line.find("\n")]] = line[0: line.find(",")]

        students = sorted(studentList)

        for val in students:
            for val2 in studentList:
                if (val == val2):
                    print (val, studentList[val])
                    break
                
        file.close()
        return studentList

    def writeStudents(studentList):
        file = open("students.txt", "w")
        
        for val in studentList:
            file.write(studentList[val])
            file.write(",")
            file.write(val + "\n")

        file.close()

    def addStudents():
        try:
            IDcount = open("ID.txt","r")
            ID = int(IDcount.readline())
            IDcount.close()
        except Exception:
            ID = 11800000
        
        student = input("\nEnter student name: ")
        
        file = open("students.txt", "a")
        
        file.write(student)
        file.write(",")
        file.write(str(ID) + "\n")
        
        file.close()  

        ID += 1
        IDcount = open("ID.txt", "w")
        IDcount.write(str(ID))
        IDcount.close()
        
        usrData = input("Add another student? (Y/N) ")
        
        if (usrData.upper() != "N"):
            StudentMenus.addStudents()

    def editStudents():
        studentList = StudentMenus.readStudents()
        
        idnum = input("Enter ID number: ")

        for val in studentList:
            if (idnum == val):
                studentList[val] = input("Enter new name: ")          

        StudentMenus.writeStudents(studentList)
        
        usrData = input("Edit another student? (Y/N) ")

        if (usrData.upper() != "N"):
            StudentMenus.editStudents()

    def deleteStudents():
        studentList = StudentMenus.readStudents()
                
        idnum = input("Enter ID number: ")

        for val in studentList:
            if (idnum == val):
                del studentList[val]
                break
            
        StudentMenus.writeStudents(studentList)
        
        usrData = input("Delete another student? (Y/N) ")

        if (usrData.upper() != "N"):
            StudentMenus.deleteStudents()

