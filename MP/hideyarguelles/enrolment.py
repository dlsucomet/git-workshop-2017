# User determines the action based on the input.
def enrolment_home(students, courses):
    print("\nENROLMENT HUB"
          "\n[1] Enrol Student"
          "\n[2] Drop Student"
          "\n[0] Exit Enrolment Hub")
    decision = input("Enter number: ")

    if decision == 1:
        enrol(students, courses)

    elif decision == 2:
        drop(courses)

    # For exiting the enrolment hub.
    elif decision == 0:
        pass

    # For invalid inputs.
    else:
        print("\nInvalid input.")


# Enrols a student into a class.
def enrol(students, courses):
    print("\nENROL STUDENT\n[0] Exit student enrolment")

    # Selects which student to be enrolled.
    for student in students:
        print("[" + str(students.index(student) + 1) + "] " + student.id_number)
    index = input("\nEnter number: ")

    # Selects which course the selected student will be enrolled in.
    if index > 0:
        print("\nENROL " + str(students[index - 1].id_number) + "\n[0] Exit process")

        for course in courses:
            print("[" + str(courses.index(course) + 1) + "] " + course.course_code)
        course_index = input("\nEnter number: ")

        if course_index > 0:
            print("Student " + students[index - 1].id_number +
                  " enrolled in " + courses[course_index - 1].course_code)
            courses[course_index - 1].enrol_student(students[index - 1])
            students[index - 1].enrol_course(courses[course_index - 1])


# Drops a student from a class.
def drop(courses):
    print("\nDROP STUDENT\n[0] Exit student dropping")

    # Select which course a student will be dropped from.
    for course in courses:
        print("[" + str(courses.index(course) + 1) + "] " + course.course_code)
    index = input("\nEnter number: ")

    # Selects which student from the course will be dropped.
    if index > 0:
        student_index = 0
        print("\nSELECT STUDENT TO DROP FROM " + courses[index - 1].course_code + "\n[0] Exit process")

        for student in courses[index - 1].students:
            student_index = courses[index - 1].students.index(student)
            print("[" + str(student_index + 1) + "] " + courses[index - 1].students[student_index].id_number)
        drop_index = input("\nEnter number: ")

        if drop_index > 0:
            print("\n" + courses[index - 1].students[student_index].id_number +
                  " has been dropped from " + courses[index - 1].course_code)
            courses[index - 1].students[drop_index - 1].drop_course(courses[index - 1])
            del courses[index - 1].students[drop_index - 1]