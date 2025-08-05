import reflex as rx


class AuthMixin(rx.State, mixin=True):
    user_id: int | None = None
    username: str | None = None

    def is_authenticated(self) -> bool:
        return self.user_id is not None

    @rx.event
    def set_user(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
