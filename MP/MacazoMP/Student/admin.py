from django.contrib import admin
from .models import Student
from .models import Course
from .models import Grade

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)
