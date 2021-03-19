from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'index.html')



def login(requset):
	form= SignUpForm()
	if requset.method == 'POST':
		form = SignUpForm(requset.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
	return render(requset,'login.html',{'form':form})


	#return render(request,'login.html',{'form':form})

