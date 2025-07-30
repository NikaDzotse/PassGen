# 🔐 Password Wordlist Generator

A modern, user-friendly GUI application for generating custom password wordlists for security testing and penetration testing purposes.

![Password Wordlist Generator](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)

## ✨ Features

- **Modern GUI**: Clean, dark-themed interface built with CustomTkinter
- **Two Generation Modes**: Standard (all combinations) and Custom Words (based on your input)
- **Flexible Character Sets**: Choose from uppercase, lowercase, digits, and symbols
- **Custom Characters**: Add your own special characters (Unicode support)
- **Word Modifications**: Capitalize, reverse, leet speak, add numbers/symbols to custom words
- **Real-time Preview**: See character set and estimated combinations before generating
- **Progress Tracking**: Real-time progress bar and generation counter
- **Size Warnings**: Automatic warnings for large wordlists that could take a long time
- **Threaded Generation**: Non-blocking UI during wordlist generation
- **File Save Dialog**: Choose where to save your wordlist
- **Cross-platform**: Works on Linux, Windows, and macOS

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/password-wordlist-generator.git
   cd password-wordlist-generator
   ```

2. **Install dependencies:**

   **Option A: Using virtual environment (recommended for Kali Linux):**
   ```bash
   python3 -m venv venv
   venv/bin/pip install -r requirements.txt
   ```

   **Option B: Using pipx (alternative):**
   ```bash
   pipx install customtkinter pillow
   ```

   **Option C: System-wide installation (not recommended on Kali):**
   ```bash
   pip install -r requirements.txt --break-system-packages
   ```

3. **Run the application:**

   **With virtual environment:**
   ```bash
   venv/bin/python main.py
   ```

   **With pipx or system installation:**
   ```bash
   python3 main.py
   ```

## 📖 Usage Guide

### Basic Usage

#### Standard Generation Mode
1. **Select "Standard Generation"** mode
2. **Set Password Length**: Enter the desired password length (1-20 characters)
3. **Select Character Sets**: Choose which character types to include:
   - ✅ Uppercase letters (A-Z)
   - ✅ Lowercase letters (a-z)
   - ✅ Digits (0-9)
   - ✅ Symbols (!@#$%^&*)
4. **Add Custom Characters** (Optional): Enter additional characters like `ñ`, `é`, `中文`
5. **Preview**: Check the estimated number of combinations
6. **Generate**: Click "Generate Wordlist" and choose where to save the file

#### Custom Words Mode
1. **Select "Custom Words Generation"** mode
2. **Enter Your Words**: Type your custom words (one per line or separated by commas)
3. **Select Word Modifications**:
   - ✅ Add numbers (0-9) before/after words
   - ✅ Add symbols (!@#$%^&*) before/after words
   - ✅ Capitalize variations (Admin, ADMIN, admin)
   - ✅ Reverse words (admin → nimda)
   - ✅ Leet speak (admin → @dm1n)
4. **Preview**: See estimated number of generated passwords
5. **Generate**: Click "Generate Wordlist" and choose where to save the file

### Advanced Features

#### Generation Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Standard Generation** | Generate all possible combinations | Brute force attacks, comprehensive testing |
| **Custom Words** | Generate variations of your words | Targeted attacks, company-specific testing |

#### Character Set Combinations

| Character Set | Characters | Example |
|---------------|------------|---------|
| Uppercase | A-Z (26 chars) | `ABCDEFGHIJKLMNOPQRSTUVWXYZ` |
| Lowercase | a-z (26 chars) | `abcdefghijklmnopqrstuvwxyz` |
| Digits | 0-9 (10 chars) | `0123456789` |
| Symbols | Special chars (32 chars) | `!@#$%^&*()_+-=[]{}|;:,.<>?` |
| Custom | User-defined | Any Unicode characters |

#### Word Modifications (Custom Words Mode)

| Modification | Description | Example |
|--------------|-------------|---------|
| **Add Numbers** | Add 0-9 before/after words | `admin` → `admin1`, `1admin` |
| **Add Symbols** | Add symbols before/after words | `admin` → `admin!`, `!admin` |
| **Capitalize** | Create case variations | `admin` → `Admin`, `ADMIN`, `admin` |
| **Reverse** | Reverse word order | `admin` → `nimda` |
| **Leet Speak** | Replace letters with symbols | `admin` → `@dm1n` |

#### Size Estimation Examples

##### Standard Generation
| Length | Charset Size | Combinations | File Size (approx) |
|--------|--------------|--------------|-------------------|
| 4 | 62 (A-Z, a-z, 0-9) | 14,776,336 | ~150 MB |
| 6 | 26 (a-z only) | 308,915,776 | ~3 GB |
| 8 | 62 (A-Z, a-z, 0-9) | 218,340,105,584 | ~2 TB |

##### Custom Words Generation
| Base Words | Modifications | Generated Passwords | Example |
|------------|---------------|-------------------|---------|
| 4 words | Numbers + Capitalize | ~252 passwords | `admin`, `password`, `user`, `john` |
| 2 words | All modifications | ~2,758 passwords | `admin`, `password` |
| 6 words | Numbers + Symbols + Capitalize | ~3,546 passwords | Company names |

⚠️ **Warning**: Large wordlists can consume significant disk space and take a very long time to generate!

### Safety Features

- **Input Validation**: Ensures valid password length and character sets
- **Size Warnings**: Automatic warnings for wordlists > 100 million combinations
- **Progress Tracking**: Real-time progress updates during generation
- **Stop Function**: Ability to stop generation at any time
- **Error Handling**: Graceful error handling with user-friendly messages

## 🛠️ Technical Details

### Architecture

The application is built with a modular design:

```
PasswordWordlistGenerator/
├── main.py              # Main application logic
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Key Components

- **GUI Framework**: CustomTkinter for modern, responsive interface
- **Threading**: Separate thread for wordlist generation to keep UI responsive
- **File I/O**: UTF-8 encoding support for international characters
- **Memory Management**: Efficient recursive generation algorithm
- **Progress Updates**: Real-time progress tracking with UI updates

### Algorithm

The wordlist generation uses a recursive algorithm to generate all possible combinations:

```python
def generate_combinations(charset, length, file_handle):
    def generate_recursive(current, remaining_length):
        if remaining_length == 0:
            file_handle.write(current + '\n')
            return
        for char in charset:
            generate_recursive(current + char, remaining_length - 1)
    
    generate_recursive("", length)
```

## 🔧 Customization

### Themes

The application supports different appearance modes:

```python
# In main.py, change these lines:
ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
```

### Character Sets

You can modify the symbol set in the `get_character_set()` method:

```python
if self.symbols_var.get():
    charset.update("!@#$%^&*()_+-=[]{}|;:,.<>?")  # Modify this line
```

## 📦 Building Executables

### Using PyInstaller

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Build executable:**
   ```bash
   pyinstaller --onefile --windowed --name "PasswordWordlistGenerator" main.py
   ```

3. **Find the executable** in the `dist/` folder

### Using Shiv (Alternative)

1. **Install Shiv:**
   ```bash
   pip install shiv
   ```

2. **Build executable:**
   ```bash
   shiv -o password-generator.pyz -e main:main .
   ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is intended for **legitimate security testing purposes only**. Users are responsible for ensuring they have proper authorization before using this tool against any systems or networks. The authors are not responsible for any misuse of this software.

## 🐛 Troubleshooting

### Common Issues

1. **Import Error: No module named 'customtkinter'**
   - Solution: Run `pip install -r requirements.txt`

2. **GUI not appearing**
   - Solution: Ensure you have a display server running (X11 on Linux)

3. **Large wordlists taking too long**
   - Solution: Use smaller character sets or shorter password lengths

4. **Out of memory errors**
   - Solution: The application writes directly to disk, but very large wordlists may still cause issues

### System Requirements

- **Python**: 3.7 or higher
- **Memory**: 512 MB RAM minimum (more for large wordlists)
- **Disk Space**: Varies based on wordlist size
- **Display**: Any modern display server (X11, Wayland, etc.)

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed information about your problem

---

**Happy Password Testing! 🔐** 