from django.db import models
from departments.models import Department


class Student(models.Model):

    SEMESTER_CHOICES = [
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
        (7, 'Semester 7'),
        (8, 'Semester 8'),
    ]

    name = models.CharField(max_length=100)

    roll_number = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    semester = models.IntegerField(
        choices=SEMESTER_CHOICES
    )

    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    skills = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.roll_number})"