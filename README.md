# django-chat-app

![chatapp](https://github.com/David-code-hub/django-chat-app/assets/55393687/c48d8868-c090-4f13-89a6-c479136984a0)


The confusing bit was understanding that django and websockets are independant, but can work interdependantly.


> [!TIP]
> Before starting read up on the web socket documentation so that you understand more or less what is going on in regrards to the client side

### Now how do these work together?🤔

Channels provide the backend functionality while web sockets handles the client/front-end side of things (meaning it’s always watching for new changes).

#### Links to docs
Web socket documentation : <https://developer.mozilla.org/en-US/docs/Web/API/WebSocket>

django channels : <https://channels.readthedocs.io/en/stable/introduction.html>
