from django.shortcuts import render
from django.views.generic.base import HttpResponseRedirect, View, HttpResponse
from .forms import registerForm, loginForm
from django.contrib.auth import authenticate, login, logout

class LoginView(View):

	def get(self,req):
		if req.user.is_autehnticated:
			return HttpResponseRedirect('/')
		form = loginForm()
		return render(req,self.template_name, {'form':form})

	def post(self,req):
		form = loginForm(req.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(req,username=username,password=password)

			if user is not None:
				login(req,user)
				print('success login')
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/')
		return HttpResponse('This is login view')

class RegisterView(View):
	template_name = 'users/register.html'

	def get(self, req):
		if req.user.is_autehnticated:
			print('already logged in')
			print(req.user)
			return HttpResponseRedirect('/')
		form = registerForm()
		context = {'form':form}
		return render(req,self.template_name,context)

	def post(self, req):
		form = registerForm(req.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']

			new_user = User(username=username, email=email)
			new_user.set_password(password)
			new_user.save()

#@login_required
#def profile(request):
#	if request.method == 'POST':
#		uform = UserUpdateForm(request.POST, instance= request.user)
#		pform = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
#
#		if uform.is_valid() and pform.is_valid():
#			uform.save()
#			pform.save()
#			messages.success(request,'Acccount updated')
#			return redirect('profile') 
#	else:
#		uform = UserUpdateForm(instance=request.user)
#		pform = ProfileUpdateForm(instance=request.user.profile)
#
#	content = {'uform':uform, 'pform':pform}
#	template = 'users/profile.html'
#	return render(request,template,content)
#
#@login_required
#def search_view(request):
#	if request.method == 'POST':
#		kerko = request.POST.get('search')
#		print(kerko)
#		User.object.filter(username_contains=kerko)
#		context = {'results':results}
#		template = 'user/search_result.html'
#		return render(request,template,context)