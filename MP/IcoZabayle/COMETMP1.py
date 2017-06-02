opt1 = 0
students = []
courses = []
chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','-']

while opt1 != 3:
    print()
    print('Welcome! Welcome! Welcome!')
    print()
    print('1. Students')
    print('2. Courses')
    print('3. Exit')
    print()
    
    opt1 = int(input('Enter your choice number: '))
    
    if opt1 == 1:
        while opt1 == 1:
            print()
            print('Students! Students! Students!')
            print()
            print('1. Add Student')
            print('2. Edit Student Info')
            print('3. View Student Report Card')
            print('4. Delete Student')
            print('5. Back')
            print()
            
            opt1 = int(input('Enter your choice number: '))
            
            if opt1 == 1:
                print()
                idNum = input('Enter ID number: ')
                existence = True
                for s in students:
                    for s2 in s:
                        if idNum == s2:
                            existence = False
                if existence:
                    last = input('Enter last name: ')
                    first = input('Enter first name: ')
                    students.append([idNum,last,first])
                    print()
                    print('Student ID number {} was added!'.format(idNum))
                else:
                    print()
                    print('Student ID number already exists!')
            elif opt1 == 2:
                print()
                existStudent = input('Enter existing Student ID number: ')
                existence = False
                editS = 0
                for s in range(len(students)):
                    if existStudent in students[s]:
                        existence = True
                        editS = s
                if existence:
                    print()
                    print('{} - {}, {}'.format(students[editS][0],students[editS][1],students[editS][2]))
                    print()
                    newID = input('Enter new ID number: ')
                    for s in range(len(students)):
                        if newID in students[s] and newID != existStudent:
                            existence = False
                            editS = s
                    if existence == True:
                        students[editS][0] = newID
                        students[editS][1] = input('Enter new last name: ')
                        students[editS][2] = input('Enter new first name: ')
                        print()
                        print('Student info was edited!')
                    else:
                        print()
                        print('Student ID number already exists!')
                else:
                    print()
                    print('Student ID number does not exist!')
                opt1 = 1
            elif opt1 == 3:
                print()
                existStudent = input('Enter existing Student ID number: ')
                existence = False
                editS = 0
                for s in range(len(students)):
                    if existStudent in students[s]:
                        existence = True
                        editS = s
                if existence:
                    na = True
                    gpa = 'NA'
                    for c in range(len(students[editS])):
                        if c > 2:
                            if 'NA' in students[editS][c]:
                                na = False
                    print()
                    print('--------------------------------------')
                    print('{} - {}, {}'.format(students[editS][0],students[editS][1],students[editS][2]))
                    print()
                    print('Course\t\tUnits\t\tGrade')
                    if na and len(students[editS]) > 3:
                        temp = 0.0
                        totalU = 0
                        for c2 in range(len(students[editS])):
                            if c2 > 2:
                                print('{}\t\t{}\t\t{}'.format(students[editS][c2][0],students[editS][c2][1],students[editS][c2][2]))
                                totalU += students[editS][c2][1]
                                temp += students[editS][c2][1] * students[editS][c2][2]
                        gpa = str(round(temp/totalU, 2))
                    elif na == False and len(students[editS]) > 3:
                        for c3 in range(len(students[editS])):
                            if c3 > 2:
                                print('{}\t\t{}\t\t{}'.format(students[editS][c3][0],students[editS][c3][1],students[editS][c3][2]))
                    print()
                    print('GPA: {}'.format(gpa))
                    print('--------------------------------------')
                else:
                    print()
                    print('Student ID number does not exist!')
                opt1 = 1
            elif opt1 == 4:
                print()
                existStudent = input('Enter existing Student ID number: ')
                existence = False
                for s in range(len(students)):
                    if existStudent in students[s]:
                        students.remove(students[s])
                        print()
                        print('Student was deleted')
                        existence = True
                        break
                if existence == False:
                    print()
                    print('Student ID number does not exist!')
                opt1 = 1
            elif opt1 == 5:
                opt1 = 0
            else:
                print()
                print('{} is not in the options.'.format(opt1))
                opt1 = 1
            
    elif opt1 == 2:
        while opt1 == 2:
            print()
            print('Courses! Courses! Courses!')
            print()
            print('1. Add Course')
            print('2. Edit Course Info')
            print('3. Enroll Student in a Course')
            print('4. Drop Student in a Course')
            print('5. Set Student Grade in a Course')
            print('6. Delete Course')
            print('7. Back')
            print()
            
            opt1 = int(input('Enter your choice number: '))

            if opt1 == 1:
                print()
                courseCode = input('Enter Course code (7 char\'s only): ')
                existence = True
                if len(courseCode) == 7:
                    for c in range(len(courses)):
                        if courseCode in courses[c]:
                            existence = False
                    if existence == False:
                        print()
                        print('Course code already exists!')
                    else:
                        validate = True
                        for c in range(len(courseCode)):
                            if courseCode[c] not in chars:
                                validate = False
                                break
                        if validate:
                            units = float(input('Enter number of units  (0-4): '))
                            if (units >= 0 and units <= 4) and units % 0.5 == 0:
                                courses.append([courseCode,units])
                                print()
                                print('Course code {} was added!'.format(courseCode))
                            else:
                                print()
                                print('Excess/Lack of units!')
                        else:
                            print()
                            print('Wrong format for course code')
                else:
                    print()
                    print('Must be 7 characters')
                opt1 = 2
            elif opt1 == 2:
                print()
                existCourse = input('Enter existing course code: ')
                existence = False
                editC = 0
                for c in range(len(courses)):
                    if existCourse in courses[c]:
                        existence = True
                        editC = c
                if existence:
                    print()
                    newCourseCode = input('Enter new Course code (7 char\'s only): ')
                    for c in range(len(courses)):
                        if newCourseCode in courses[c] and newCourseCode != existCourse:
                            existence = False
                            editC = c
                    if existence == True:
                        courses[editC][0] = newCourseCode
                        newUnits = float(input('Enter new number of units (0-4): '))
                        if (units >= 0 and units <= 4) and units % 0.5 == 0:
                            courses[editC][1] = newUnits
                            print()
                            print('Course info was edited!')
                        else:
                            print()
                            print('Excess/Lack of units!')
                    else:
                        print()
                        print('Course code already exists!')
                else:
                    print()
                    print('Course code does not exist!')
            elif opt1 == 3:
                print()
                existCourse = input('Enter existing course code: ')
                existence = False
                editC = 0
                for c in range(len(courses)):
                    if existCourse in courses[c]:
                        existence = True
                        editC = c
                if existence:
                    existStudent = input('Enter existing Student ID number to be enrolled to this course: ')
                    existence = False
                    editS = 0
                    for s in range(len(students)):
                        if existStudent in students[s]:
                            existence = True
                            editS = s
                    if existence:
                        newC = list(courses[editC])
                        newC.append('NA')
                        if newC not in students[editS]:
                            students[editS].append(newC)
                            print()
                            print('Student ID number {} enrolled to the Course {}!'.format(students[editS][0],courses[editC][0]))
                        else:
                            print()
                            print('Student ID number is already in this course!')
                    else:
                        print()
                        print('Student ID number does not exist!')
                else:
                    print()
                    print('Course code does not exist!')
                opt1 = 2
            elif opt1 == 4:
                print()
                existCourse = input('Enter existing course code: ')
                existence = False
                editC = 0
                for c in range(len(courses)):
                    if existCourse in courses[c]:
                        existence = True
                        editC = c
                if existence:
                    existStudent = input('Enter existing Student ID number to be dropped from this course: ')
                    existence = False
                    editS = 0
                    for s in range(len(students)):
                        if existStudent in students[s]:
                            existence = True
                            editS = s
                    if existence:
                        newC = list(courses[editC])
                        newC.append('NA')
                        students[editS].remove(newC)
                        print()
                        print('Student ID number {} dropped from the Course {}!'.format(students[editS][0],courses[editC][0]))
                    else:
                        print()
                        print('Student ID number does not exist!')
                else:
                    print()
                    print('Course code does not exist!')
                opt1 = 2
            elif opt1 == 5:
                print()
                existStudent = input('Enter existing Student ID number: ')
                existence = False
                editS = 0
                for s in range(len(students)):
                    if existStudent in students[s]:
                        existence = True
                        editS = s
                if existence:
                    print()
                    print('Enrolled course(s)')
                    ctr = 1
                    existingCourses = []
                    for ec in range(len(students[editS])):
                        if ec > 2:
                            print('{}. {}'.format(ctr,students[editS][ec][0]))
                            existingCourses.append(students[editS][ec][0])
                            ctr += 1
                    if ctr != 1:
                        print()
                        chosenCourse = input('Enter Course code to be graded: ')
                        if chosenCourse in existingCourses:
                            existence = False
                            for c in range(len(students[editS])):
                                if c > 2:
                                    if chosenCourse in students[editS][c]:
                                        grade = float(input('Enter grade (0-4): '))
                                        if (grade >= 0 and grade <= 4) and grade % 0.5 == 0:
                                            students[editS][c][2] = grade
                                            print()
                                            print('Course code {} was graded'.format(chosenCourse))
                                        else:
                                            print()
                                            print('Incorrect grade input!')
                        else:
                            print()
                            print('Course code is not in the list!')
                    else:
                        print('None')
                else:
                    print()
                    print('Student ID number does not exist!')
                opt1 = 2
            elif opt1 == 6:
                print()
                existCourse = input('Enter existing Course code: ')
                existence = False
                for c in range(len(courses)):
                    if existCourse in courses[c]:
                        courses.remove(courses[c])
                        print()
                        print('Course was deleted')
                        existence = True
                        break
                if existence == False:
                    print()
                    print('Course code does not exist!')
                opt1 = 2
            elif opt1 == 7:
                opt1 = 0
            else:
                print()
                print('{} is not in the options.'.format(opt1))
                opt1 = 2

    elif opt1 == 3:
        print()
        print('Thank you!')
    else:
        print()
        print('{} is not in the options.'.format(opt1))
