from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views
from . import consumers

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('send_request/<int:pk>/', views.send_request, name='send_request'),
    path('requests/', views.view_requests, name='requests'),
    path('accept_request/<int:sent_from_id>/<int:sent_to_id>/', views.accept_request, name='accept_request'),
    path('accept_request_by_id/<int:id>/', views.accept_request_by_id, name='accept_request_by_id'),
    path('chat/<int:receiver_id>/', views.chat_view, name="chat"),
]