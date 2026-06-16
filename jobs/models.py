from django.db import models
from companies.models import Company


class JobPosting(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    deadline = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.company.company_name}"

    class Meta:
        verbose_name_plural = "Job Postings"