from django.db import models

# Create your models here.

class Career(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    length = models.PositiveSmallIntegerField(default=5)
    
    def __str__(self):
        txt = "{0} (Length: {1} year(s))"
        return txt.format(self.name, self.length)

class Student(models.Model):
    dni =  models.CharField(max_length=8, primary_key=True)
    paternallastname = models.CharField(max_length=35)
    maternallastname = models.CharField(max_length=35)
    names = models.CharField(max_length=35)
    birthdate = models.DateField()
    sexes = [('F', 'Female'), ('M', 'Male')]
    sex = models.CharField(max_length=1, choices=sexes, default='F')
    career = models.ForeignKey(Career, null=False, blank=False, on_delete=models.CASCADE)
    vigency = models.BooleanField(default=True)

    def fullname(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.paternallastname, self.maternallastname, self.names)

    def __str__(self):
        txt = "{0} / Career {1} / {2}"
        if self.vigency:
            statusstudent = "Current student"
        else:
            statusstudent = "Not student anymore"
        return txt.format(self.fullname(), self.career, statusstudent)


class Course(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.PositiveSmallIntegerField()
    professor = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1}) / Professor: {2}"
        return txt.format(self.name, self.code, self.professor)

class Tuition(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    tuitiondate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} enrolled in the course {1} / Date: {2}"
        enrolleddate = self.tuitiondate.strftime("%A %d/%m/%Y | %H:%M:%S")
        return txt.format(self.student.fullname(), self.course, enrolleddate)