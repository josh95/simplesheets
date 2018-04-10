from django.contrib import admin

from .models import Dm, Player, Sheets, Attributes, Allies, Levels, Items, Ally_mapping, Item_mapping

admin.site.register(Dm)
admin.site.register(Player)
admin.site.register(Sheets)
admin.site.register(Attributes)

admin.site.register(Allies)
admin.site.register(Levels)
admin.site.register(Items)

admin.site.register(Ally_mapping)
admin.site.register(Item_mapping)

