"""
raven.contrib.django.wsgi_hooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implements a hook method for wsgi servers like chaussette or the gunicorn
executable which doesn't run a django command.

:copyright: (c) 2010-2012 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""


def run_raven(*args, **kwargs):
    """Set up raven for django by running a django command.
    It is necessary because chaussette doesn't run a django command.
    """
    from django.core.management import call_command
    call_command('validate')
    return True
