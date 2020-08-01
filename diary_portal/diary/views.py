from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

# Create your views here.
class InternListView(LoginRequiredMixin, ListView):
    model = models.Company
    fields = ('CompanyName', 'POC', 'CPOC', 'TopRemark', 'placement')
    paginate_by = 10
    template_name = 'diary/intern_list.html'

class PlacementListView(LoginRequiredMixin, ListView):
    model = models.Company
    fields = ('CompanyName', 'POC', 'CPOC', 'TopRemark', 'placement')
    paginate_by = 10
    template_name = 'diary/placement_list.html'

class RemarksListView(LoginRequiredMixin, ListView):
    model = models.Remarks
    fields = ('company', 'POC', 'CPOC', 'remark', 'datetime')
    paginate_by = 10
    template_name = 'diary/remarks_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(company__pk__exact=self.kwargs.get('pk'))

class CreateRemarkView(LoginRequiredMixin, CreateView):
    model = models.Remarks
    fields = ('company', 'POC', 'CPOC', 'remark')
    success_url = reverse_lazy('intern_list')
    template_name = 'diary/create_remark.html'

class ThanksPage(TemplateView):
    template_name = 'diary/thanks.html'
