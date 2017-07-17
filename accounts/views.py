from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def create_account(request):
    if request.method == 'POST':
        if request.POST["password"] == request.POST["password_valid"]:

            # try/catch block to catch unique usernames
            try:
                User.objects.get(username=request.POST["username"])
                return render(request, 'accounts/create_account.html', {'error': 'Username is already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password"])
                login(request, user)
                return render(request, 'accounts/create_account.html')
        
        else:
            return render(request, 'accounts/create_account.html', {'error': 'Passwords must match'})

    return render(request, 'accounts/create_account.html')


def login_user(request):
    if request.method == 'POST':
        # get username and password
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # If user is redirected to login, send them to there original page
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')

        else:
            return render(request, 'accounts/login_user.html', {'error': 'Username and Password did not match'})

    else:
        return render(request, 'accounts/login_user.html')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')