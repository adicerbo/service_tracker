from django.contrib import admin
from .models import Boat, Part, Service

admin.site.register(Boat)
admin.site.register(Service)
admin.site.register(Part)