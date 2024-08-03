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
        received_requests = list(Request.objects.filter(request_sent_to_id=request.user.id))
        sent_requests_to_users = [r.request_sent_to for r in sent_requests]
        accepted_sent_requests_to_users = [r.request_sent_to for r in sent_requests if r.accepted]
        received_requests_from_users = [r.request_sent_from for r in received_requests]
        accepted_received_requests_from_users = [r.request_sent_from for r in received_requests if r.accepted]
        print(sent_requests_to_users)
        return render(request, "home.html",
                      {'users': users,
                       'sent_requests_to_users': sent_requests_to_users,
                       'accepted_sent_requests_to_users': accepted_sent_requests_to_users,
                       'received_requests_from_users': received_requests_from_users,
                       'accepted_received_requests_from_users': accepted_received_requests_from_users})


@csrf_exempt
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def send_request(request, pk=None):
    if request.method == 'GET':
        if pk and pk != request.user.id:
            print(pk)
            if not Request.objects.filter(request_sent_from_id=request.user.id, request_sent_to_id=pk).exists():
                make_send_request = Request.objects.create(request_sent_from_id=request.user.id, request_sent_to_id=pk)
                print("Request sent")

                return redirect("home")
        return redirect("home")


@csrf_exempt
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_requests(request):
    if request.method == 'GET':
        requests = Request.objects.all()
        print(requests)
        sent_requests = request.user.sent_requests.all()
        not_accepted_sent_requests = [r for r in sent_requests if not r.accepted]
        received_requests = request.user.received_requests.all()
        not_accepted_received_requests = [r for r in received_requests if not r.accepted]
        print(sent_requests)
        print(received_requests)
        return render(request, "requests.html", {'not_accepted_sent_requests': not_accepted_sent_requests, 'not_accepted_received_requests': not_accepted_received_requests})


@csrf_exempt
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def accept_request(request, sent_from_id=None, sent_to_id=None):
    if request.method == 'GET':
        if sent_from_id and sent_to_id:
            chat_request = Request.objects.get(request_sent_from_id=sent_from_id, request_sent_to_id=sent_to_id)
            chat_request.accepted = True
            chat_request.save()

            return redirect("home")


@csrf_exempt
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def accept_request_by_id(request, id=None):
    if request.method == 'GET':
        if id:
            chat_request = Request.objects.get(id=id)
            chat_request.accepted = True
            chat_request.save()

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

