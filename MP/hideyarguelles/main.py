# COMET Machine Project
# Catherine Claire M. Arguelles
# 11540680 BSINSYS


from courses import course_home
from students import students_home
from enrolment import enrolment_home
from grades import grades_hub

students = []  # student list
courses = []  # course list

while True:
    print("\nMANAGE: "
          "\n[1] Students"
          "\n[2] Courses"
          "\n[3] Enrolment"
          "\n[4] Grades"  
          "\n[0] Exit Program")
    user_input = input("Enter number: ")

    # For adding, editing, and deleting students.
    if user_input == 1:
        students_home(students)

    # For adding, editing, and deleting courses.
    elif user_input == 2:
        course_home(courses)

    # For enrolling and dropping students from a course.
    elif user_input == 3:
        enrolment_home(students, courses)

    # For viewing and setting grades.
    elif user_input == 4:
        grades_hub(students, courses)

    # For exiting the program.
    elif user_input == 0:
        break

    # For invalid inputs
    else:
        print ("\nInvalid input.")