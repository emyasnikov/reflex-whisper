import reflex as rx


class UploadState(rx.State):
    files: list[str] = []

    @rx.event
    async def upload(self, files: list[rx.UploadFile]):
        for file in files:
            data = await file.read()
            path = rx.get_upload_dir() / file.name
            with path.open("wb") as f:
                f.write(data)
            self.files.append(file.name)


def upload_file():
    return rx.vstack(
        rx.upload(
            id="upload",
            accept={
                "audio/mpeg",
            },
        ),
        rx.button(
            "Upload",
            on_click=UploadState.upload(rx.upload_files("upload")),
        ),
        rx.foreach(
            UploadState.files,
            lambda f: rx.audio(src=rx.get_upload_url(f))
        ),
    )
