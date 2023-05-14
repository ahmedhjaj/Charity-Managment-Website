from django import forms

from .models import Case, Family_Member, Regions

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = (
        "name",
        "gender",
        "job",
        "region",
        "typeHelp",
        "marriageStatus",
        "birthDate",
        "nationalID",
        "nationalIDExpiration",
        "qualification",
        "phoneNumber",
        "gaurdianName",
        "gaurdianRelation",
        "gaudrianNumber",
        "housing",
        "caseDescribtion",
        )
        widgets = {
            "birthDate": forms.DateInput(attrs={"type": "date"}),
            "nationalIDExpiration": forms.DateInput(attrs={"type": "date"}),
        }

class Family_MemberForm(forms.ModelForm):
    class Meta:
        model = Family_Member
        fields = (
        "name",
        "gender",
        "age",
        "qualification",
        "occupation",
        "notes",
        )
        