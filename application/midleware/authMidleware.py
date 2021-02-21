from flask import redirect, session, url_for
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login'), code=302)
        return f(*args, **kwargs)
    return decorated_function
