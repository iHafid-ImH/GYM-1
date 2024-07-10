from django.contrib import admin
from .models import Trainer,Member,Subscription,Contact
# Register your models here.
admin.site.register(Trainer)
admin.site.register(Member)
admin.site.register(Subscription)
admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')