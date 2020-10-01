from django.contrib import admin

from unesco.models import Site, Category,Iso,States,Region
# Register your models here.
admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Iso)
admin.site.register(States)
admin.site.register(Region)
