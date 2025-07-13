from django.core.cache import cache
from .models import Property

def get_all_properties():
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.all().values(
            'title', 'description', 'price', 'location', 'created_at'
        ))
        cache.set('all_properties', properties, timeout=3600)  # Cache for 1 hour
    return properties
