from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
        response.headers['Cache-Control'] = 'public, max-age=0'
        return response
        
    return update_wrapper(no_cache, view)