# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat_manager.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boardgame_manager.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_manager.routing.websocket_urlpatterns
        )
    ),
})