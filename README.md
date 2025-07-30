# PassGen

A modern, user-friendly GUI application for generating custom password wordlists for security testing and penetration testing purposes. Fully self-contained in one file (`main.py`) with auto-installation and virtual environment support.

![Password Wordlist Generator](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)

## Features

* Custom word generation based on user input with multiple modification options
* Modifications include capitalization, reversal, leet speak, and addition of numbers/symbols
* Real-time preview of estimated wordlist size
* Real-time progress bar and counter
* Threaded generation for responsive UI
* File dialog for saving generated wordlists
* Automatic virtual environment creation and dependency installation
* Cross-platform support (Linux, Windows, macOS)

## Quick Start

### Prerequisites

* Python 3.7 or higher

### Run the Application

```bash
python3 main.py
```

* Automatically sets up a virtual environment in `venv/`
* Installs `customtkinter` if missing
* Re-launches the app inside the virtual environment

### Optional: Manual Setup

```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python main.py
```

## Usage Guide

### Custom Words Generation

1. Enter custom words (one per line or comma-separated)
2. Select desired word modifications:

   * Add numbers (0-9)
   * Add symbols (!@#\$%^&\*)
   * Capitalize variations (Admin, ADMIN, admin)
   * Reverse words (e.g., admin to nimda)
   * Apply leet speak (e.g., admin to @dm1n)
3. View estimated combinations
4. Click "Generate Wordlist" and choose save location

### Word Modifications Summary

| Modification | Example        |
| ------------ | -------------- |
| Numbers      | admin1, 1admin |
| Symbols      | admin!, !admin |
| Capitalize   | Admin, ADMIN   |
| Reverse      | nimda          |
| Leet Speak   | @dm1n          |

### Estimated Sizes

| Words | Modifications     | Estimated Count |
| ----- | ----------------- | --------------- |
| 2     | All               | \~2,758         |
| 4     | Numbers + Capital | \~252           |
| 6     | Numbers + Symbols | \~3,546         |

Note: Very large wordlists (100,000+ entries) may require significant disk space and time.

### Safety Features

* Validates inputs before starting generation
* Warns users of large output sizes
* Real-time progress feedback
* User-initiated cancellation support
* Error messaging and exception handling

## Technical Details

### Project Structure

```
PasswordWordlistGenerator/
├── main.py              # Self-contained app with auto-venv and GUI
├── requirements.txt     # Optional dependency list
├── README.md            # Project documentation
```

### Auto Virtual Environment Bootstrapping

`main.py` creates a virtual environment and restarts the app within it:

```python
if not os.path.exists("venv/bin/python"):
    subprocess.run(["python3", "-m", "venv", "venv"])
os.execv("venv/bin/python", ["venv/bin/python"] + sys.argv)
```

### Installation-Free Execution

* Simply run `python3 main.py`
* No separate install or setup scripts required

### Required Dependency

```txt
customtkinter
```

## Packaging (Optional)

### Using PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

### Using Shiv

```bash
pip install shiv
shiv -o passwordgen.pyz -e main:main .
```

## Contributing

1. Fork the repository
2. Create a new feature branch: `git checkout -b feature`
3. Commit and push changes
4. Submit a pull request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This tool is intended strictly for authorized security testing. Users are responsible for ensuring they comply with applicable laws and regulations.

## Troubleshooting

| Issue                           | Suggested Action                            |
| ------------------------------- | ------------------------------------------- |
| No module named 'customtkinter' | Run `python3 main.py` to auto-install       |
| GUI does not appear             | Ensure you are running in a GUI environment |
| High memory usage               | Reduce the wordlist size or word length     |

---

For feedback, issues, or questions, please use the GitHub issue tracker.
