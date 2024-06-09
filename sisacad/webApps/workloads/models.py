from django.db import models
import uuid
from teachers.models import Teacher
from courses.models import Course, Laboratory

# Create your models here.

class Workload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.CharField(max_length=1)
    capacity = models.PositiveIntegerField()
    year = models.IntegerField(editable=False)
    semester = models.IntegerField(editable=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.course:
            self.year = self.course.year
            self.semester = self.course.semester
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.course.name} {self.group} - Profesor: {self.teacher.lastnames} {self.teacher.names}"

class WorkloadLab(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.CharField(max_length=1)
    capacity = models.PositiveIntegerField()
    year = models.IntegerField(editable=False)
    semester = models.IntegerField(editable=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.laboratory:
            self.year = self.laboratory.year
            self.semester = self.laboratory.semester
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.laboratory.name} {self.group} - Profesor: {self.teacher.lastnames} {self.teacher.names}"