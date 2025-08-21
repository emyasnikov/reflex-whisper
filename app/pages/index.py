import reflex as rx

from ..states import AuthState
from ..template import template


class IndexState(AuthState):
    @rx.event
    def on_load(self):
        if not self.is_authenticated():
            return rx.redirect("/login")


@rx.page(route="/", on_load=IndexState.on_load)
def index() -> rx.Component:
    return template(lambda: rx.box(), on_load=IndexState.on_load)
