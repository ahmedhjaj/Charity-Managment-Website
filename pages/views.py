from django.shortcuts import render
from django.views.generic import TemplateView
from cases.models import Case

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        labels_help, data_help = self.get_pie_chart_data_helps()
        labels_regions, data_regions = self.get_pie_chart_data_region()
        context["labels_help"] = labels_help
        context["data_help"] = data_help
        context["labels_regions"] = labels_regions
        context["data_regions"] = data_regions
        return context

    def get_pie_chart_data_helps(self):
        helps = {}
        queryset = Case.objects.all()
        for case in queryset:
            help_key = str(case.typeHelp)  # Convert region to string
            if help_key not in helps:
                helps[help_key] = 0
            helps[help_key] += 1
        labels_help = list(helps.keys())
        data_help = list(helps.values())
        return labels_help, data_help
    def get_pie_chart_data_region(self):
        regions = {}
        queryset = Case.objects.all()
        for case in queryset:
            region_key = str(case.region)  # Convert region to string
            if region_key not in regions:
                regions[region_key] = 0
            regions[region_key] += 1
        labels_regions = list(regions.keys())
        data_regions = list(regions.values())
        return labels_regions, data_regions

    
