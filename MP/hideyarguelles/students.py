from objects import *


# User determines the action based on the input.
def students_home(students):
    print("\nSTUDENT HUB"
          "\n[1] New Student"
          "\n[2] Edit Student"
          "\n[3] Delete Student"
          "\n[0] Exit Student Hub")
    decision = input("Enter number: ")

    if decision == 1:
        add_student(students)

    elif decision == 2:
        edit_student(students)

    elif decision == 3:
        delete_student(students)

    # Exits the student hub.
    elif decision == 0:
        pass

    # For invalid inputs.
    else:
        print("\nInvalid input.")


# Creates a new student and adds it to the student list 'students'.
# A student is identified by its name and ID number.
def add_student(students):
    name = raw_input("\nNEW STUDENT\nEnter name: ")
    id_number = raw_input("Enter ID Number: ")
    students.append(Student(name, id_number))


# Edits an existing student's name and ID number.
def edit_student(students):
    print("\nEDIT STUDENT\n[0] Exit student editing")

    for student in students:
        print("[" + str(students.index(student) + 1) + "] " + student.id_number)
    index = input("\nEnter number: ")

    if index > 0:
        new_name = raw_input("Change " + students[index - 1].name + " to: ")
        new_id = raw_input("Change " + students[index - 1].id_number + " to: ")
        students[index - 1].name = new_name
        students[index - 1].id_number = new_id


# Deletes an existing student by removing it from the student list.
def delete_student(students):
    print("\nDELETE STUDENT\n[0] Exit student deletion")

    for student in students:
        print("[" + str(students.index(student) + 1) + "] " + student.id_number)
    index = input("\nEnter number: ")

    if index > 0:
        print("Deleted student with ID Number " + students[index - 1].id_number)
        del students[index - 1]