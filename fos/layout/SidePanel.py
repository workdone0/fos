from textual.app import ComposeResult
from textual.widgets import Static, Input
from textual.containers import Container
from fos.components.SearchBox import SearchBox
from fos.components.FileExplorer import FileExplorer


class SidePanel(Static):
    def on_input_changed(self, message: Input.Changed) -> None:
        self.query_one(FileExplorer).search = message.value

    def compose(self) -> ComposeResult:
        yield Container(Container(FileExplorer(), SearchBox(), classes="vertical-layout"), classes="horizontal-layout")
