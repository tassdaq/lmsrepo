from django.contrib import admin
from home.models import Profile,lecture,zoom_session,timetables








# Register your models here.
admin.site.register(Profile)
admin.site.register(lecture)
admin.site.register(zoom_session)
admin.site.register(timetables)



admin.site.site_header="HYSEC ADMIN"
admin.site.site_title="HYSEC ADMIN PORTAL"
admin.site.index_title="Welcome to Hysec Admin Portal"