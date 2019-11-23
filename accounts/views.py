from django.utils.decorators import method_decorator

from .models import Profile
from django.views import generic
from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, ProfileForm, ProfileForm1
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from denuncias.models import Denuncia

@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'perfil': user_profile})

@login_required
def dashboard(request):
    user_profile = Profile.objects.get(user=request.user)
    try:
        denuncias = Denuncia.objects.get(user=request.user)
    except Denuncia.DoesNotExist:
        denuncias = None
    return render(request, 'accounts/dashboard.html', {'perfil': user_profile, 'denuncias': denuncias})

@login_required
def configurations(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/configurations.html', {'perfil': user_profile})


class Register(generic.CreateView):
    form_class = ProfileForm
    success_url = reverse_lazy('login')
    template_name = "accounts/register.html"

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request,user)
        return redirect('index')

@method_decorator(login_required, name='dispatch')
class ManageReports(generic.ListView):
    model = Denuncia
    template_name = "accounts/manage_report.html"

    def get_context_data(self, **kwargs):
        denuncias = Denuncia.objects.filter(user=self.request.user).all()
        user_profile = Profile.objects.get(user=self.request.user)
        context = {"denuncias": denuncias, 'perfil': user_profile}
        return context

def _login(request):
    return render(request, 'accounts/login.html')


@login_required
@transaction.atomic
def update_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm1(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Seu perfil foi atualizado!'))
            return redirect('perfil')
        else:
            messages.error(request, _('Por favor, corrija os erros abaixo.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm1(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'perfil': user_profile
    })