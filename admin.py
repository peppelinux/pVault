from django.contrib import admin
from .models import *

from admin_inline_fk import *

from django.contrib import admin
from django.contrib import messages

class EncodingFormatAdmin(admin.ModelAdmin):
    #search_fields = ['codice_stazione_regione']
    list_display  = [ 'name', 'function', 'example'  ]
    #list_filter   = [ 'comune', 'provincia' ]
    pass
admin.site.register(EncodingFormat, EncodingFormatAdmin)

class PasswordEncodingAdmin(admin.ModelAdmin):
    pass
admin.site.register(PasswordEncoding, PasswordEncodingAdmin)

class ServerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Server, ServerAdmin)

class PasswordVaultAdmin(admin.ModelAdmin):
    def view_password(modeladmin, request, queryset):      
        from pVault.models import PasswordVault
        for i in queryset:
            pv = PasswordVault.objects.get(username=i.username).view()
            messages.add_message(request, messages.INFO, '%s password is: %s' % (i.username, pv))
    view_password.short_description = "decrypt password and print it on screen"
    
    list_display  = [ 'username', 'servers', 'hashes', 'is_active'  ]
    inlines       = [ PasswordVaultExportsInLine, PasswordVaultHistoryInLine ]
    actions       = [view_password,]
admin.site.register(PasswordVault, PasswordVaultAdmin)
