from adminapp.models import Exhibit, Exhibit_Notification, Question, User, User_Porfile, Visitor, Staff, Admin, Curator
from django.contrib import admin

# Register your models here.
admin.site.register(Exhibit)
admin.site.register(Question)
admin.site.register(User_Porfile)
admin.site.register(User)
admin.site.register(Visitor) 
admin.site.register(Staff)
admin.site.register(Admin)
admin.site.register(Curator)
admin.site.register(Exhibit_Notification)