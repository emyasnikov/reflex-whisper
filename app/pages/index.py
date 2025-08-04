import reflex as rx

from rxconfig import config


class IndexState(rx.State):
    pass


@rx.page(route="/")
def index() -> rx.Component:
    return rx.text(config.app_name)
