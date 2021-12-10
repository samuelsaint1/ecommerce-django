from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
# Create your views here.
def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            pasword = form.cleaned_data['pasword']
            # Saintsamuel229@gmail.com
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'registrado con exito')
            return redirect('register')


    context = {
        'form': form
    }
