from django.contrib import admin
from .models import Case, Family_Member, Family_Income, Family_Expenses, Medical_Expenses, Notes

# Register your models here.
admin.site.register(Case)
admin.site.register(Family_Member)
admin.site.register(Family_Income)
admin.site.register(Family_Expenses)
admin.site.register(Medical_Expenses)
admin.site.register(Notes)



