from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Patient, CarePlan, Reports
from Files.models import Users, Files
from .serializers import PatientsListSerializer, PatientSerializer, PatientDetailSerializer, StaffSerializer, CarePlanSerializer, CarePlansSerializer, FileSerializer, ReportSerializer
from Files.serializers import FilesSerializer
from django.db.models import Q


class PatientView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        patient_serializer = PatientSerializer(data=request.data)

        if patient_serializer.is_valid():
            patient_serializer.save(user=request.user)
            return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
        return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        patient = Patient.objects.filter(user=request.user)
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def staffmembers(request):
    staff = Users.objects.all()
    serializer = StaffSerializer(staff, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def staffreports(request):
    reports = Reports.objects.all()
    serializer = ReportSerializer(reports, many=True)

    return JsonResponse({
        'data': serializer.data
    })


class CarePlanView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        careplan_serializer = CarePlanSerializer(data=request.data)

        if careplan_serializer.is_valid():
            careplan_serializer.save(user=request.user)
            return Response(careplan_serializer.data, status=status.HTTP_201_CREATED)
        return Response(careplan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        careplan = CarePlanSerializer.objects.filter(user=request.user)
        serializer = CarePlanSerializer(careplan, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarePlanDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CarePlan.objects.all()
    serializer_class = CarePlanSerializer


class EditCarePlan(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarePlanSerializer
    queryset = CarePlan.objects.all()

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteCarePlan(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarePlanSerializer
    queryset = CarePlan.objects.all()



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def FilesView(request):
    files = Files.objects.all().distinct()
    serializer = FileSerializer(files, many=True)

    return JsonResponse({
        'data': serializer.data
    })


class DeleteFileView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FilesSerializer
    queryset = Files.objects.all()


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def search_files(request):
    query = request.query_params.get("search")
    files = Files.objects.filter(Q(file__icontains=query) | Q(user__email__icontains=query) | Q(user__phone_number__icontains=query))
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def search_patients(request):
    query = request.query_params.get("search")
    patients = Patient.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(address__icontains=query) | Q(attending_staff__email__icontains=query) | Q(id__icontains=query))
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def search_reports(request):
    query = request.query_params.get("search")
    reports = Reports.objects.filter(Q(user__email__icontains=query) | Q(report__icontains=query) | Q(id__icontains=query))
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class ReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        report_serializer = ReportSerializer(data=request.data)

        if report_serializer.is_valid():
            report_serializer.save(user=request.user)
            return Response(report_serializer.data, status=status.HTTP_201_CREATED)
        return Response(report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer


class EditReport(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReportSerializer
    queryset = Reports.objects.all()

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class EditStaffReport(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReportSerializer
    queryset = Reports.objects.all()


class DeleteReport(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReportSerializer
    queryset = Reports.objects.all()


class StaffDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Users.objects.all()
    serializer_class = StaffSerializer