from textual.app import ComposeResult
from textual.widgets import Static, DirectoryTree


class FileExplorer(Static):
    def compose(self) -> ComposeResult:
        yield DirectoryTree("./", id="file-ex", classes="border")
