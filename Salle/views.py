from django.shortcuts import render, redirect
from .forms import ContactForm 
from .models import Contact 
from .forms import MemberForm
from .models import Member


def home(request):
    return render(request,"Main.html")

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'ContactUsForm.html', {'form': form})

def thank_you(request):
    return render(request, 'ThankYou.html')


def view_contacts(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'view_contacts.html', {'contacts': contacts})




def member_view(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_thank_you')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})

def view_members(request):
    members = Member.objects.all().order_by('-date_joined')
    return render(request, 'view_members.html', {'members': members})

def member_thank_you_view(request):
    return render(request, 'member_thank_you.html')

def admin_web_view(request):
    return render(request, 'Admin-Web.html')