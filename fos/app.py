from textual.app import App, ComposeResult
from layout import MainLayout, SidePanel
from textual.containers import Container


class Layout(App):
    CSS_PATH = "styles/main.tcss"

    def compose(self) -> ComposeResult:
        yield SidePanel.SidePanel()
        yield MainLayout.MainLayout()


if __name__ == "__main__":
    app = Layout()
    app.run()
