from django.contrib import admin
from .models import *

from admin_inline_fk import *

from django.contrib import admin
from djcelery.models import (TaskState, WorkerState,
                 PeriodicTask, IntervalSchedule, CrontabSchedule)

# disable djcelery modeladmin
admin.site.unregister(TaskState)
admin.site.unregister(WorkerState)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(PeriodicTask)


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
    list_display  = [ 'username', 'password', 'servers', 'is_active'  ]
    inlines       = [ PasswordVaultExportsInLine, PasswordVaultHistoryInLine ]

admin.site.register(PasswordVault, PasswordVaultAdmin)
