from rest_framework import serializers
from .models import Patient, CarePlan, Reports
from Files.models import Users, Files
from Files.serializers import UserSerilazer


class PatientsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'age',
            'address',
            'attending_staff',
        )


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "user",
            'first_name',
            'last_name',
            'phone',
            "package_type",
            'age',
            'address',
            'attending_staff',
            'gender',
            'created'
        ]
        read_only_fields = ["user"]


class PatientDetailSerializer(serializers.ModelSerializer):
    user = UserSerilazer(read_only=True, many=False)

    class Meta:
        model = Patient
        fields = (
            "id",
            "user",
            'first_name',
            'last_name',
            'phone',
            "package_type",
            'age',
            'address',
            'attending_staff',
            'gender',
            'created'
        )


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "email", "phone_number"]


class CarePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarePlan
        fields = [
            "id",
            "user",
            'patient',
            'goal_of_plan',
            'recommendations',
            "goals",
            'medications',
            'relevant_patient_history',
            'Physical_of_patient',
        ]
        read_only_fields = ["user"]


class CarePlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarePlan
        fields = "__all__"


class CarePlanDetailSerializer(serializers.ModelSerializer):
    user = UserSerilazer(read_only=True, many=False)
    patient = PatientSerializer(read_only=True, many=False)

    class Meta:
        model = CarePlan
        fields = [
            "id",
            "user",
            'patient',
            'goal_of_plan',
            'recommendations',
            "goals",
            'medications',
            'relevant_patient_history',
            'Physical_of_patient',
        ]


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = [
            "id",
            "user",
            'patient',
            'report'
        ]
        read_only_fields = ["user"]