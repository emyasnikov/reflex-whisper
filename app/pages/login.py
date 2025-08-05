import reflex as rx


class LoginState(rx.State):
    username: str = ""
    password: str = ""

    def login(self):
        return rx.redirect("/")


@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return rx.form(
        rx.card(
            rx.flex(
                rx.heading("Login"),
                rx.input(
                    placeholder="Username",
                ),
                rx.input(
                    placeholder="Password",
                    type="password",
                ),
                rx.button("Login", on_click=LoginState.login),
                direction="column",
                spacing="4",
                width="100%",
            ),
            margin="auto",
            margin_top="30vh",
            width="300px",
            padding="20px",
        ),
    )
