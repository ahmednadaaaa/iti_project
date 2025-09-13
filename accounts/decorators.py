from django.shortcuts import redirect

def notLoggedUsers(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('crowdfunding:home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
