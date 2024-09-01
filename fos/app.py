from textual.app import App, ComposeResult
from layout import MainLayout, SidePanel
from textual.binding import Binding
from textual.widgets import Footer, Header


class Layout(App):
    CSS_PATH = "styles/main.tcss"
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app")
    ]

    def on_mount(self) -> None:
        self.title = "FOS"
        self.sub_title = "find on asteroids"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield SidePanel.SidePanel()
        yield MainLayout.MainLayout()
        yield Footer()


if __name__ == "__main__":
    app = Layout()
    app.run()
