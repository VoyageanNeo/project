from django.contrib import admin


from .models import mileStone, mileStory, UserProfile
admin.site.register(mileStone)
admin.site.register(mileStory)
admin.site.register(UserProfile)