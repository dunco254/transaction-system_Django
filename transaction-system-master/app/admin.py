from django.contrib import admin
from .models import Transaction, User, TransactionAdmin, UserAdmin, Bank, BankAdmin
# Register your models here.

admin.site.site_header = 'SCG Gateway'

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Bank, BankAdmin)
