from textual.app import ComposeResult
from textual.widgets import Static, Input


class SearchBox(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="find", id="search", classes="border")
