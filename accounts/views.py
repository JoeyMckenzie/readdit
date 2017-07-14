from django.shortcuts import render

# Create your views here.
def create_account(request):
    if request.method == 'POST':
        print("POST WORKED")
    
    return render(request, 'accounts/create_account.html')