from pathlib import Path
import typer
from textual.app import App, ComposeResult

from fos.components.FileExplorer import FilteredDirectoryTree
from fos.layout import MainLayout, SidePanel
from textual.binding import Binding
from textual.widgets import Footer, Header, DirectoryTree, Static
from rich.syntax import Syntax
from rich.traceback import Traceback

app_cli = typer.Typer()


class Layout(App):
    CSS_PATH = "styles/main.tcss"
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="c", action="collapse", description="Collapse Directory Tree"),
        Binding(key="e", action="expand", description="Expand Directory Tree"),
    ]

    def __init__(self, path: Path | None = None) -> None:
        super().__init__()
        self.path = path

    def on_mount(self) -> None:
        self.title = "FOS"
        self.sub_title = "find on asteroids"

    def action_collapse(self):
        tree: DirectoryTree = self.query_one(FilteredDirectoryTree)
        tree.root.collapse_all()
        tree.root.expand()

    def action_expand(self):
        tree: DirectoryTree = self.query_one(FilteredDirectoryTree)
        tree.root.expand_all()

    def on_directory_tree_file_selected(
            self, event: DirectoryTree.FileSelected
    ) -> None:
        """Called when the user clicks a file in the directory tree."""
        event.stop()
        code_view = self.query_one("#code", Static)
        try:
            syntax = Syntax.from_path(
                str(event.path),
                line_numbers=True,
                word_wrap=False,
                indent_guides=True,
                theme="lightbulb",
            )
        except Exception:
            code_view.update(Traceback(theme="github-dark", width=None))
            self.sub_title = "ERROR"
        else:
            code_view.update(syntax)
            self.query_one("#code-view").scroll_home(animate=False)
            self.sub_title = str(event.path)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True, icon="")
        yield SidePanel.SidePanel(path=self.path)
        yield MainLayout.MainLayout()
        yield Footer()


@app_cli.command()
def run(path: Path = typer.Option(None, help="Optional path to start the DirectoryTree from")):
    if path and not path.exists():
        typer.echo(f"Error: The provided path '{path}' does not exist.")
        raise typer.Exit(code=1)
    app = Layout(path)
    app.run()


if __name__ == "__main__":
    app_cli()
