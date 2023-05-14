from django.contrib import admin
from .models import (
    Case,
    Family_Member,
    Family_Income,
    Family_Expenses,
    Medical_Expenses,
    Notes,
    Regions,
    TypeHelp,
    Comment,
)


class CommentInline(admin.TabularInline):  # new
    model = Comment
    extra = 0 # new


class CaseAdmin(admin.ModelAdmin):  #
    newinlines = [
        CommentInline,
    ]


# Register your models here.
admin.site.register(Case, CaseAdmin)
admin.site.register(Family_Member)
admin.site.register(Family_Income)
admin.site.register(Family_Expenses)
admin.site.register(Medical_Expenses)
admin.site.register(Notes)
admin.site.register(Regions)
admin.site.register(TypeHelp)

