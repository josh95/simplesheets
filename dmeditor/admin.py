from django.contrib import admin

from .models import Dm, Player, Sheets, Attributes, Allies, Levels, Items

admin.site.register(Dm)
admin.site.register(Player)
admin.site.register(Sheets)
admin.site.register(Attributes)

admin.site.register(Allies)
admin.site.register(Levels)
admin.site.register(Items)
