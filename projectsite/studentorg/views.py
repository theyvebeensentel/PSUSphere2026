from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import (
    OrganizationForm,
    OrgMemberForm,
    StudentForm,
    CollegeForm,
    ProgramForm,
)


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        
        today = timezone.now().date()
        context["students_joined_this_year"] = (
            OrgMember.objects.filter(date_joined__year=today.year)
            .values("student_ref")
            .distinct()
            .count()
        )
        context["total_organizations"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()
        return context


class OrganizationList(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = 'object_list'
    template_name = 'org_list.html'
    paginate_by = 5
    ordering = ["college_info__college_name", "name"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return qs

class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')


# ================= OrgMember Views =================
class OrgMemberList(LoginRequiredMixin, ListView):
    model = OrgMember
    context_object_name = 'object_list'
    template_name = 'orgmember_list.html'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["student_ref__lastname", "date_joined"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "student_ref__lastname"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(student_ref__firstname__icontains=query) |
                Q(student_ref__lastname__icontains=query) |
                Q(organization_ref__name__icontains=query)
            )
        return qs

class OrgMemberCreateView(LoginRequiredMixin, CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(LoginRequiredMixin, UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(LoginRequiredMixin, DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')


# ================= Student Views =================
class StudentList(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'object_list'
    template_name = 'student_list.html'
    paginate_by = 5

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')


# ================= College Views =================
class CollegeList(LoginRequiredMixin, ListView):
    model = College
    context_object_name = 'object_list'
    template_name = 'college_list.html'
    paginate_by = 5

class CollegeCreateView(LoginRequiredMixin, CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(LoginRequiredMixin, UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(LoginRequiredMixin, DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')


# ================= Program Views =================
class ProgramList(LoginRequiredMixin, ListView):
    model = Program
    context_object_name = 'object_list'
    template_name = 'program_list.html'
    paginate_by = 5

class ProgramCreateView(LoginRequiredMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(LoginRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(LoginRequiredMixin, DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')