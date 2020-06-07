from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from .decorators import profile_required

# Create your views here.
@profile_required
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {
        'form': form
    }
    return render(request,'accounts/register.html',context)

def finalize(request):
    form = UserChangeForm()
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            pass
            
    context = {
        'form': form
    }
    return render(request,'accounts/register.html',context)