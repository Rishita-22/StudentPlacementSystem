from django.db import models


class Company(models.Model):
    company_name = models.CharField(
        max_length=100,
        unique=True
    )

    eligibility_criteria = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    package = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Companies"