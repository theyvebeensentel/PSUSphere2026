from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from studentorg.models import Organization
from studentorg.forms import OrganizationForm

# Front page rendering the organization list
class HomePageView(ListView):
    model = Organization
    context_object_name = 'object_list'
    template_name = 'home.html'
    paginate_by = 5

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'object_list'
    template_name = 'org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')