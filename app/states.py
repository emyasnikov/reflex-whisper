import reflex as rx


class AuthState(rx.State):
    logged_in: bool = False
    user_id: int | None = None
    username: str | None = None

    def is_authenticated(self) -> bool:
        return self.logged_in

    @rx.event
    def on_load(self):
        if not self.is_authenticated():
            return rx.redirect("/login")

    @rx.event
    def on_login(self, user_id: int, username: str):
        self.logged_in = True
        self.user_id = user_id
        self.username = username
        return rx.redirect("/")

    @rx.event
    def on_logout(self):
        self.logged_in = False
        self.user_id = None
        self.username = None
        return rx.redirect("/")
