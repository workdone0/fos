from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Vertical


class FileExplorer(Static):
    def compose(self) -> ComposeResult:
        yield Static("File Viewer", id="file-ex")
