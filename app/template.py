import reflex as rx

from .components.navbar import navbar
from .states import AuthState
from rxconfig import config
from typing import Callable


def template(
    page: Callable[[], rx.Component],
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
    )
