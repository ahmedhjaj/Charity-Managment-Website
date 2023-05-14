from django.urls import path
from .views import (
    CaseListView,
    CaseDetailView,
    CaseUpdateView,
    CaseDeleteView,
    CaseCreateView,
    FamilyMemberCreateView,
    FamilyMemberUpdateView,
    FamilyMemberDeleteView,
    FamilyIncomeCreateView,
    FamilyIncomeUpdateView,
    FamilyIncomeDeleteView,
    FamilyExpensesCreateView,
    FamilyExpensesUpdateView,
    FamilyExpensesDeleteView,
    MedicalExpensesCreateView,
    MedicalExpensesUpdateView,
    MedicalExpensesDeleteView,
    NoteCreateView,
    NoteDeleteView,
    NoteUpdateView,
    DownloadExcelView,
    DownloadAllView,
    AddRegionView,
    AddHelpView
)


urlpatterns = [
    path("<int:pk>/", CaseDetailView.as_view(), name="case_detail"),
    path("<int:pk>/edit/", CaseUpdateView.as_view(), name="case_edit"),
    path("<int:pk>/delete/", CaseDeleteView.as_view(), name="case_delete"),
    path("new/", CaseCreateView.as_view(), name="case_new"),
    path(
        "<int:pk>/family_members/new/",
        FamilyMemberCreateView.as_view(),
        name="member_new",
    ),
    path(
        "<int:case_pk>/family_members/<int:pk>/edit/",
        FamilyMemberUpdateView.as_view(),
        name="member_edit",
    ),
    path(
        "<int:case_pk>/family_members/<int:pk>/delete/",
        FamilyMemberDeleteView.as_view(),
        name="member_delete",
    ),
    path(
        "<int:pk>/family_income/new/",
        FamilyIncomeCreateView.as_view(),
        name="income_new",
    ),
    path(
        "<int:case_pk>/family_income/<int:pk>/edit/",
        FamilyIncomeUpdateView.as_view(),
        name="income_edit",
    ),
    path(
        "<int:case_pk>/family_income/<int:pk>/delete/",
        FamilyIncomeDeleteView.as_view(),
        name="income_delete",
    ),
    path(
        "<int:pk>/family_expenses/new/",
        FamilyExpensesCreateView.as_view(),
        name="expense_new",
    ),
    path(
        "<int:case_pk>/family_expenses/<int:pk>/edit/",
        FamilyExpensesUpdateView.as_view(),
        name="expense_edit",
    ),
    path(
        "<int:case_pk>/family_expenses/<int:pk>/delete/",
        FamilyExpensesDeleteView.as_view(),
        name="expense_delete",
    ),
    path(
        "<int:pk>/medical_expenses/new/",
        MedicalExpensesCreateView.as_view(),
        name="medical_new",
    ),
    path(
        "<int:case_pk>/medical_expenses/<int:pk>/edit/",
        MedicalExpensesUpdateView.as_view(),
        name="medical_edit",
    ),
    path(
        "<int:case_pk>/medical_expenses/<int:pk>/delete/",
        MedicalExpensesDeleteView.as_view(),
        name="medical_delete",
    ),
    path(
        "<int:pk>/note/new/",
        NoteCreateView.as_view(),
        name="note_new",
    ),
    path(
        "<int:case_pk>/note/<int:pk>/edit/",
        NoteUpdateView.as_view(),
        name="note_edit",
    ),
    path(
        "<int:case_pk>/note/<int:pk>/delete/",
        NoteDeleteView.as_view(),
        name="note_delete",
    ),
    path(
        "download-excel/<int:case_id>/",
        DownloadExcelView.as_view(),
        name="download_excel",
    ),
    path(
        "download-excel/all_tables/",
        DownloadAllView.as_view(),
        name="download_all_cases",
    ),
    path('add_region/', AddRegionView.as_view(), name='add_region'),
    path('add_help/', AddHelpView.as_view(), name='add_help'),

    path("", CaseListView.as_view(), name="case_list"),
]
