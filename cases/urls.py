from django.urls import path
from .views import (
    CaseListView,
    CaseDetailView,
    CaseUpdateView,
    CaseDeleteView,
    CaseCreateView,
)


urlpatterns = [
    path("<int:pk>/", CaseDetailView.as_view(), name="case_detail"),
    path("<int:pk>/edit/", CaseUpdateView.as_view(), name="case_edit"),
    path("<int:pk>/delete/", CaseDeleteView.as_view(), name="case_delete"),
    path("new/", CaseCreateView.as_view(), name="case_new"),
    path("", CaseListView.as_view(), name="case_list"),
]
