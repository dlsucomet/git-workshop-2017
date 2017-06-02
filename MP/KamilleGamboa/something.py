# JUST A PRACTICE !!!!!!!
#
# class Student:
#     student_list = []
#
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self.courses = {}
#
#     def add_course(self, code, grade):
#         self.courses[code] = grade
#
#
# class Course:
#     def __init__(self, code, units):
#         self.code = code
#         self.units = units
#
#
# # START OF SOMETHING NEW
# student_list = []
# course_list = []
# response = None
#
# while response != 0:
#     s = None
#     print("[1] Students\n[2] Courses\n[3] Grades\n[0] Exit")
#     response = int(input())
#
#     # STUDENTS
#     if response == 1:
#         while s != 0:
#             s_choice = None
#             s2_choice = None
#             s3_choice = None
#             print("[1] Login\n[2] Register\n[0] Main Menu")
#             s = int(input())
#
#             if s == 1:
#                 print("Enter ID Number: ")
#                 id = int(input())
#                 for student in student_list:
#                     if id == student.id:
#                         current_obj = student
#                 print("Hi, " + current_obj.name)  # TEST
#
#                 while s_choice != 0:
#                     print("[1] Enroll\n[2] Edit Information\n[3] Delete Account\n[0] Logout")
#                     s_choice = int(input())
#                     if s_choice == 1:
#                         print("[1] Enlist\n[2] Drop")
#                         choice = int(input())
#
#                         if choice == 1:
#                             print("COURSES OFFERRED\n")
#                             for course in course_list:
#                                 print(course.code + "\t" + str(course.units))
#                             print("Enter Course Code to enroll in: ")
#                             code = raw_input()
#                             grade = 0
#
#                             current_obj.add_course(code, grade)
#                             print("You have succesfully enrolled in " + str(current_obj.courses[code]))  # TEST
#
#                         else:
#                             print("YOUR CURRICULUM AUDIT\n")
#                             for key, value in current_obj.courses.items():
#                                 print (key, value)
#                             # for course in current_obj.courses:
#                             #     print(current_obj.courses.get(Course, default=None))
#                             print("Enter course code to drop: ")
#                             code = raw_input()
#                             del current_obj.courses[code]
#
#                     elif s_choice == 2:
#                         print("Edit [1] Name\n     [2] ID Number")
#                         s2_choice = int(input())
#                         # EDIT NAME
#                         if s2_choice == 1:
#                             print("Type new name: ")
#                             name = raw_input()
#                             setattr(current_obj, 'name', name)
#                             print(current_obj.name)  # TEST
#                         # EDIT ID NUMBER
#                         else:
#                             print("Type new ID Number: ")
#                             id = int(input())
#                             setattr(current_obj, 'id', id)
#                             print(current_obj.id)  # TEST
#
#                     elif s_choice == 3:
#                         print("Are you sure? [1] Yes [2] No: ")
#                         s3_choice = int(input())
#                         if s3_choice == 1:
#                             student_list = [student for student in student_list if student.id != current_obj.id]
#                             for student in student_list:
#                                 print(student.id)
#                             s_choice = 0
#
#             elif s == 2:
#                 # ADD STUDENT
#                 print("Enter name: ")
#                 name = raw_input()
#                 print("Enter ID Number: ")
#                 id = int(input())
#                 courses = None
#
#                 new_student = Student(name, id)
#                 student_list.append(new_student)
#
#                 s = 1
#
#             else:
#                 s = 0
#
#     elif response == 2:
#         print("[1] Add\n[2] Edit\n[3] Delete")
#         c = int(input())
#         # ADD COURSE
#         if c == 1:
#             print("Enter code: ")
#             code = raw_input()
#             print("Enter unit/s: ")
#             unit = int(input())
#             new_course = Course(code, unit)
#             course_list.append(new_course)
#             print(course_list[0].code)  # TEST
#
#         # EDIT COURSE
#         elif c == 2:
#             for course in course_list:
#                 print(course.code)
#                 print("\n")
#
#             print("Enter course code: ")
#             code = raw_input()
#
#             for course in course_list:
#                 if code == course.code:
#                     print(course.code)  # TEST
#                     current_obj = course
#
#             print("Edit [1] Code\n     [2] Unit")
#             edit = int(input())
#
#             if edit == 1:
#                 print("Enter new code: ")
#                 code = raw_input()
#                 setattr(current_obj, 'code', code)
#                 print(current_obj.code)  # TEST
#
#             elif edit == 2:
#                 print("Enter new number of unit/s")
#                 unit = int(input())
#                 setattr(current_obj, 'unit', unit)
#                 print(current_obj.unit)  # TEST
#
#         else:
#             for course in course_list:
#                 print(course.code)
#                 print("\n")
#             # NEEDS ERROR CHECKING
#             print("Enter course code to delete: ")
#             code = raw_input()
#             course_list = [course for course in course_list if course.code != code]
#
#     # GRADES
#     elif response == 3:
#         print("Enter ID Number: ")
#         id = raw_input()
#         print("Enter Course Code: ")
#         code = raw_input()
#         print("Enter Grade: ")
#         grade = float(input())
#
#         for student in student_list:
#             if id == student.id:
#                 student.courses[code] = grade
#
#
#
#
#
#
#
#
#
#
#             #
#     # if response == 1:
#     #     print("[1] Add\n[2] Edit\n[3] Delete")
#     #     s = int(input())
#     #
#     #     # ADD STUDENT
#     #     if s == 1:
#     #         print("Enter name: ")
#     #         name = raw_input()
#     #         print("Enter ID Number: ")
#     #         id = int(input())
#     #
#     #         new_student = Student(name, id)
#     #         student_list.append(new_student)
#     #
#     #     # EDIT STUDENT
#     #     elif s == 2:
#     #         print("Enter ID Number: ")
#     #         id = int(input())
#     #
#     #         for student in student_list:
#     #             if id == student.id:
#     #                 print(student.id) # TEST
#     #                 current_obj = student
#     #
#     #         print("Edit [1] Name\n     [2] ID Number")
#     #         s_edit = int(input())
#     #         # EDIT NAME
#     #         if s_edit == 1:
#     #             print("Type new name: ")
#     #             name = raw_input()
#     #             setattr(current_obj, 'name', name)
#     #             print(current_obj.name) # TEST
#     #         # EDIT ID NUMBER
#     #         else:
#     #             print("Type new ID Number: ")
#     #             id = int(input())
#     #             setattr(current_obj, 'id', id)
#     #             print(current_obj.id) # TEST
#     #
#     #     else:
#     #         for student in student_list:
#     #             print(str(student.id) + "\t" + str(student.name))
#     #
#     #
#     #         # NEEDS ERROR CHECKING
#     #         print("Type the ID number you want to remove from the list: ")
#     #         id = int(input())
#     #
#     #         student_list = [student for student in student_list if student.id != id]
#     #
#     #
#     #
#     #  # COURSES
#     elif response == 2:
#         print("[1] Add\n[2] Edit\n[3] Delete")
#         c = int(input())
#
#         # ADD COURSE
#         if c == 1:
#             print("Enter code: ")
#             code = raw_input()
#
#             print("Enter unit/s: ")
#             unit = int(input())
#
#             new_course = Course(code, unit)
#             course_list.append(new_course)
#             print(course_list[0].code) # TEST
#
#         # EDIT COURSE
#         elif c == 2:
#             for course in course_list:
#                 print(course.code)
#                 print("\n")
#
#             print("Enter course code: ")
#             code = raw_input()
#
#             for course in course_list:
#                 if code == course.code:
#                     print(course.code) # TEST
#                     current_obj = course
#
#             print("Edit [1] Code\n     [2] Unit")
#             edit = int(input())
#             if edit == 1:
#                 print("Enter new code: ")
#                 code = raw_input()
#                 setattr(current_obj, 'code', code)
#                 print(current_obj.code)  # TEST
#
#             elif edit == 2:
#                 print("Enter new number of unit/s")
#                 unit = int(input())
#                 setattr(current_obj, 'unit', unit)
#                 print(current_obj.unit) # TEST
#
#         else:
#             for course in course_list:
#                 print(course.code)
#                 print("\n")
#
#             # NEEDS ERROR CHECKING
#             print("Enter course code to delete: ")
#             code = raw_input()
#             course_list = [course for course in course_list if course.code != code]
#
#     #
#     # # ENROLLMENT
#     # elif response == 3:
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #tests
# test = student_list[0].id
# print(test)
#
# # trial = False
# # while (trial == False):
# #     print("Enter code: ")
# #     code = raw_input()
# #
# #     if len(code) != 7:
# #         print("Course code should be characters")
# #     else:
# #         ctr = 0
# #         trial = False
# #         for letter in code:
# #             if code[ctr] == "-":
# #                 trial = True
#
#
#
#
#
#
#
# # < P50000: 0% tax
# # between 50001 and 100000: 10% tax
# # over 100000: 15%
# #
# # print net income (salary - tax)
#
# # salary = input()
# # if salary < 50000:
#
#
# # print("hello");
# #
# # a = True
# # b = False
# #
# # a = input()
# # print(a)
# #
# # a = input()
# # print(type(a))
# #
# # # if/else statements
# # if condition:
# #     code
# # elif other condition:
# #     code
# # else:
# #     code
#
