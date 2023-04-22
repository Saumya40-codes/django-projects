from django.forms import ModelForm
from .models import Room,SignUp, Test, Topic, Loginpage

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
    
class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = fields = ['user','email','password']

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['username','email','password']

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class Loginform(ModelForm):
    class Meta:
        model = Loginpage
        fields = ['username','password']