from django.shortcuts import render
from .forms import UserLoginForm

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            return render(request, 'success.html', {'username': username, 'email': email})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})
