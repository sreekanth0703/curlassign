from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from assignment.models import *
from assignment.serializers import *
import json
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_superuser=0).order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserMappingViewSet(viewsets.ModelViewSet):
    queryset = UserMapping.objects.all()
    serializer_class = UserMappingSerializer
    permission_classes = [permissions.IsAuthenticated]


@method_decorator(csrf_exempt, name='dispatch')
class LoginRequestView(View):
    serializer_class = LoginRequestSerializer

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = LoginRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def get(self, request):
        serializer = LoginRequestSerializer(LoginRequest.objects.filter(status='pending'), many=True)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request):
        data = JSONParser().parse(request)
        data_obj = LoginRequest.objects.get(id=data['id'])
        serializer = LoginRequestSerializer(data_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class status(View):

    def get(self, request):
        if request.user.is_authenticated:
            data = {'username': request.user.username, 'first_name': request.user.first_name, 'status': 1, "message": "Success"}
            return HttpResponse(json.dumps(data), status=200)
        else:
            data = {'status': 0, 'message': 'Invalid User'}
            return HttpResponse(json.dumps(data), status=403)


@method_decorator(csrf_exempt, name='dispatch')
class RequestStatus(View):
    def post(self, request):
        data = json.loads(request.read())
        res_data = {'username': '', 'status': 0}
        data_obj = LoginRequest.objects.filter(id=data['id'])
        if data_obj and data_obj[0].status == 'approved':
            user = data_obj[0].user
            request.session.set_expiry(86400)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            res_data['username'] = user.username
            res_data['status'] = 1
            return HttpResponse(json.dumps(res_data))
        elif data_obj and data_obj[0].status == 'rejected':
            return HttpResponse(json.dumps(res_data), status=401)
        return HttpResponse(json.dumps(res_data), status=403)


@method_decorator(csrf_exempt, name='dispatch')
class user_login(View):
    def post(self, request):
        data = json.loads(request.read())
        res_data = {'username': '', 'status': 0}
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            res_data['username'] = user.username
            res_data['status'] = 1
            return HttpResponse(json.dumps(res_data))
        return HttpResponse(json.dumps(res_data), status=403)


@method_decorator(csrf_exempt, name='dispatch')
class user_logout(View):
    def get(self, request):
        resp_data = {'success': 1, 'message': "Logged Out"}
        logout(request)
        return HttpResponse(json.dumps(resp_data), status=200)
