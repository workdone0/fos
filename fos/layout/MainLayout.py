from textual.app import ComposeResult
from textual.widgets import Static


class MainLayout(Static):
    def compose(self) -> ComposeResult:
        yield Static("Two", classes="horizontal-layout border")
