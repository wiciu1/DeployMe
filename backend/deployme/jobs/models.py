from django.db import models

class JobOffer(models.Model):
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    seniority = models.CharField(max_length=10)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    technologies = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


