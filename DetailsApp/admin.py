from django.contrib import admin
from DetailsApp.models import Department,Subject,Semester

# Register your models here.
admin.site.register(Department)
admin.site.register(Subject)

admin.site.register(Semester)