from django.contrib import admin

from .models import Dm, Player, Sheets, Attributes, ally, level, item

admin.site.register(Dm)
admin.site.register(Player)
admin.site.register(Sheets)
admin.site.register(Attributes)

admin.site.register(ally)
admin.site.register(level)
admin.site.register(item)
