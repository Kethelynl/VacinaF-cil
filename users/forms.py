from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # Personalizando mensagens de erro em português
        self.fields['username'].error_messages = {
            'unique': 'Este nome de usuário já existe. Escolha outro.',
            'required': 'O nome de usuário é obrigatório.',
        }
        self.fields['password1'].error_messages = {
            'required': 'A senha é obrigatória.',
            'min_length': 'A senha deve ter pelo menos 8 caracteres.',
        }
        self.fields['password2'].error_messages = {
            'required': 'A confirmação da senha é obrigatória.',
            'password_mismatch': 'As senhas não coincidem. Tente novamente.',
        }
        self.fields['email'].error_messages = {
            'invalid': 'Por favor, insira um endereço de email válido.',
            'required': 'O email é obrigatório.',
        }
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']