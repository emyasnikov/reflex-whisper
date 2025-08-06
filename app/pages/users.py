import reflex as rx

from ..components.table import header_cell
from ..models import User
from ..template import template


class UsersState(rx.State):
    users: list[User] = []
    current_user: User = User()

    def load_users(self) -> list[User]:
        with rx.session() as session:
            self.users = session.exec(
                User.select()
            ).all()

    def on_delete(self, user_id: int):
        pass


def show_user(user: User) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.created_at),
        rx.table.cell(
            rx.icon_button(
                rx.icon("trash-2", size=18),
                on_click=lambda: UsersState.on_delete(user.id),
                color_scheme="red",
                variant="ghost",
            ),
        ),
        align="center",
        style={"_hover": {"bg": rx.color("gray", 3)}},
    )


@rx.page(route="/users")
@template
def users() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                header_cell("user", "Name"),
                header_cell("calendar", "Created at"),
                header_cell("settings-2", "Actions"),
            ),
        ),
        rx.table.body(rx.foreach(UsersState.users, show_user)),
        on_mount=UsersState.load_users,
    )
