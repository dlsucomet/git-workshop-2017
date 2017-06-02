from django.db import models
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy


# Create your models here.
#, kwargs={'pk': self.pk}


class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)


class Course(models.Model):
    course_code = models.CharField(max_length=7)
    units = MinMaxFloat(min_value=0.0, max_value=4.0)

    def get_absolute_url(self):
        return reverse('student:index')

    def __str__(self):
        return self.course_code + ' - Units: ' + str(self.units)


class Student(models.Model):
    name = models.CharField(max_length=250)
    id_num = models.CharField(max_length=8)
    course = models.ManyToManyField(Course)

    def get_absolute_url(self):
        return reverse('student:index')

    def __str__(self):
        return self.name + ' - ' + self.id_num


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = MinMaxFloat(min_value=0.0, max_value=4.0)

    def get_absolute_url(self):
        return reverse('student:index')

    def __str__(self):
        return self.course.course_code + ": " + str(self.grade)
