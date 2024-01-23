# from django.contrib import admin
# from django.urls import path
# from .views import AssignUsersRandomly, TodoView, TodoOpperations, complete,UserCreateView,UserListView

# urlpatterns = [
#     path('todos/', TodoView.as_view(), name='todo-list'),
#     path('todos/<int:pk>/', TodoOpperations.as_view(), name='todo-detail'),
#     path('todos/<int:pk>/complete/', complete, name='todo-complete'),
#     path('users/', UserCreateView.as_view(), name='user-create'),
#     path('all-users/', UserListView.as_view(), name='user-list'),
#     path('assign/', AssignUsersRandomly.as_view(), name='assign-users-randomly'),
# ]

# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, UserViewSet, AssignUsersRandomlyViewSet

router = DefaultRouter()
router.register('todos', TodoViewSet)
router.register('users', UserViewSet)
router.register('assign-users', AssignUsersRandomlyViewSet, basename='assign-users-randomly')


urlpatterns = [
    path('', include(router.urls)),
]
