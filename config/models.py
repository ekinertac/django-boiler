#==================================================
# This file is not a real model file
# it only be the creation of the default superuser
#
# I'm really tired of giving admin/admin@admin.com/admin input for
# everyime write the './manage.py syncdb' command
#==================================================


from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals

# From http://stackoverflow.com/questions/1466827/ --
#
# Prevent interactive question about wanting a superuser created.  (This code
# has to go in this otherwise empty "models" module so that it gets processed by
# the "syncdb" command during database creation.)

username = 'admin'
password = 'admin'
email = 'admin@admin.com'

signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')


# Create our own test user automatically.

def create_testuser(app, created_models, verbosity, **kwargs):
  if not settings.DEBUG:
    return
  try:
    auth_models.User.objects.get(username=username)
  except auth_models.User.DoesNotExist:
    print '=' * 80
    print 'Creating Administrative Superuser'
    print '-' * 80
    print 'Username: %s' % username
    print 'Password: %s' % password
    print 'Email:    %s' % email
    print '=' * 80
    assert auth_models.User.objects.create_superuser(username, email, password)
  else:
    print 'Superuser already exists.'

signals.post_syncdb.connect(create_testuser,
    sender=auth_models, dispatch_uid='common.models.create_testuser')