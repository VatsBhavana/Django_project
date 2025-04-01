from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(AdminUser)
admin.site.register(learners)
admin.site.register(category)
admin.site.register(course)
admin.site.register(enrollcourse)
admin.site.register(company)