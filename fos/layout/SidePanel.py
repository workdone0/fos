from pathlib import Path

from textual.app import ComposeResult
from textual.widgets import Static, Input, DirectoryTree
from textual.containers import Container
from fos.components.SearchBox import SearchBox
from fos.components.FileExplorer import FileExplorer, FilteredDirectoryTree


class SidePanel(Static):
    def __init__(self, path: Path | None = None):
        super().__init__()
        self.path = path

    def on_input_changed(self, message: Input.Changed) -> None:
        self.query_one(FileExplorer).search = message.value

    def compose(self) -> ComposeResult:
        yield Container(Container(FileExplorer(self.path), SearchBox(), classes="vertical-layout"),
                        classes="horizontal-layout")
