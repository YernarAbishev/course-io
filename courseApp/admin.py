from django.contrib import admin
from .models import Category, Course, Theme
# Register your models here.
admin.site.site_header = 'My admin'

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Theme)
