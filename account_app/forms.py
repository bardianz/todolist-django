from django import forms

from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,
                               disabled=True,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control disabled'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', ]


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file', 'style': '50px'}))

    class Meta:
        model = Profile
        fields = ['avatar', ]


# from django.contrib.auth.forms import AuthenticationForm, UsernameField

# from django import forms

# class UserSignupForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserSignupForm, self).__init__(*args, **kwargs)

#     username = UsernameField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': '', 'id': 'username'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': '',
#             'id': 'id_password',
#         }
# ))


# from .models import CustomUser
# from django.contrib.auth.forms import UserCreationForm

# class SignUpForm(UserCreationForm):
#    class Meta:
#       model = CustomUser
#       fields = ('username', 'password1', 'password2', 'email')
