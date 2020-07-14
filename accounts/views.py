#from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from accounts.models import User, user_type
from .forms import UserAdminCreationForm
from django.contrib.auth.forms import AuthenticationForm

#def group_check(request):
#	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
#	group_name=str(group_name[0]) # convert to string

#	if "student" == group_name:
#		print (group_name)
#		return redirect('http://127.0.0.1:8000/student/')
#	elif "counsel" == group_name:
#		print(group_name)
#		return redirect('http://127.0.0.1:8000/counsel/')

def group_check(request):
	#group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	#group_name=str(group_name[0]) # convert to string
	user = request.user
	if user.groups.filter(name='student').exists():
		#print (group_name)
		return redirect('http://127.0.0.1:8000/student/')
	elif user.groups.filter(name='counsel').exists():
		#print(group_name)
		return redirect('http://127.0.0.1:8000/counsel/')


def logout_view(request):
	auth.logout(request)
	return redirect('http://127.0.0.1:8000/')

#def signup(request):
#	if (request.method == 'POST'):
#		username = request.POST.get('username')
#		email = request.POST.get('email')
#		password = request.POST.get('password')
#		st = request.POST.get('student')
#		co = request.POST.get('counsel')

#		user = User.objects.create_user(
#			username=username,
#			email=email,
#		)
#		user.set_password(password)
#		user.save()
#
#		usert = None
#		if st:
#			usert = user_type(user=user, is_student=True)
#		elif co:
#			usert = user_type(user=user, is_counsel=True)
#
#		usert.save()
#		# Successfully registered. Redirect to homepage
#		return redirect('home')
#	return render(request, 'signup.html')
def signup(request):
	form = UserAdminCreationForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			login(request, user)
			return redirect('group/')

		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])

			return render(request=request,
						  template_name="register_counsel.html",
						  context={"form": form})
	form = UserAdminCreationForm
	return render(request=request, template_name ='register_counsel.html', context={"form":form})

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('group/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request,
				  template_name="login_request.html",
				  context={"form": form})


#def login(request):
#	if (request.method == 'POST'):
#		email = request.POST.get('email')  # Get email value from form
#		password = request.POST.get('password')  # Get password value from form
#		user = authenticate(request, email=email, password=password)
#
#		if user is not None:
#			login(request, user)
#			type_obj = user_type.objects.get(user=user)
#			if user.is_authenticated and type_obj.is_student:
#				return redirect('http://127.0.0.1:8000/student/')  # Go to student home
#			elif user.is_authenticated and type_obj.is_counsel:
#				return redirect('http://127.0.0.1:8000/counsel/')  # Go to teacher home
#		else:
#			# Invalid email or password. Handle as you wish
#			return redirect('http://127.0.0.1:8000/')

#	return render(request, 'login.html')


#class register_counsel(CreateView):
#	#group = Group.objects.get(name='counsel')
#	#user.groups.add(group)
#    form_class = UserAdminCreationForm
#    success_url = reverse_lazy('teacher_home')
#    template_name = "register_counsel.html"

#class register_student(CreateView):
#    form_class = UserAdminCreationForm
#    success_url = reverse_lazy('student_home')
#    template_name = "register_student.html"

#class LoginView