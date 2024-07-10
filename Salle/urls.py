from django.shortcuts import render
from GYM.urls import path
from . import views
from .views import home, contact_us, thank_you
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.
urlpatterns=[
    path('', views.home, name='home'),
    path('contact/', contact_us, name='contact_us'),
    path('thank-you/', thank_you, name='thank_you'),
    path('admin/contacts/', views.view_contacts, name='view_contacts'),
    path('member/', views.member_view, name='member_us'),
    path('member_thank_you/', views.member_thank_you_view, name='member_thank_you'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)