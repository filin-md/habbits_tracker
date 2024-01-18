from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import generics

from main.forms import RegisterForm
from main.models import User, Habit
from main.paginators import MainPaginator
from main.permissions import IsOwnerOrStaff
from main.serializers import HabitSerializer


# Create your views here.

class RegisterView(CreateView):
    # Создаем обычный контроллер на создание сущности
    model = User
    form_class = RegisterForm


def homepage():
    pass


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrStaff]
    pagination_class = MainPaginator


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsOwnerOrStaff]


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrStaff]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrStaff]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrStaff]


