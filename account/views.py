from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import error
from .my_dec import need_log_out

@need_log_out('index')
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'account/register.html', context)

@need_log_out('index')
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'account/login.html')

@login_required(login_url='/login/')
def custom_logout(request):
    logout(request)
    return redirect('index')