from django.shortcuts import render
from django.shortcuts import redirect
from .form import RegistrationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('entries:blog-home')
    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request,'users/register.html',context=context)