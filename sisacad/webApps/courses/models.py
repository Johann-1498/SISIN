from django.db import models
import uuid

YEARS = [
        (1, 'Primero'),
        (2, 'Segundo'),
        (3, 'Tercero'),
        (4, 'Cuarto'),
        (5, 'Quinto')
    ]
SEMESTERS = [
    (1, 'Primer Semestre'),
    (2, 'Segundo Semestre'),
    (3, 'Tercer Semestre'),
    (4, 'Cuarto Semestre'),
    (5, 'Quinto Semestre'),
    (6, 'Sexto Semestre'),
    (7, 'Séptimo Semestre'),
    (8, 'Octavo Semestre'),
    (9, 'Noveno Semestre'),
    (10, 'Décimo Semestre')
]

# Create your models here.
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=100)
    theory_hours = models.DecimalField(max_digits=4, decimal_places=2)
    credits = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    hasLaboratory = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    
    year = models.IntegerField(choices=YEARS, default=1)
    semester = models.IntegerField(choices=SEMESTERS, default=1)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
class Laboratory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    year = models.IntegerField(choices=YEARS, default=1)
    semester = models.IntegerField(choices=SEMESTERS, default=1)
    
    def __str__(self):
        return f"{self.name} - Laboratorio"