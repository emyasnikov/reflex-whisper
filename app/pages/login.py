import hashlib
import reflex as rx

from ..models import User


class LoginState(rx.State):
    @rx.event
    def login(self, form_data: dict):
        with rx.session() as session:
            user = session.exec(
                User.select().where(User.name == form_data["username"])
            ).first()
            if not user or user.password != hashlib.sha256(form_data["password"].encode()).hexdigest():
                yield rx.toast.error("Invalid username or password!")
                return rx.redirect("/login")
            rx.session.set("user_id", user.id)
            rx.session.set("username", user.name)
        yield rx.toast.success("Login successful!")
        return rx.redirect("/")


@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return rx.form(
        rx.card(
            rx.flex(
                rx.heading("Login"),
                rx.input(
                    name="username",
                    placeholder="Username",
                ),
                rx.input(
                    name="password",
                    placeholder="Password",
                    type="password",
                ),
                rx.button("Login", type="submit"),
                rx.text("Not registered? ", rx.link("Signup", href="/signup")),
                direction="column",
                spacing="4",
                width="100%",
            ),
            margin="auto",
            margin_top="30vh",
            width="300px",
            padding="20px",
        ),
        on_submit=LoginState.login,
        reset_on_submit=True,
    )
