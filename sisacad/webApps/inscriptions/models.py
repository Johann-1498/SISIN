from django.db import models
from students.models import Student
from workloads.models import Workload, WorkloadLab
import uuid

# Create your models here.

class Inscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    workload = models.ForeignKey(Workload, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.lastnames} {self.student.names} - {self.workload.course.name} {self.workload.group}"
    
class InscriptionLab(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    workload = models.ForeignKey(WorkloadLab, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.lastnames} {self.student.names} - {self.workload.laboratory.name} {self.workload.group}"