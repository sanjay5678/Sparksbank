from django.contrib import admin

# Register your models here.
from bank.models import Transfers,Transactions
admin.site.register(Transfers)
admin.site.register(Transactions)