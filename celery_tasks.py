from __future__ import absolute_import  
from celery import shared_task, task

# example from shell or another app.views
# from pVault.tasks import tasktest
# tasktest.delay('This is only a test.')

# in settings.py put these:
# if 'pVault' in INSTALLED_APPS:
#    from pVault.settings import *

# run the worker
# python manage.py celeryd -l info

# run web monitor if needed
# celery flower

@shared_task
def tasktest(param):  
    return 'The task executed with argument "%s" ' % param

