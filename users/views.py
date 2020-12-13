from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request): # register page logic 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) # form wiht user data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}!You can Log in Now") # Flash message
            return redirect('login')
    else:
            form = UserRegisterForm() # empty form
    return render(request,'users/register.html',{'form':form})

@login_required # to display the route when the user is logged in 
def profile(request): # profile of an user logic 
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your Account Has Been Updated! ")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context) # pasing the forms to the profile page