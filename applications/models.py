from django.db import models
from students.models import Student
from jobs.models import JobPosting


class Application(models.Model):

    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        JobPosting,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    applied_date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.name} - {self.job.title}"

    class Meta:
        verbose_name_plural = "Applications"