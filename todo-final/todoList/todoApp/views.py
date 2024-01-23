import datetime
from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Todo, User
from .serializers import TodoSerializer, UserSerializer
from rest_framework.filters import SearchFilter

class CustomPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'links_for_pages': {
                'next_page': self.get_next_link(),
                'previous_page': self.get_previous_link()
            },
            'Total_Items': self.page.paginator.count,
            'Task_list': data
        })

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-due_date')
    serializer_class = TodoSerializer
    pagination_class = CustomPagination
    filter_backends =[SearchFilter]
    search_fields=['title','details']

    

    def due_date_check(self,todo):
        if todo.due_date:
            current_date = datetime.now().date()
            days_until_due = (todo.due_date - current_date).days
            if 0 <= days_until_due <= 7:
                return Response({'success': 'Your task deadline is ' + days_until_due})
        return False

    @action(detail=True, methods=['get'])
    def assign_user(self, request, pk=None):
        todo = self.get_object()  
        user_id = request.data.get('user_id')

        try:
            user = User.objects.get(pk=user_id)
            todo.user = user
            todo.save()
            return Response({'success': 'User assigned to the task successfully'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def remove_user(self, request, pk=None):
        todo = self.get_object() 
        todo.user = None
        todo.save()
        return Response({'success': 'User removed from the task'})

    @action(detail=True, methods=['get'])
    def mark_completed(self, request, pk=None):
        todo = self.get_object() 
        todo.completed = True
        todo.save()
        return Response({'success': 'Task marked as completed successfully'})
    
    @action(detail=False,methods=['get'])
    def search(self,request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        if serializer.data is not None:
         return Response(serializer.data)
        else:
            return Response({'message':'No data found'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AssignUsersRandomlyViewSet(viewsets.ViewSet):

    def get_queryset(self):
        return Todo.objects.all().order_by('-due_date')

    def list(self, request):
        todos = self.get_queryset()
        users = User.objects.all()

        if not todos.exists() or not users.exists():
            return Response({
                    'error': 'No tasks or users available'
                    }, status=status.HTTP_404_NOT_FOUND)

        assigned_users_data = []

        for todo in todos:
            random_user = users.order_by('?').first()
            todo.user = random_user
            todo.save()

            assigned_user_data = {
                'task_details': TodoSerializer(todo, context={'request': request}).data,
                'message': 'User assigned successfully'
            }
            assigned_users_data.append(assigned_user_data)

        paginator = CustomPagination()
        page = paginator.paginate_queryset(assigned_users_data, request)
        return paginator.get_paginated_response(page)
