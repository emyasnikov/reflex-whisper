import reflex as rx


def link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="md", weight="medium"),
        href=url,
    )


def navbar(title: str, links: dict) -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        "languages",
                        border_radius="25%",
                        height="auto",
                        width="2.25em",
                    ),
                    rx.heading(
                        title,
                        size="4",
                        weight="bold",
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    *[link(text, url) for text, url in links.items()],
                    spacing="5",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        ),
                    ),
                    rx.menu.content(
                        rx.menu.item("Logout"),
                    ),
                    justify="end",
                ),
                align_items="center",
                justify="between",
            ),
        ),
        bg=rx.color("gray", 3),
        padding="1em",
        width="100%",
    )
