"""
 This module contains useful utilities for GeoDjango.
"""
from django.core.exceptions import ImproperlyConfigured

try:
    # LayerMapping requires DJANGO_SETTINGS_MODULE to be set,
    # and ImproperlyConfigured is raised if that's not the case.
    from django.contrib.gis.utils.layermapping import (  # NOQA
        LayerMapError, LayerMapping,
    )
except ImproperlyConfigured:
    pass
