# pVault
Password Vault with customizable password storage

Django application that lets you manage user credentials with the possibility to export them in different hash format.
It could be also used together with django-rq to propagate exported user credentials to production servers (freeRadius, joomla, LDAP, many others...they only need their running worker connected to redis server), according to its development milestone.

TODO:
- Django-rq jobs with different templates for any kind of password propagations (joomla, wordpress, freeradius...);
- Django-rq worker examples for production nodes;
- Json Web Tokens (python-jose's JWT) in views.py. This feature allows the production nodes to push in pVault password, updates and new credentials as well and lets the workers get signed jobs.

REQUIREMENTS:
- pycrypto
- passlib
- hashlib
- python-jose
- redis  # change it to your preferred message broker
- django-rq
- MySQL-python
