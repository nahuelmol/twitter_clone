from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib.db.models import User 
from django.contrib.db.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST) 
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('usernam')
			messages.success(request,'Acccount created for {}'.format(username))
			return reverse('login')
	else:
		form = UserRegisterForm()

	content = {'form':form}
	template = 'users/register.html'
	return render(request,template,content)

@login_required
def profile(request):
	if request.method == 'POST':
		uform = UserUpdateForm(request.POST, instance= request.user)
		pform = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

		if uform.is_valid() and pform.is_valid():
			uform.save()
			pform.save()
			messages.success(request,'Acccount updated')
			return redirect('profile') 
	else:
		uform = UserUpdateForm(instance=request.user)
		pform = ProfileUpdateForm(instance=request.user.profile)

	content = {'uform':uform, 'pform':pform}
	template = 'users/profile.html'
	return render(request,template,content)

@login_required
def search_view(request):
	if request.method == 'POST':
		kerko = request.POST.get('search')
		print(kerko)
		User.object.filter(username_contains=kerko)
		context = {'results':results}
		template = 'user/search_result.html'
		return render(request,template,context)