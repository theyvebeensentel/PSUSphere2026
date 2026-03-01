from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class College(BaseModel):
    college_name = models.CharField(max_length=150)

    def __str__(self):
        return self.college_name

class Program(BaseModel):
    prog_name = models.CharField(max_length=150)
    # Renamed from 'college' to 'college_info' to avoid clash
    college_info = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.prog_name

class Organization(BaseModel):
    name = models.CharField(max_length=250)
    # Renamed from 'college' to 'college_info'
    college_info = models.ForeignKey(College, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Student(BaseModel):
    student_id = models.CharField(max_length=15)
    lastname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    # Renamed from 'program' to 'program_info'
    program_info = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

class OrgMember(BaseModel):
    # Renamed fields to 'student_ref' and 'organization_ref'
    student_ref = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization_ref = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField()