from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Case(models.Model):
    GENDERS = [
        ("ML", "Male"),
        ("FE", "Female"),
    ]
    MARRIAGE_STATUS = [
        ("MA", "Married"),
        ("SN", "Signle"),
        ("WO", "Widowed"),
    ]
    GAURDIAN_RELATIONS = [
        ("BR", "Brother"),
        ("SI", "Sister"),
        ("MA", "Mother"),
        ("OT", "Other"),
    ]

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    addDate = models.DateTimeField(auto_now_add=True, )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDERS)
    job = models.CharField(max_length=150)
    marriageStatus = models.CharField(max_length=2, choices=MARRIAGE_STATUS)
    birthDate = models.DateField()
    nationalID = models.CharField(max_length=14)
    nationalIDExpiration = models.DateField()
    qualification = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=150)
    gaurdianName = models.CharField(max_length=255)
    gaurdianRelation = models.CharField(max_length=2, choices=GAURDIAN_RELATIONS)
    gaudrianNumber = models.CharField(max_length=150)
    housing = models.CharField(max_length=255)
    caseDescribtion = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("case_detail", kwargs={"pk": self.pk})
