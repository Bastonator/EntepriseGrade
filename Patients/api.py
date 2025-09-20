from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Patient, CarePlan, Reports
from .serializers import PatientsListSerializer, PatientSerializer, PatientDetailSerializer, CarePlansSerializer, CarePlanDetailSerializer, ReportSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def patients(request):
    patients = Patient.objects.all().order_by('-created')
    serializer = PatientsListSerializer(patients, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def patient_detail(request, pk):
    patient = Patient.objects.get(pk=pk)
    serializer = PatientDetailSerializer(patient, many=False)

    print(serializer.data)
    return JsonResponse(serializer.data)



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def careplans(request):
    careplan = CarePlan.objects.all()
    serializer = CarePlansSerializer(careplan, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET', 'PUT', 'POST'])
@authentication_classes([])
@permission_classes([])
def careplan_detail(request, pk):
    careplan = CarePlan.objects.get(pk=pk)

    print(f"Received: {pk}")
    if request.method == 'GET':
        serializer = CarePlanDetailSerializer(careplan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("received data", request.data)
        serializer = CarePlanDetailSerializer(careplan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("Validation error", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def reports(request):
    report = Reports.objects.all()
    serializer = ReportSerializer(report, many=True)

    return JsonResponse({
        'data': serializer.data
    })
