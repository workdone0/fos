from textual.app import App, ComposeResult
from layout import MainLayout, SidePanel
from textual.binding import Binding
from textual.widgets import Footer, Header, DirectoryTree, Static
from rich.syntax import Syntax
from rich.traceback import Traceback


class Layout(App):
    CSS_PATH = "styles/main.tcss"
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app")
    ]

    def on_mount(self) -> None:
        self.title = "FOS"
        self.sub_title = "find on asteroids"

    def on_directory_tree_file_selected(
            self, event: DirectoryTree.FileSelected
    ) -> None:
        """Called when the user click a file in the directory tree."""
        event.stop()
        code_view = self.query_one("#code", Static)
        try:
            syntax = Syntax.from_path(
                str(event.path),
                line_numbers=True,
                word_wrap=False,
                indent_guides=True,
                theme="github-dark",
            )
        except Exception:
            code_view.update(Traceback(theme="github-dark", width=None))
            self.sub_title = "ERROR"
        else:
            code_view.update(syntax)
            self.query_one("#code-view").scroll_home(animate=False)
            self.sub_title = str(event.path)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield SidePanel.SidePanel()
        yield MainLayout.MainLayout()
        yield Footer()


if __name__ == "__main__":
    app = Layout()
    app.run()
