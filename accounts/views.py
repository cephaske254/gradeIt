from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import profile_required
from .forms import UpdateUserForm, UserProfileForm
from main.models import Profile, User
# Create your views here.

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

@login_required
def finalize(request):
    current_user = request.user
    update_user = UpdateUserForm()
    user_profile = UserProfileForm()
    if request.method == 'POST':
        update_user = UpdateUserForm(request.POST)
        if update_user.is_valid():
            first_name = update_user.cleaned_data.get('first_name')
            last_name = update_user.cleaned_data.get('last_name')
            email = update_user.cleaned_data.get('email')
            user = User.objects.get(pk=current_user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
        
        user_profile = UserProfileForm(request.POST,request.FILES)
        if user_profile.is_valid():
            phone = user_profile.cleaned_data.get('phone')
            bio = user_profile.cleaned_data.get('bio')
            photo = request.FILES.get('photo')
            print(phone)
            Profile.save_profile(current_user,bio,phone,photo)
        return redirect('home')


            
    context = {
        'user_profile': user_profile,
        'update_user': update_user,
        'user': current_user,
    }
    return render(request,'accounts/finalize.html',context)