from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at")
    search_fields = ("college_name",)
    list_filter = ("created_at",)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college_info")
    search_fields = ("prog_name", "college_info__college_name")
    list_filter = ("college_info",)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college_info", "description")
    search_fields = ("name", "description")
    list_filter = ("college_info",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program_info")
    search_fields = ("lastname", "firstname")

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student_ref", "get_member_program", "organization_ref", "date_joined")
    search_fields = ("student_ref__lastname", "student_ref__firstname")

    def get_member_program(self, obj):
        try:
            return obj.student_ref.program_info
        except Exception:
            return None
    
    get_member_program.short_description = 'Program'