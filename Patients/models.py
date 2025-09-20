import uuid
from django.conf import settings
from django.db import models
from Files.models import Users, Package


class Staff(models.Model):
    role = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    salary = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Users, related_name="patient_uploaded_by", on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    package_type = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    attending_staff = models.ManyToManyField(Users, null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """USED IN THE  FIRST SIGNALS FUNCTION, NO LONGER USED IN THE CURRENT SIGNALS FUNCTION"""
    def as_dict(self):
        return {
            "id": str(self.id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat(),
        }

    def __str__(self):
        return self.first_name


class CarePlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Users, related_name="careplan_uploaded_by", on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, related_name="patient_careplan", on_delete=models.DO_NOTHING)
    goal_of_plan = models.CharField(max_length=2555, null=True)
    recommendations = models.CharField(max_length=2595, null=True)
    goals = models.CharField(max_length=2559, null=True)
    medications = models.CharField(max_length=2550, null=True)
    relevant_patient_history = models.CharField(max_length=2555, null=True)
    Physical_of_patient = models.CharField(max_length=2555, null=True)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.goal_of_plan


class Reports(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Users, related_name="report_uploaded_by", on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, related_name="patient_report", on_delete=models.DO_NOTHING)
    report = models.CharField(max_length=2555, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id