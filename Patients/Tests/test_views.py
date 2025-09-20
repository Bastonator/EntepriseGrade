from django.test import TestCase
from Patients.views import PatientView
from Patients.models import Patient
from django.urls import reverse
from Files.models import Users
from rest_framework.test import APIClient
import pytest
import json


"""TEST DONE USING DJNAGO TESCTCASE"""
class TestUnauthenticatedViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Users.objects.create_user(email="e@e.com", password="password1739")
        self.patient = Patient.objects.create(first_name="eddy", phone=7363332,
                                         age=27, user=self.user)
        """TESTING TO SEE OF WE USE CREATE USER AGAIN FOR A USER THATS ALREADY CREATED
         WILL DTATABASE BE AFFECTED?"""
        """ANSWER TO ABOVE QUESTION IS THAT THE TEST DATABASES IA AUTOMATICALLY DLETED, 
        DIDNT NOTICE IT BEING EXPLICICTLY STATED ON THE TERMINAL"""
        self.url = reverse("patient-detail", kwargs={"pk": str(self.patient.id)})
        self.add_url = reverse("add-patient")

    def test_patient__detail_view_isOK(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_add_patient_with_loging(self):
        response = self.client.get(self.add_url)
        self.assertEquals(response.status_code, 401)


class TestAuthenticatedViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Users.objects.create_user(email="e@e.com", password="password1739")
        """TESTING TO SEE OF WE USE CREATE USER AGAIN FOR A USER THATS ALREADY CREATED
         WILL DTATABASE BE AFFECTED?"""
        """ANSWER TO ABOVE QUESTION IS THAT THE TEST DATABASES IA AUTOMATICALLY DLETED, 
        DIDNT NOTICE IT BEING EXPLICICTLY STATED ON THE TERMINAL"""
        self.url = reverse("add-patient")
        self.client.force_authenticate(user=self.user)
        """WILL TRY FORCE_LOGIN AFTER
        NOTE: CLIENT.FORCE_LOGIN DOESNT WORK IN TESTCASES"""
        """ANOTHER NOTE: FORCE LOGIN DOES NOT WORK ONLY USE USER AUTHETICATE WITH DRF"""
    def test_add_patient_with_login(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)


"""TEST BEING DONE USING PYTEST"""
@pytest.mark.django_db
def test_patient_detail_view_isOK_onPytest(client):
    user = Users.objects.create_user(email="e@e.com", password="password1739")
    patient = Patient.objects.create(first_name="eddy", phone=7363332,
                                          age=27, user=user)
    url = reverse("patient-detail", kwargs={"pk": str(patient.id)})
    """I PREFER REVERSE FOR MY URLS BECAUSE IT FREVENT ME WRITING THE FULL URL LINK,
    BUT ITS EASY TO FORGET THAT ITS A LINK BECAUSE IT HAS NO ARGUMENTS DIRECTLY ON THE LINK STRING"""

    response = client.get(url)
    assert response.status_code == 200


"""ASSESSING IF ERROR WHEN THERE IS NO AUTHETICATED USER"""
@pytest.mark.django_db
def test_patientview_isOK_onPytest():
    client = APIClient()
    user = Users.objects.create_user(email="e@e.com", password="password1739")
    client.force_authenticate(user=user)
    """FORCE LOGIN DOES NOT WORK ONLY USE USER AUTHETICATE"""
    url = reverse("add-patient")
    """I PREFER REVERSE FOR MY URLS BECAUSE IT FREVENT ME WRITING THE FULL URL LINK,
    BUT ITS EASY TO FORGET THAT ITS A LINK BECAUSE IT HAS NO ARGUMENTS DIRECTLY ON THE LINK STRING"""

    response = client.get(url)
    assert response.status_code == 200