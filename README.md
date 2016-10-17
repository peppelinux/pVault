# pVault
Password Vault with customizable password storage

Django application that lets you manage user credentials with the possibility to export them in different hash format.
It could be also used together with celery to propagate exported user credentials to production servers (freeRadius, joomla, LDAP, many others), according to its development milestone.

TODO:
- Celery tasks for different kind of password propagation (joomla, wordpress, freeradius...)
- Celery worker examples for production nodes
- Json Web Tokens (python-jose's JWT) from production nodes brings passwords updates and brand new credentials on pVault

REQUIREMENTS
- pycrypto
- passlib
- hashlib
- python-jose
- redis  # change it to your preferred message broker
- django-celery
- flower # optional
