from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # save to database -- tian
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Your account has been created for {username}! You are now able to log in')
            # other options: message.debug(), message.info(), message.warning(), message.error() -tian

            return redirect('login')
    else:
        # doing nothing, returning empty form -tian
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
    # 'form' kept the user data. when the submitted form was invalid, the data was saved
    # in 'form' and displayed back, instead of displaying a new blank form, so that user
    # didn't have to enter from scratch. -tian


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # without instance=..., we will get a blank form. instance= populate the form. -tian
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')

            # use redirect() instead of render(request). -tian
            # this is called post-get-redirect pattern.
            #    when you reload your browser after submitting a form, an alert message
            #    comes up that says: are you sure that you want to reload because the
            #    data will be resubmitted.
            #
            #    this is because your browser is telling you that you are about to run
            #    another post request when you reload your page.
            #
            #    therefore, redirecting here causes browser to send a get request and then we
            #    don't get the alert message.
            #
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context) # users/templates/users/profile.html -tian
