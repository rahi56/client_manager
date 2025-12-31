from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('main_applicant', 'company', 'status', 'initial_payment')
    list_filter = ('company', 'status', 'initial_payment')
    search_fields = ('main_applicant', 'gcbl_no', 'channel_name')
from django.contrib import admin

# Register your models here.
