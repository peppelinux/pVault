# pVault
Password Vault with customizable password storage

Django application that lets you manage user credentials with the possibility to export them in different hash format.
It could be also used together with celery to propagate exported user credentials to production servers (freeRadius, joomla, LDAP, many others), according to its development milestone.

TODO:
- Celery tasks for different kind of password propagations (joomla, wordpress, freeradius...);
- some Celery worker examples for production nodes;
- Json Web Tokens (python-jose's JWT) in views.py. This feature lets the production nodes to push password updates and new credentials  in pVault as well;

REQUIREMENTS:
- pycrypto
- passlib
- hashlib
- python-jose
- redis  # change it to your preferred message broker
- django-celery
- flower # optional
