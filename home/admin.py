from django.contrib import admin
from home.models import Contact
from home.models import Maintenance
from home.models import Driving
from home.models import Tvswarranty
from home.models import Olas1pro

# Register your models here.
admin.site.register(Contact)
admin.site.register(Maintenance)
admin.site.register(Driving)
admin.site.register(Tvswarranty)
# admin.site.register(Herowarranty)
# admin.site.register(Suzukiwarranty)
# admin.site.register(Hondawarranty)
# admin.site.register(Yamahawarranty)
# admin.site.register(Atherwarranty)
# admin.site.register(Viviprowarranty)
# admin.site.register(Olawarranty)
# admin.site.register(Bajajwarranty)
# admin.site.register(Riverindiewarranty)
admin.site.register(Olas1pro)