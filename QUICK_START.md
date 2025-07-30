# 🚀 Quick Start Guide

## Get Started in 3 Steps

### 1. Install Dependencies
```bash
# For Kali Linux (recommended)
python3 -m venv venv
venv/bin/pip install -r requirements.txt

# For other Linux distributions
pip3 install -r requirements.txt
```

### 2. Run the Application
```bash
# With virtual environment
venv/bin/python main.py

# With system Python
python3 main.py

# Or use the launcher script
./run.sh
```

### 3. Generate Your First Wordlist

#### Option A: Standard Generation
1. Select "Standard Generation" mode
2. Set password length (e.g., 4)
3. Select character sets (e.g., lowercase + digits)
4. Click "Generate Wordlist"
5. Choose save location
6. Wait for completion!

#### Option B: Custom Words Generation
1. Select "Custom Words Generation" mode
2. Enter your words (e.g., "admin", "password", "user")
3. Select modifications (e.g., add numbers, capitalize)
4. Click "Generate Wordlist"
5. Choose save location
6. Wait for completion!

## 🎯 Examples

### Example 1: Standard Generation - 4-character passwords with lowercase letters

**Settings:**
- Mode: Standard Generation
- Length: 4
- Character sets: Lowercase letters only
- Result: 456,976 combinations (~2.2 MB file)

**Time:** ~1 second

### Example 2: Custom Words - Company-specific passwords

**Settings:**
- Mode: Custom Words Generation
- Words: "company", "corp", "inc", "ltd"
- Modifications: Add numbers, capitalize
- Result: ~1,200 passwords (~12 KB file)

**Time:** ~0.1 seconds

## ⚠️ Safety Warnings

- **Large wordlists** can consume significant disk space
- **Long passwords** with many character sets can take hours/days
- **Always check** the estimated size before generating

## 🛠️ Troubleshooting

**"No module named 'customtkinter'"**
```bash
pip3 install customtkinter pillow
```

**"Permission denied" on run.sh**
```bash
chmod +x run.sh
```

**GUI not appearing**
- Ensure you have a display server running (X11, Wayland)
- Try running from terminal: `python3 main.py`

## 📁 File Structure
```
password-wordlist-generator/
├── main.py              # Main application
├── utils.py             # Utility functions
├── requirements.txt     # Dependencies
├── install.sh          # Installation script
├── run.sh              # Launcher script
├── test_app.py         # Test suite
├── demo.py             # Demo script
└── README.md           # Full documentation
```

## 🎉 You're Ready!

The application features:
- ✅ Real-time progress tracking
- ✅ Size warnings for large wordlists
- ✅ Custom character support
- ✅ Threaded generation (non-blocking UI)
- ✅ File save dialog
- ✅ Cross-platform compatibility

**Happy password testing! 🔐** 
