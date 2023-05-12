from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Case
# Create your views here.
class CaseListView(ListView):
    model = Case
    template_name = "case_list.html"

class CaseDetailView(DetailView):
    model = Case
    template_name = "case_detail.html"

class CaseUpdateView(UpdateView):
    model = Case
    fields = (
        "name",
        "gender",
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
    template_name = "case_edit.html"

class CaseDeleteView(DeleteView):
    model = Case
    template_name = "case_delete.html"
    success_url = reverse_lazy("case_list")

class CaseCreateView(CreateView):
    model = Case
    template_name = "case_new.html"
    fields = (
        "name",
        "gender",
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