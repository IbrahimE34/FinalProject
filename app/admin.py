from django.contrib import admin

import app
from app.models import Car, Category

admin.site.register(Car)
admin.site.register(Category)
