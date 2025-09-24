from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.session.get('user_id') is None:
            messages.error(request, "Please sign in to access this page.")
            return redirect('/signin/')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
