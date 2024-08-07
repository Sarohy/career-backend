from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from .models import User

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'is_counselor')

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'is_counselor', 'is_active', 'is_staff')
