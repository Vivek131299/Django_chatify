from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

from .models import Request


@csrf_exempt
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.method == 'GET':
        users = list(User.objects.exclude(username=request.user.username))
        sent_requests = list(Request.objects.filter(request_sent_from_id=request.user.id))
        sent_requests_to_users = [request.request_sent_to for request in sent_requests]
        accepted_requests_users = [request.request_sent_to for request in sent_requests if request.accepted]
        print(sent_requests_to_users)
        return render(request, "home.html", {'users': users, 'sent_requests_to_users': sent_requests_to_users, 'accepted_requests_users': accepted_requests_users})


@csrf_exempt
@login_required
def send_request(request, pk=None):
    if request.method == 'GET':
        if pk and pk != request.user.id:
            print(pk)
            if not Request.objects.filter(request_sent_from_id=request.user.id, request_sent_to_id=pk).exists():
                make_send_request = Request.objects.create(request_sent_from_id=request.user.id, request_sent_to_id=pk)
                print("Request sent")

                return redirect("home")
        return redirect("home")



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

