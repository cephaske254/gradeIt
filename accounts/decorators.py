from django.shortcuts import redirect
from main.models import Profile
def profile_required(view_func):
    def _decorated(request, *args, **kwargs):
        #Check authorization
        if request.user.is_authenticated:
            profile = Profile.get_profile(request.user)
            if not profile:
                return redirect('finalize')
        return view_func(request,*args, **kwargs)
    return _decorated 
