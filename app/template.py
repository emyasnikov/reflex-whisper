import reflex as rx

from .components.navbar import navbar
from .states import AuthState
from rxconfig import config
from typing import Callable


def template(
    page: Callable[[], rx.Component],
) -> rx.Component:
    return rx.vstack(
        navbar(
            config.title,
            {
                "Home": "/",
            },
            AuthState.on_logout,
        ),
        rx.hstack(
            rx.container(page()),
        ),
        width="100%",
    )
