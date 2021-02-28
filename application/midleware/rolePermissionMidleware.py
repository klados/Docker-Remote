from flask import redirect, session, request, flash
from functools import wraps


def role_required(roles):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('role') not in roles:
                flash("Sorry, You do not have permission", "danger")
                return redirect(request.referrer)
            return f(*args, **kwargs)
        return decorated_function
    return wrapper
