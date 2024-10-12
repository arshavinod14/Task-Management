from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from .filters import TaskFilter
from rest_framework.pagination import PageNumberPagination 
from rest_framework.filters import OrderingFilter

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id=None):
        if task_id is None:
            tasks = Task.objects.filter(
                Q(assigned_to=request.user) | Q(created_by=request.user)
            )

            # Search functionality
            search_query = request.GET.get('search', None)
            if search_query:
                tasks = tasks.filter(
                    Q(title__icontains=search_query) | Q(description__icontains=search_query)
                )

            # filters
            task_filter = TaskFilter(request.GET, queryset=tasks)
            tasks = task_filter.qs

            #ordering
            ordering = request.GET.get('ordering', None)
            if ordering:
                tasks = tasks.order_by(ordering)

            #pagination
            paginator = PageNumberPagination()
            paginator.page_size = 10 
            result_page = paginator.paginate_queryset(tasks, request)

            
            serializer = TaskSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)
        
        else:
            task = get_object_or_404(Task, id=task_id, created_by=request.user)
            serializer = TaskSerializer(task)
            return Response(serializer.data)


    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
