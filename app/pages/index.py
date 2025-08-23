import reflex as rx

from ..components.upload import upload_file
from ..template import template


class IndexState():
    pass


@rx.page(route="/")
@template
def index() -> rx.Component:
    return rx.box(
        upload_file()
    )
