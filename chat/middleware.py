from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from django.conf import settings
import jwt
from django.contrib.auth import get_user_model

User = get_user_model()

@database_sync_to_async
def get_user_from_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get('user_id')
        user = User.objects.get(id=user_id)
        return user
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
        return AnonymousUser()

class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return TokenAuthMiddlewareInstance(scope, self)

class TokenAuthMiddlewareInstance:
    def __init__(self, scope, middleware):
        self.scope = scope
        self.middleware = middleware

    async def __call__(self, receive, send):
        query_string = parse_qs(self.scope["query_string"].decode())
        token = query_string.get("token")
        if token:
            self.scope["user"] = await get_user_from_token(token[0])
        else:
            self.scope["user"] = AnonymousUser()

        inner = self.middleware.inner(self.scope)
        return await inner(receive, send)
