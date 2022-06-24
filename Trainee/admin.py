from django.contrib import admin

# Register your models here.
from Trainee.models import Trainee,Course
admin.site.register(Course)
admin.site.register(Trainee)
