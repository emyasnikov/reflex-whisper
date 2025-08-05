import reflex as rx


class AuthState(rx.State):
    user_id: int | None = None
    username: str | None = None

    def is_authenticated(self) -> bool:
        return self.user_id is not None

    @rx.event
    def on_login(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username

    @rx.event
    def on_logout(self):
        self.user_id = None
        self.username = None
