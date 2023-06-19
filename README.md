# django-chat-app





### How i understand it💀
I guess the confusing bit,for me,was understanding that django and websockets are independant hence they have different docs

Web socket documentation : <https://developer.mozilla.org/en-US/docs/Web/API/WebSocket>

django channels : <https://channels.readthedocs.io/en/stable/introduction.html>

> the first thing before starting is reading up on the web socket documentation so that you undertand more of less what is going on in regrards to the client side

### Now how do these work together?
well channels basically provide the backend functionality while web sockets handles the client/front-end side of things (meaning it’s always watching for new changes and sends it to server the server then does whatever is necessary with that info(if chat application then it would send that data back to client to display to user) 

