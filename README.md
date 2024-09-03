
# fos (Find On Steroids)

**fos** (Find On Steroids) is a powerful command-line tool written in Python using the [Textual](https://github.com/Textualize/textual) library. It allows you to search and view files within a folder effortlessly. Inspired by the [Frogmouth](https://github.com/Textualize/frogmouth) project, **fos** takes file browsing to the next level by combining search functionality with a user-friendly interface for file exploration.

## Features

- **Search and Browse Files:** Seamlessly search for files and browse through them within a specified folder.
- **Syntax Highlighting:** View file contents with syntax highlighting, making it easier to read and understand code files.
- **SidePanel Navigation:** A side panel with a DirectoryTree widget allows for easy navigation through your folder structure.

## Installation

To get started with **fos**, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/fos.git
cd fos
pip install -r requirements.txt
```

## Usage

Run **fos** by navigating to the directory where it's installed and using the following command:

```bash
python fos/app.py --path=/path/to/your/folder
```

Replace `/path/to/your/folder` with the path of the folder you wish to browse and search within. Skip the `--path` parameter if you want to view the current folder.

### Command-Line Options

- `--path`: Path to the folder you want to browse.
- `--help`: Show help message with usage details.

## Contribution

**fos** is still in active development, and we welcome contributions from the community! Some areas that need improvement include:

- **Multiple Themes:** We currently lack support for multiple themes, and contributions to add this feature are highly appreciated.
- **Image Viewing:** Support for viewing images is not yet implemented, so feel free to work on this feature.
- **Optimizations:** Any other improvements, optimizations, or feature requests are welcome.

To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Textual](https://github.com/Textualize/textual) library by [Textualize](https://github.com/Textualize) for making it easier to build rich TUI applications in Python.
- [Frogmouth](https://github.com/Textualize/frogmouth) project for the inspiration.

---

Feel free to reach out with any questions or suggestions!
