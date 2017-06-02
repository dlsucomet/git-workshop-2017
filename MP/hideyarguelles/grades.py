# User determines the action based on the input.
def grades_hub(students, courses):
    print("\nENROLMENT HUB"
          "\n[1] View Student's Grades"
          "\n[2] Set Student's Grades"
          "\n[0] Exit Grades Hub")
    decision = input("Enter number: ")

    if decision == 1:
        view_grades(students)

    elif decision == 2:
        set_grade(students, courses)

    elif decision == 0:
        pass


# Prints a student's courses, grades, and GPA.
def view_grades(students):
    print("\nVIEW GRADES\n[0] Exit viewing grades")

    # Selects the student for viewing of grades.
    for student in students:
        print("[" + str(students.index(student) + 1) + "] " + student.id_number)
    index = input("\nEnter number: ")

    if index > 0:
        students[index - 1].view_grades()


# Sets a student's grade in a particular course.
def set_grade(students, courses):
    print("\nSET GRADE FOR STUDENT\n[0] Exit grading")

    # Selects the student to grade for a particular course.
    for student in students:
        print("[" + str(students.index(student) + 1) + "] " + student.id_number)
    index = input("\nEnter number: ")

    # Selects the course to grade.
    if index > 0:
        print("\nSELECT COURSE TO GRADE FOR ID " + students[index - 1].id_number + "\n[0] Exit process")
        ctr = 1  # counter for loop

        for course in students[index - 1].grades.keys():
            print("[" + str(ctr) + "] " + course.course_code)
            ctr += ctr
        course_index = input("\nEnter number: ")

        if course_index > 0:
            course_code = students[index - 1].grades.keys()[course_index - 1].course_code
            grade = input("\nEnter grade: ")
            print(students[index - 1].id_number + " graded " + str(grade) + " for " + course_code)
            students[index - 1].grades[get_course(course_code, courses)] = grade


# Gets the course with the same code from the course list.
def get_course(course_code, courses):
    for course in courses:
        if course.course_code == course_code:
            return course