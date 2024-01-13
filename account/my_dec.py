from django.http import HttpResponseRedirect
from django.urls import reverse

def need_log_out(redirect_to):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse(redirect_to))
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
