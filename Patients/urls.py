from django.urls import path, include
from .views import PatientView, staffreports, StaffDetail, EditStaffReport, staffmembers, CarePlanView, EditCarePlan, CarePlanDetail, DeleteCarePlan, FilesView, DeleteFileView, search_reports,search_files, search_patients, ReportDetail, EditReport, DeleteReport, ReportView
from . import api
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()


urlpatterns = [
    path('', api.patients, name='api_patients'),
    path('add_patient/', PatientView.as_view(), name="add-patient"),
    path('<uuid:pk>/', api.patient_detail, name="patient-detail"),
    path('staff/', staffmembers, name="staff-members"),
    path('staff/<uuid:pk>/', StaffDetail.as_view(), name="staff-detail"),
    path('staff_reports/', staffreports, name="staff-reports"),
    path('files/', FilesView, name="files"),
    path('create_careplan/', CarePlanView.as_view(), name="create-careplan"),
    path('careplan/', api.careplans, name='api_careplans'),
    path('patient_plan/<uuid:pk>/', api.careplan_detail, name="careplan-detail"),
    path('care_plan/<uuid:pk>/', CarePlanDetail.as_view(), name="care-plan"),
    path('edit_careplan/<uuid:pk>/', EditCarePlan.as_view(), name="edit_careplan"),
    path('delete_careplan/<uuid:pk>/', DeleteCarePlan.as_view(), name="delete_careplan"),
    path('delete/<int:pk>/', DeleteFileView.as_view(), name="file_delete"),
    path('search_files', search_files, name="file_search"),
    path('search_patients', search_patients, name="patient_search"),
    path('search_reports', search_reports, name="report_search"),
    path('create_report/', ReportView.as_view(), name="create-report"),
    path('report/<uuid:pk>/', ReportDetail.as_view(), name="report"),
    path('edit_report/<uuid:pk>/', EditReport.as_view(), name="edit_report"),
    ##path('edit_staffreport/<uuid:pk>/', EditStaffReport.as_view(), name="edit_staff_report"),
    path('delete_report/<uuid:pk>/', DeleteReport.as_view(), name="delete_report"),
    path('reports/', api.reports, name='api_reports'),
]
