from textual.app import ComposeResult
from textual.widgets import Static, Input


class SearchBox(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Search for files or folders...", id="search", classes="border")
