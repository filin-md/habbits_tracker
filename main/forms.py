from django.contrib.auth.forms import UserCreationForm

from main.models import User


class RegisterForm(UserCreationForm):
    # Наследуемся от специальной формы UserCreationForm из модуля auth
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)