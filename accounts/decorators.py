from django.shortcuts import redirect
from main.models import Profile
def profile_required(view_func):
    def _decorated(request, *args, **kwargs):
        #Check authorization
        profile = Profile.get_profile(request.user)
        if profile:
            return redirect('home')
        return view_func(request,*args, **kwargs)
    return _decorated 
