import djcelery
djcelery.setup_loader()

# Celery
BROKER_URL = 'redis://localhost:6379/0'  
CELERY_ACCEPT_CONTENT = ['json']  
CELERY_TASK_SERIALIZER = 'json'  
CELERY_RESULT_SERIALIZER = 'json'  


# Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('pVault.celery_tasks',)

# Set Serializers
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
