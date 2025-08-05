import hashlib
import reflex as rx

from ..models import User


class SignupState(rx.State):
    @rx.event
    def signup(self, form_data: dict):
        with rx.session() as session:
            user = session.exec(
                User.select().where(User.name==form_data["username"])
            ).first()
            if user:
                yield rx.toast.error("User already exists!")
                return rx.redirect("/signup")
            user = User(
                name=form_data["username"],
                password=hashlib.sha256(form_data["password"].encode()).hexdigest(),
            )
            session.add(user)
            session.commit()
        yield rx.toast.success("User created successfully!")
        return rx.redirect("/")


@rx.page(route="/signup", title="Signup")
def signup() -> rx.Component:
    return rx.form(
        rx.card(
            rx.flex(
                rx.heading("Signup"),
                rx.input(
                    name="username",
                    placeholder="Username",
                ),
                rx.input(
                    name="password",
                    placeholder="Password",
                    type="password",
                ),
                rx.button("Signup", type="submit"),
                rx.text("Already registered? ", rx.link("Login", href="/login")),
                direction="column",
                spacing="4",
                width="100%",
            ),
            margin="auto",
            margin_top="30vh",
            width="300px",
            padding="20px",
        ),
        on_submit=SignupState.signup,
        reset_on_submit=True,
    )
