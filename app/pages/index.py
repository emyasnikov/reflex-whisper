import reflex as rx

from rxconfig import config


class IndexState(rx.State):
    def is_authenticated(self) -> bool:
        return False

    @rx.event
    def on_load(self):
        if not self.is_authenticated():
            return rx.redirect("/login")


@rx.page(on_load=IndexState.on_load)
def index() -> rx.Component:
    return rx.box(rx.text(config.app_name))
