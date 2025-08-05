import reflex as rx

from ..mixins import AuthMixin
from rxconfig import config


class IndexState(AuthMixin, rx.State):
    @rx.event
    def on_load(self):
        if not self.is_authenticated():
            return rx.redirect("/login")


@rx.page(on_load=IndexState.on_load)
def index() -> rx.Component:
    return rx.box(rx.text(config.app_name))
