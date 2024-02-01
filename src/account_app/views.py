from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# from .forms import SignUpForm
from .forms import UpdateUserForm, UpdateProfileForm
from .models import Profile
from todo_app.models import ToDoItem
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/account/login')
def dashboard_view(request):
    user = request.user
    profile = Profile.objects.get(user=request.user)
    print()
    number_of_items = len(ToDoItem.objects.filter(owner=user))
    context = {
        'number_of_items': number_of_items,
        'profile':profile
    }

    return render(request, 'account_app/dashboard.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Please fill the fields with correct information')
            return redirect('account_app:signup')
    form = UserCreationForm()
    return render(request, 'account_app/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('account_app:dashboard')
        else:
            messages.error(request,'Username or password not correct')
            return redirect('account_app:login')

    form = AuthenticationForm()
    return render(request, 'account_app/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

@login_required(login_url='/account/login')
def profile_view(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('account_app:dashboard')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    template = 'account_app/profile.html'
    return render(request, template, {'user_form': user_form, 'profile_form': profile_form})


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account_app/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('/')


# def profile_view(request):
#     # username = request
#     # query = CustomUser.objects.filter()
#     # print(query)
#     # context = {
#     #     'profile': query,
#     # }
#     context = {
#     }

#     return render(request, , context)
