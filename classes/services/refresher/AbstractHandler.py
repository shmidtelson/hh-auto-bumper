from __future__ import annotations
from classes.services.refresher.Handler import Handler
from typing import Any, Union
from abc import abstractmethod

class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Union[str,None]:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None