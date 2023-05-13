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
    path("", CaseListView.as_view(), name="case_list"),
]
