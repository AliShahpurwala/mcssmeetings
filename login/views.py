from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_view(request):
	if request.method == "POST":
		usernameInput = request.POST['username']
		passwordInput = request.POST.get('password', '')
		currentUser = authenticate(request, username=usernameInput, password=passwordInput)
		if currentUser is not None:
			login(request, currentUser)
			request.session['failed'] = False
			return redirect('home_view')
		else:
			request.session['failed'] = True
			return redirect('login_view')
	return render(request, 'login.html')