from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Order

admin.site.register(Order, SimpleHistoryAdmin)
