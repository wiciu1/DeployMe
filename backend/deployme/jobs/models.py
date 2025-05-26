from datetime import timezone

from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=False)

class JobOffer(models.Model):
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    seniority = models.CharField(max_length=10)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technology)
    portal = models.CharField(max_length=100, default='unknown')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


