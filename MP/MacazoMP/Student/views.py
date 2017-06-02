from django.shortcuts import render
from .models import Student, Course,Grade
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def index(request):
    return render(request, 'Student/index.html')


def listofstudents(request):
    all_students = Student.objects.all()
    context = {
        'all_students': all_students,
    }
    return render(request, 'Student/listofstudents.html', context)


def listofcourses(request):
    all_courses = Course.objects.all()
    context = {
        'all_courses': all_courses,
    }
    return render(request, 'Student/listofcourses.html', context)


def detail(request, student_id):
    all_courses = Grade.objects.filter(student__id_num=student_id)

    counter = 0
    gpa = 0
    for course in all_courses:
        gpa += course.grade
        counter += 1

    if gpa > 0:
        gpa = gpa / counter

    context = {
        'all_courses': all_courses,
        'student_id': student_id,
        'studentname': Student.objects.filter(id_num__exact=student_id).first(),
        'gpa': gpa,
    }
    return render(request, 'Student/studentinfo.html', context)


class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'id_num']


class AddGrades(CreateView):
    model = Grade
    fields = ['course', 'student', 'grade']


class CourseCreate(CreateView):
    model = Course
    fields = ['course_code', 'units']
