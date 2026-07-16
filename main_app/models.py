from django.db import models

from django.db import models

class Lecturer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="სახელი")
    last_name = models.CharField(max_length=50, verbose_name="გვარი")
    email = models.EmailField(unique=True, verbose_name="ელ.ფოსტა")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="კურსის დასახელება")
    description = models.TextField(blank=True, null=True, verbose_name="აღწერა")
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses", verbose_name="ლექტორი")

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="სახელი")
    last_name = models.CharField(max_length=50, verbose_name="გვარი")
    email = models.EmailField(unique=True, verbose_name="ელ.ფოსტა")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="რეგისტრაციის თარიღი")
    courses = models.ManyToManyField(Course, related_name="students", verbose_name="კურსები")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
