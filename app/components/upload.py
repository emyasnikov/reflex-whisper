import reflex as rx


class UploadState(rx.State):
    files: list[str] = []
    progress: int = 0
    total: int = 0
    uploading: bool = False

    @rx.event
    async def on_upload(self, files: list[rx.UploadFile]):
        for file in files:
            data = await file.read()
            self.total += len(data)
            path = rx.get_upload_dir() / file.name
            with path.open("wb") as f:
                f.write(data)
            self.files.append(file.name)

    @rx.event
    def on_progress(self, progress: dict):
        self.uploading = True
        self.progress = round(progress["progress"] * 100)
        if self.progress >= 100:
            self.uploading = False


def upload_file():
    return rx.vstack(
        rx.upload(
            id="upload",
            accept={
                "audio/mpeg",
                "audio/wav",
            },
        ),
        rx.progress(value=UploadState.progress, max=100),
        rx.cond(
            ~UploadState.uploading,
            rx.button(
                "Upload",
                on_click=UploadState.on_upload(
                    rx.upload_files(
                        upload_id="upload",
                        on_upload_progress=UploadState.on_progress,
                    ),
                ),
            ),
        ),
        rx.foreach(
            UploadState.files,
            lambda f: rx.audio(src=rx.get_upload_url(f))
        ),
    )
