from django.contrib import admin
from .models import Case, Family_Member, Family_Income, Family_Expenses, Medical_Expenses, Notes
from import_export import resources

class CaseResource(resources.ModelResource):
    class Meta:
        model = Case

"""data = CaseResource().export()
print(data)"""
# Register your models here.
admin.site.register(Case)
admin.site.register(Family_Member)
admin.site.register(Family_Income)
admin.site.register(Family_Expenses)
admin.site.register(Medical_Expenses)
admin.site.register(Notes)



