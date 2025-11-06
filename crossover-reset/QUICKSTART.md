# Quick Start Guide

## 🚀 Build in 3 Steps

### 1. Download the Files
```bash
# Download or clone the repository
cd ~/Downloads
# Extract if needed
```

### 2. Run the Build Script
```bash
cd crossover-reset
chmod +x build.sh
./build.sh
```

The script will:
- Check your Python installation
- Install required tools (py2app or PyInstaller)
- Build the standalone Mac app
- Show you where to find it

### 3. Use the App
```bash
# The app is in the dist folder
open "dist/CrossOver Reset.app"

# Or double-click it in Finder
```

That's it! 🎉

---

## 📦 Package for Distribution

To share with others:

```bash
cd dist
zip -r "CrossOver Reset.app.zip" "CrossOver Reset.app"
```

Upload `CrossOver Reset.app.zip` to GitHub releases or share it directly.

---

## ⚡ Even Faster (One Command)

If you trust automation:

```bash
cd crossover-reset && chmod +x build.sh && ./build.sh
```

---

## 🐛 Troubleshooting

### "xcode-select: command not found"
Install Xcode Command Line Tools:
```bash
xcode-select --install
```

### "pip3: command not found"  
Install or upgrade Python:
```bash
# Check if Python 3 is installed
python3 --version

# If not, install from https://www.python.org
```

### "Permission denied" when running app
On other Macs, users may need to:
```bash
xattr -cr "CrossOver Reset.app"
```
Or right-click → Open (first time only)

---

## 📖 Full Documentation

See `README.md` for complete details, technical info, and advanced options.
