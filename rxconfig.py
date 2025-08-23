import reflex as rx

config = rx.Config(
    app_name="app",
    db_url="sqlite:///aki_nlp.db",
    env=rx.Env.DEV,
    nav_links={
        "Home": "/",
        "Users": "/users",
    },
    plugins=[
        rx.plugins.TailwindV4Plugin(),
    ],
    title="AKI NLP",
)
