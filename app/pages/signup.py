import reflex as rx


class SignupState(rx.State):
    username: str = ""
    password: str = ""

    def signup(self):
        return rx.redirect("/")


@rx.page(route="/signup", title="Signup")
def signup() -> rx.Component:
    return rx.form(
        rx.card(
            rx.flex(
                rx.heading("Signup"),
                rx.input(
                    placeholder="Username",
                ),
                rx.input(
                    placeholder="Password",
                    type="password",
                ),
                rx.button("Signup", on_click=SignupState.signup),
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
