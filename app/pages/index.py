import reflex as rx

from ..template import template


class IndexState():
    pass


@rx.page(route="/")
@template
def index() -> rx.Component:
    return rx.box()
