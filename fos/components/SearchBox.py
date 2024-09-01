from textual.app import ComposeResult
from textual.widgets import Static


class SearchBox(Static):
    def compose(self) -> ComposeResult:
        yield Static("Search", id="search")
