from django.contrib.auth.views import LoginView
from django.urls import path

from main.views import RegisterView, homepage, HabitListAPIView, PublicHabitListAPIView, HabitCreateAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/public/', PublicHabitListAPIView.as_view(), name='public_habits_list'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/update/<int:pk>', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>', HabitDestroyAPIView.as_view(), name='habit_delete'),

]
