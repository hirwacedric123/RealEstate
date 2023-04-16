from django.contrib import admin

# Register your models here.
from realapp.models import House
from realapp.models import LandPlot

# Register your models here.
class HouseAdmin(admin.ModelAdmin):
  list_display = ("category", "price", "address",)
admin.site.register(House,HouseAdmin)

class LandPlotAdmin(admin.ModelAdmin):
  list_display = ("category", "price", "address",)
admin.site.register(LandPlot,LandPlotAdmin)