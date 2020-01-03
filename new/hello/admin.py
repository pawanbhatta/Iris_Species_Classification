from django.contrib import admin
from .models import IrisPlants

# Register your models here.
# admin.site.register(IrisPlants)


@admin.register(IrisPlants)
class AdminIris(admin.ModelAdmin):
    list_display = ('length_petal', "length_sepal",
                    "width_petal", "width_sepal", "dSpecies")

    def dSpecies(self, obj):
        return obj.get_species_display()
    dSpecies.short_description = "Species"
