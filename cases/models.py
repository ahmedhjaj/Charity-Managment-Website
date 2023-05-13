from django.db import models
from django.conf import settings
from django.urls import reverse

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

QUALIFICATIONS = [
    ("HS", "High School"),
    ("BA", "Bachelor"),
]

REGIONS = [
    ("BJ", "Borj Al Arab"),
    ("AX", "Alexandria"),
]

# Create your models here.
class Case(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    addDate = models.DateTimeField(auto_now_add=True, )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDERS)
    job = models.CharField(max_length=150)
    region = models.CharField(max_length=2, choices=REGIONS)
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
    
class Family_Member(models.Model):
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDERS)
    age = models.IntegerField()
    qualification = models.CharField(max_length=2, choices=QUALIFICATIONS)
    occubation = models.CharField(max_length=150)
    notes = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

    
class Family_Income(models.Model):
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
    )
    source_name = models.CharField(max_length=150)
    amount = models.IntegerField()
    def __str__(self):
        return self.name


class Family_Expenses(models.Model):
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
    )
    statement = models.CharField(max_length=150)
    amount = models.IntegerField()
    notes = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    
class Medical_Expenses(models.Model):
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
    )
    fullName = models.CharField(max_length=255)
    diseaseType = models.CharField(max_length=2, choices=GENDERS)
    medicine = models.CharField(max_length=150)
    insuranceID = models.IntegerField()

    def __str__(self):
        return self.name


    
class Notes(models.Model):
    humanNeeds = models.CharField(max_length=300)
    otherHelp = models.CharField(max_length=300)
    interviewDescription = models.CharField(max_length=300)
    interviewResult = models.CharField(max_length=300)
    researcherOpinion = models.CharField(max_length=300)
    supervisorOpinion = models.CharField(max_length=300)
    overallRating = models.CharField(max_length=300)

    def __str__(self):
        return self.name


