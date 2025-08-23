import reflex as rx

from .components.navbar import navbar
from .states import AuthState
from rxconfig import config
from typing import Callable, Optional


def template(page: Optional[Callable[[], rx.Component]] = None, *, on_load: Optional[Callable] = None) -> rx.Component:
    def apply(page_fn: Callable[[], rx.Component]) -> rx.Component:
        return rx.box(
            navbar(
                config.title,
                config.nav_links,
                AuthState.on_logout,
            ),
            rx.container(page()),
            on_mount=on_load or AuthState.on_load,
        )
    if page is not None and callable(page):
        return apply(page)

    def decorator(page_fn: Callable[[], rx.Component]):
        return apply(page_fn)

    return decorator
