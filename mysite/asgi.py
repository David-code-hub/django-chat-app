"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import chat.routing

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter( #check type of connection
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(           
            AuthMiddlewareStack(    #populate the connection’s scope with currently authenticated user
                                    #similar to how Django’s AuthenticationMiddleware populates the...
                                    #request object of a view function with the currently authenticated user. 
                URLRouter( #routes to consumer based on provided url
                    chat.routing.websockets_urlpatterns
                )   
            )
        ),
    }
)
