import reflex as rx

from ..states import AuthState
from ..template import template


class IndexState():
    pass


@rx.page(route="/")
def index() -> rx.Component:
    return template(lambda: rx.box(), on_load=AuthState.on_load)
