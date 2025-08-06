import reflex as rx

from ..components.navbar import navbar
from ..states import AuthState
from rxconfig import config


class IndexState(AuthState):
    @rx.event
    def on_load(self):
        if not self.is_authenticated():
            return rx.redirect("/login")


@rx.page(on_load=IndexState.on_load)
def index() -> rx.Component:
    return rx.box(
        navbar(config.title, {}, IndexState.on_logout),
    )
