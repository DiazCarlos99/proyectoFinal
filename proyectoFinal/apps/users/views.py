from django.shortcuts import render

# Create your views here.
def Users(request):

	return render(request, 'app_users/users.html')

