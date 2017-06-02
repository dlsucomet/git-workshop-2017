from objects import *


# User determines the action based on the input.
def course_home(courses):
    print("\nCOURSE HUB"
          "\n[1] New Course"
          "\n[2] Edit Course"
          "\n[3] Delete Course"
          "\n[0] Exit Course Hub")
    decision = input("Enter number: ")

    if decision == 1:
        add_course(courses)

    elif decision == 2:
        edit_course(courses)

    elif decision == 3:
        delete_course(courses)

    # Exits the course hub.
    elif decision == 0:
        pass

    # For invalid inputs.
    else:
        print("\nInvalid input.")


# Creates a new course and adds it to the course list 'courses'.
# A course is identified by its code and units.
def add_course(courses):
    course_code = raw_input("\nNEW COURSE\nEnter course code: ")
    units = input("Enter course units: ")
    courses.append(Course(course_code, units))


# Edits an existing course's code and units.
def edit_course(courses):
    print("\nEDIT COURSE\n[0] Exit course editing")

    for course in courses:
        print("[" + str(courses.index(course) + 1) + "] " + course.course_code)
    index = input("\nEnter number: ")

    if index > 0:
        new_code = raw_input("\nChange " + courses[index - 1].course_code + " to: ")
        new_units = input("Change " + str(courses[index - 1].units) + " to: ")
        courses[index - 1].course_code = new_code
        courses[index - 1].units = new_units


# Deletes an existing course by removing it from the course list.
def delete_course(courses):
    print("\nDELETE COURSE\n[0] Exit course deletion")

    for course in courses:
        print("[" + str(courses.index(course) + 1) + "] " + course.course_code)
    index = input("\nEnter number: ")

    if index > 0:
        print("Deleted course " + courses[index - 1].course_code + " " + str(courses[index - 1].units))
        del courses[index - 1]