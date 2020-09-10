from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_view(request):
	if request.method == "POST":
		print(request.POST)
		usernameInput = request.POST['username']
		passwordInput = request.POST.get('password', '')
		currentUser = authenticate(request, username=usernameInput, password=passwordInput)
		if currentUser is not None:
			request.session['failed'] = False
		else:
			request.session['failed'] = True
			return redirect('login_view')
	return render(request, 'login.html')