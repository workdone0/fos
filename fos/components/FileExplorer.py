from pathlib import Path
from typing import Iterable

from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DirectoryTree


class FileExplorer(Widget):
    search = reactive("", recompose=True)

    def compose(self) -> ComposeResult:
        yield FilteredDirectoryTree("./", search_query=self.search)


class FilteredDirectoryTree(DirectoryTree):
    def __init__(self, path: str | Path, search_query):
        super().__init__(path)
        self.search = search_query

    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        def contains_search_term(path: Path) -> bool:
            if self.search.lower() in path.name.lower():
                return True
            if path.is_dir():
                for subpath in path.iterdir():
                    if contains_search_term(subpath):
                        return True
            return False

        return [path for path in paths if contains_search_term(path)]
