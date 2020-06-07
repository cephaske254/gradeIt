from django.http import HttpResponseRedirect

def profile_required(view_func):
    def _decorated(request, *args, **kwargs):
        #Check authorization
        if not request.user.is_authenticated:
            return view_func(request,*args, **kwargs)
        else:
            return HttpResponseRedirect('finalize/')
    return _decorated 
