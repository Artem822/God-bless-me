from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, login


user = get_user_model

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('Main_page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})