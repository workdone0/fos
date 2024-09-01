from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Container
from fos.components.SearchBox import SearchBox
from fos.components.FileExplorer import FileExplorer


class SidePanel(Static):
    def compose(self) -> ComposeResult:
        yield Container(Container(FileExplorer(), SearchBox(), classes="vertical-layout"), classes="layout")
