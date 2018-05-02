from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
import messenger.routing


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': SessionMiddlewareStack(AuthMiddlewareStack(
        URLRouter(
            messenger.routing.websocket_urlpatterns
        )
    )),
})
