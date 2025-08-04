import reflex as rx

config = rx.Config(
    app_name="app",
    db_url="sqlite:///aki_nlp.db",
    env=rx.Env.DEV,
    plugins=[
        rx.plugins.TailwindV4Plugin(),
    ],
)
