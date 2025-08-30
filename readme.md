# Comic Book Archive Page Remover

This project provides a Python script to remove the last page from `.cbr` (RAR) or `.cbz` (ZIP) comic book archive files. The script creates a new modified file while preserving the original. CBR files are converted to CBZ format in the output.

## Features

- Remove the last page from CBZ (ZIP) and CBR (RAR) comic archives
- Preserves original file and creates a new `_modified.cbz` file
- Converts CBR files to CBZ format for better compatibility
- Comprehensive error handling for missing files, empty archives, and unsupported formats
- Natural sorting of pages to maintain correct order

## Requirements

- Python 3.x
- `rarfile` library (can be installed via `pip install rarfile`)
- `unittest` library (comes with Python)

## Installation

1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```bash
   pip install rarfile
   ```

## Usage

### Command Line

Run the script directly:

```bash
python deleteLastPage.py
```

### As a Module

Import and use the function in your code:

```python
from deleteLastPage import delete_last_page

try:
    delete_last_page('example.cbz')
    print("Successfully removed last page!")
except (ValueError, FileNotFoundError) as e:
    print(f"Error: {e}")
```

The script will create a new file with `_modified` appended to the original file name, without the last page. CBR files will be converted to CBZ format.

## Running Unit Tests

The project includes unit tests to verify the functionality of the `delete_last_page` function. To run the tests, use the following command:

```bash
python -m unittest discover
```

## Project Structure

```
.
├── deleteLastPage.py
├── test_deleteLastPage.py
├── readme.md
├── LICENSE
```

## Function Overview

### delete_last_page

```python
def delete_last_page(file_name):
    """
    Deletes the last page from a .cbr or .cbz file.

    Args:
        file_name (str): The name of the .cbr or .cbz file.

    Raises:
        ValueError: If the file extension is not .cbr or .cbz, or if archive is empty.
        FileNotFoundError: If the file does not exist.
    """
```

## Error Handling

The script includes robust error handling for:

- **File not found**: Raises `FileNotFoundError` if the specified file doesn't exist
- **Empty archives**: Raises `ValueError` if the archive contains no files
- **Unsupported formats**: Raises `ValueError` for non-CBR/CBZ files
- **Corrupted archives**: Handles malformed archive files gracefully

## Unit Tests Overview

### test_delete_last_page_cbz

Tests the deletion of the last page from a `.cbz` file and verifies the output.

### test_delete_last_page_cbr

Tests error handling for CBR files (note: creating test CBR files requires external tools).

### test_unsupported_file_format

Tests that a `ValueError` is raised for unsupported file extensions.

### test_single_page_cbz

Tests handling of archives with only one page (results in empty archive).

### test_non_existent_file

Tests that `FileNotFoundError` is raised for missing files.

### test_empty_archive

Tests that `ValueError` is raised for empty archives.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions are welcome! Please fork the repository and create a pull request.

## Author

Subhajit Ganguly

## Known Limitations

- CBR files are converted to CBZ format in the output (this is actually beneficial for compatibility)
- The `rarfile` library is read-only, so creating test CBR files requires external tools
- Page ordering relies on natural string sorting, which works well for most comic naming conventions

## Acknowledgements

- The `zipfile` and `rarfile` libraries for handling ZIP and RAR files, respectively.
- Python's `tempfile` module for safe temporary file operations.
