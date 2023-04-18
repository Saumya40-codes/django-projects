from django.forms import ModelForm
from .models import Room, UserLogin,SignUp

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class LoginForm(ModelForm):
    class Meta:
        model = UserLogin
        fields = '__all__'
    
class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'