from django.contrib import admin
from .models import Locomotive, Brigade, Repair, Worker

admin.site.register(Locomotive)
admin.site.register(Brigade)
admin.site.register(Repair)
admin.site.register(Worker)
