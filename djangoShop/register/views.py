
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render, redirect

# from django.views.generic import ListView, DetailView, CreateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import RegisterUserForm, UserCreationForm
# from django.contrib.auth import authenticate, login

from .forms import *
from .models import *

@login_required
def profile_view(request):
    return render(request, 'register/profile.html')



class RegisterView(FormView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy("register:profile")


    def form_valid(self, form):
        form.save()
        if form.is_valid():
            try:
                Register.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Oppsss')
        return super().form_valid(form)

def home(request):
    return render(request, 'register/home.html')

