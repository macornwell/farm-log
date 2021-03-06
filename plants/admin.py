from django.contrib import admin
from plants.models import Bloom, Cultivar, Genus, Harvest, \
    PlantProductivityReport, Resource, Species, Watering


admin.site.register(Bloom)
admin.site.register(Cultivar)
admin.site.register(Genus)
admin.site.register(Harvest)
admin.site.register(PlantProductivityReport)
admin.site.register(Resource)
admin.site.register(Species)
admin.site.register(Watering)
