from django.contrib import admin
from .models import Passager_informations_vol
from .models import Bagage_informations_vol
from .models import Manifest,Vol_information


# Register your models here.
admin.site.register(Passager_informations_vol)
admin.site.register(Bagage_informations_vol)
admin.site.register(Manifest)
admin.site.register(Vol_information)

