from models import Student, Course
from user_input import (
    Choice,
    get_int,
    get_float,
    get_string
)

student_list = []
course_list = []


# STUDENTS
def get_student_course(student):
    print("Enrolled courses:")

    student_courses = [course for course, grade in student.course_grade.items()]
    if not student_courses:
        print("No enrolled courses!")
    else:
        for course in student_courses:
            print(course.code)

        # [print(course) for course in student_courses]

        user_input = get_string("Select course")

        matching_courses = [course for course in student_courses if course.code == user_input]
        if not matching_courses:
            get_student_course(student)

        return matching_courses[0]




def get_student():
    student_id = get_int("Enter ID Number:")
    matching_ids = [student for student in student_list if student.id == student_id]

    if not matching_ids:
        print("You're not in the list!")
        get_student()

    return matching_ids[0]  # Take first student


def enter_student_control_panel(student):

    def enroll_student():

        def enlist():
            course = get_course()
            student.course_grade[course] = None
            print(f"Student {student.name} successfully enrolled to {course.code}")

        def drop():
            course = get_student_course(student)
            del student.course_grade[course]
            print(f"Removed {course.code} from course list")

        enroll_choices = [Choice(name = "Enlist", action = enlist),
                          Choice(name = "Drop", action = drop)]

        Choice.show_choices(enroll_choices)

    def edit_student():
        def edit_name():
            new_name = get_string("Enter your new name")
            student.name = new_name

        def edit_id_number():
            new_id = get_int("Enter your new ID number")
            student.id = new_id

        edit_choices = [Choice(name="Edit name", action=edit_name),
                        Choice(name="Edit ID Number", action=edit_id_number)]

        Choice.show_choices(edit_choices)

    def delete_student():
        student_list.remove(student)
        print("Account successfully deleted!")
        show_student_center()

    def show_student_grades():
        for course, grade in student.course_grade.items():
            grade = grade if grade else "No grade yet"
            print(f"{course.code} - {grade}")

    choices = [Choice(name="Enroll", action=enroll_student),
               Choice(name="Edit Information", action=edit_student),
               Choice(name="Delete Account", action=delete_student),
               Choice(name="Show Grades", action=show_student_grades),
               Choice(name="Log out", action=show_student_center)]

    Choice.show_choices(choices)
    enter_student_control_panel(student)


def show_student_center():
    def show_log_in():
        student = get_student()
        enter_student_control_panel(student)

    def register():
        name = get_string("Enter name")
        id = get_int("Enter ID Number")

        student_list.append(Student(name = name, id = id))
        print(f"Welcome {name}!")

    choices = [Choice(name="Log in", action=show_log_in),
               Choice(name="Register", action=register),
               Choice(name="Main Menu", action=lambda: print())]

    Choice.show_choices(choices)
    show_menu()


#COURSE
def get_course():
    print("Available Courses:")
    [print(course.code) for course in course_list]
    user_input = get_string("Select course")

    matching_courses = [course for course in course_list if course.code == user_input]
    if not matching_courses:
        get_course()

    course = matching_courses[0]
    return course


def show_courses():

    def add_course():
        code = get_string("Enter Code")
        unit = get_int("Enter unit")
        course_list.append(Course(unit = unit, code = code))
        print(course_list[0].code) # TEST

    def edit_course():
        course = get_course()

        def edit_code():
            new_code = get_string("Enter new code")
            course.code = new_code

        def edit_unit():
            new_unit = get_int("Enter new unit")
            course.unit = new_unit

        edit_choices = [Choice(name = "Edit Code", action= edit_code),
                        Choice(name = "Edit Unit", action= edit_unit)]

        Choice.show_choices(edit_choices)

    def delete_courses():
        course = get_course()
        course_list.remove(course)
        print(f"Course {course.code} deleted")

    choices = [Choice(name = "Add", action= add_course),
               Choice(name = "Edit", action= edit_course),
               Choice(name = "Delete", action= delete_courses),
               Choice(name = "Main Menu")]

    Choice.show_choices(choices)
    show_menu()


# GRADES
def show_grades():
    student = get_student()
    course = get_student_course(student)
    grade = get_float("Enter grade")
    student.course_grade[course] = grade


# MENU
def show_menu():
    choices = [Choice(name="Students", action=show_student_center),
               Choice(name="Courses", action=show_courses),
               Choice(name="Grades", action=show_grades),
               Choice(name="Exit", action=lambda: print("You want to leave!"))]

    Choice.show_choices(choices)

show_menu()