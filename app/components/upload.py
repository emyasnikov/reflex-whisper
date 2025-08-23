import reflex as rx


class UploadState(rx.State):
    current: int = 0
    files: list[str] = []
    total: int = 0
    uploading: bool = False

    @rx.event
    async def upload(self, files: list[rx.UploadFile]):
        for file in files:
            data = await file.read()
            self.total += len(data)
            path = rx.get_upload_dir() / file.name
            with path.open("wb") as f:
                f.write(data)
            self.files.append(file.name)

    @rx.event
    def progress(self, progress: dict):
        self.uploading = True
        self.current = round(progress["progress"] * 100)
        if self.current >= 100:
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
        rx.progress(value=UploadState.current, max=100),
        rx.cond(
            ~UploadState.uploading,
            rx.button(
                "Upload",
                on_click=UploadState.upload(
                    rx.upload_files(
                        upload_id="upload",
                        on_upload_progress=UploadState.progress,
                    ),
                ),
            ),
        ),
        rx.foreach(
            UploadState.files,
            lambda f: rx.audio(src=rx.get_upload_url(f))
        ),
    )
