import reflex as rx

from ..states import AuthState
from rxconfig import config


class IndexState(rx.State):
    @rx.event
    def on_load(self):
        if not AuthState.is_authenticated():
            return rx.redirect("/login")


@rx.page(on_load=IndexState.on_load)
def index() -> rx.Component:
    return rx.box(rx.text(config.app_name))
