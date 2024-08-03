from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.method == 'GET':
        return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
