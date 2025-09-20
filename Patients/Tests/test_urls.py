from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from Patients.api import patients, patient_detail
from Patients.views import PatientView
from Patients.models import Patient
from Files.models import Users
import pytest


class TestUrls(SimpleTestCase):

    def test_list_patients_url_existence(self):
        url = reverse('api_patients')
        print(resolve(url))
        self.assertEquals(resolve(url).func, patients)

    def test_patient_create_url_existence(self):
        """SAME AS ABOVE JUST DONE DIFFRERENTLY"""
        url_resolved = resolve(reverse('add-patient'))
        print(url_resolved)
        self.assertEquals(url_resolved.func.view_class, PatientView)


class PatientDetailTests(TestCase):
    """USE TESTCASE HERE BECAUSE SIMPLETESTCASE CANT ALTER DATABASE"""
    def test_patient_detail_url_existence(self):
        user = Users.objects.create_user(email="e@e.com", password="password1739")
        patient = Patient.objects.create(first_name="eddy", phone=7363332,
                                         age=27, user=user)
        url = reverse('patient-detail', kwargs={"pk": str(patient.id)})
        print(resolve(url))
        response = self.client.get(url)
        assert response.status_code == 200
"""GOING TO STOP HERE FOR TESTING, IT IS CLEAR THAT THIS URL TESTCASES WORK
 AND THE REST OF THE URLS MOST LIKELY WILL WORK WITHOUT ISSUE TOO. """