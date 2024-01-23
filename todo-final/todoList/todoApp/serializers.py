# serializers.py

from rest_framework import serializers
from .models import Todo, User
from datetime import date

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)  
    approaching_date = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['id', 'user','url', 'title', 'details', 'image', 'date_created', 'completed','priority','due_date','approaching_date']

    def get_approaching_date(self, instance):
        if instance.due_date:
            today = date.today()
            days_until_due = (instance.due_date - today).days

            if days_until_due == 0:
                return "Due Today"
            elif days_until_due < 0:
                return "Overdue"
            elif days_until_due <= 3:
                return "Approaching Due Date"
            else:
                return ""
        else:
            return ""
        

