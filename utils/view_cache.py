# utils/view_cache.py
from django.core.cache import cache
from hashlib import md5
from functools import wraps
from django.http import JsonResponse

def cache_page_view(timeout=300):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if request.method != 'GET':
                return view_func(request, *args, **kwargs)

            key_str = request.get_full_path()
            cache_key = md5(key_str.encode()).hexdigest()

            cached_response = cache.get(cache_key)
            if cached_response is not None:
                return cached_response

            response = view_func(request, *args, **kwargs)
            cache.set(cache_key, response, timeout)
            return response
        return wrapped_view
    return decorator
