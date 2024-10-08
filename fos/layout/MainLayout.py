from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import VerticalScroll


class MainLayout(Static):

    def compose(self) -> ComposeResult:
        with VerticalScroll(classes="horizontal-layout border", id="code-view"):
            yield Static(id="code", expand=True)
