from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Case,Family_Member, Family_Expenses, Family_Income, Medical_Expenses, Notes
from django import forms
from .forms import CaseForm, Family_MemberForm

# Create your views here.
class CaseListView(ListView):
    model = Case
    template_name = "case_list.html"


class CaseDetailView(DetailView):
    model = Case
    template_name = "case_detail.html"
    context_object_name = 'case'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        case = self.get_object()
        family_members = Family_Member.objects.filter(case=case)
        family_income = Family_Income.objects.filter(case=case)
        family_expenses = Family_Expenses.objects.filter(case=case)
        medical_expenses = Medical_Expenses.objects.filter(case=case)
        notes = Notes.objects.filter(case=case)
        
        context['family_members'] = family_members
        context['family_income'] = family_income
        context['family_expenses'] = family_expenses
        context['medical_expenses'] = medical_expenses
        context['notes'] = notes
        return context


class CaseUpdateView(UpdateView):
    model = Case
    fields = (
        "name",
        "gender",
        "job",
        "region",
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
    form_class = CaseForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
