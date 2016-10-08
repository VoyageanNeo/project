from django.contrib import admin
from .models import Signup
# Register your models here.
from .forms import SignupForm
class SignupAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form=SignupForm

admin.site.register(Signup, SignupAdmin)