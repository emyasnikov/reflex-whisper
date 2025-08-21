import reflex as rx

from .components.navbar import navbar
from .states import AuthState
from rxconfig import config
from typing import Callable, Optional


def template(
    page: Callable[[], rx.Component],
    on_load: Optional[Callable] = None,
) -> rx.Component:
    return rx.box(
        navbar(
            config.title,
            {
                "Home": "/",
                "Users": "/users",
            },
            AuthState.on_logout,
        ),
        rx.container(page()),
        on_mount=on_load,
    )
