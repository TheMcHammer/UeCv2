from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.forms import UserAdminCreationForm, SignUpForm, UserUpdateForm, ProfileUpdateForm


@login_required()
def profiles(request):
    #args = {'user': request.user}
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request. FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #messages.succes(request, f'Your account has beeen updated!')
            return redirect('profiles')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'counsel_profile.html', context)