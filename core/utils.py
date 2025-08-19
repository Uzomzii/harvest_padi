from functools import wraps
from django.http import HttpResponseForbidden

def get_role(request, default="farmer"):
    return request.session.get("role", default)

def role_required(*allowed_roles):
    def deco(view):
        @wraps(view)
        def _wrapped(request, *args, **kwargs):
            role = get_role(request)
            if role not in allowed_roles:
                return HttpResponseForbidden("Not allowed for your role in this demo.")
            return view(request, *args, **kwargs)
        return _wrapped
    return deco
