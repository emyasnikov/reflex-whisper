import hashlib
import reflex as rx

from ..models import User


class SignupState(rx.State):
    username: str = ""
    password: str = ""

    def signup(self):
        with rx.session() as session:
            user = session.exec(
                User.select().where(User.name==self.username)
            ).first()
            if user:
                return rx.redirect("/signup")
            user = User(
                name=self.username,
                password=hashlib.sha256(self.password.encode()).hexdigest(),
            )
            session.add(user)
            session.commit()
        self.success_message = "User created successfully!"

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
