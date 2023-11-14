from collections import namedtuple

from _decimal import Decimal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AuthForm, ProfileForm, EditProfileForm
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from .models import Profile
# Create your views here.


class MyLoginView(LoginView):

    template_name = 'users/login.html'

    redirect_authenticated_user = True


class MyLogoutView(LogoutView):

    next_page = '/'


class RegisterView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        reg_form = ProfileForm()
        context = {
            'reg_form': reg_form
        }
        return render(request, 'users/register.html', context=context)

    def post(self, request):
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            date_of_birth = form.cleaned_data['date_of_birth']
            city = form.cleaned_data['city']

            user = authenticate(username=username, password=password)
            Profile.objects.create(user=user, date_of_birth=date_of_birth, city=city)

            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid form')


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        full_user = model_to_dict(request.user) | model_to_dict(request.user.profile)
        form = EditProfileForm(initial=full_user)

        return render(request, 'users/edit_profile.html', {
            'form': form,
        })

    def post(self, request):
        form = EditProfileForm(request.POST)

        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()

            request.user.profile.date_of_birth = form.cleaned_data['date_of_birth']
            request.user.profile.city = form.cleaned_data['city']
            request.user.profile.save()

            return redirect('profile')


@login_required()
def user_profile_view(request):
    user_lots = request.user.lot_set.all()
    favorites = request.user.favorites.all()

    return render(request, 'users/user_profile.html', {
        'favorites': favorites,
        'user_lots': user_lots,
    })


def top_up_balance(request):
    if request.method == 'POST':
        top_up = Decimal(request.POST.get('top_up'))

        profile = request.user.profile
        profile.balance += top_up
        profile.save()

        return redirect('profile')


# class MyLoginView(View):
#
#     def get(self, request):
#         auth_form = AuthForm()
#         context  = {
#             'auth_form': auth_form
#         }
#
#         return render(request, 'users/login.html', context)
#
#     def post(self, request):
#         auth_form = AuthForm(request.POST)
#
#         if auth_form.is_valid():
#             cd = auth_form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse(f'{request.user.username}, Вы успешно вошли в систему!')
#                 else:
#                     auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна!')
#             else:
#                 auth_form.add_error('__all__', 'Ошибка! Проверьте правильность введелния логина и пароля!')


# def logout_view(request):
#     logout(request)
#     return redirect('/')
