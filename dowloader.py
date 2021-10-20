from pytube import YouTube


def calculate_progress_to_zero(maxSize, current):
    remaining = maxSize - current
    return (remaining / maxSize) * 100


class Downloader:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.size = -1
        self.yt = YouTube(url)
        self.yt.register_on_progress_callback(self.progress)

    def run(self):
        self.yt.streams \
            .filter(only_audio=True, file_extension='mp4') \
            .desc() \
            .first() \
            .download(output_path=self.path)

    def progress(self, stream, chunk_bytes, bytes_remaining):
        if self.size == -1 and bytes_remaining != 0:
            self.size = bytes_remaining