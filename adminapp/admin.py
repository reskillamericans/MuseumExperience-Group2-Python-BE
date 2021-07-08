from adminapp.models import Exhibit, Exhibit_Notification, Question, User, User_Profile, Subscriber
from django.contrib import admin

# Register your models here.
admin.site.register(Exhibit)
admin.site.register(Question)
admin.site.register(User_Profile)
admin.site.register(User)
admin.site.register(Exhibit_Notification)
admin.site.register(Subscriber) 