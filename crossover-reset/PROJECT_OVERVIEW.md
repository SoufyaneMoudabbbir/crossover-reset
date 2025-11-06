# CrossOver Trial Reset - Project Overview

## 📁 File Structure

```
crossover-reset/
│
├── 📱 Application Files
│   ├── crossover_reset_gui.py      # Main GUI application (tkinter)
│   └── crossover_reset_cli.py      # Original command-line version
│
├── 🔧 Build Files
│   ├── setup.py                    # py2app configuration
│   ├── build.sh                    # Automated build script ⭐
│   └── make_icon.sh                # Icon generator helper
│
├── 📚 Documentation
│   ├── README.md                   # Complete documentation
│   ├── QUICKSTART.md              # Quick build guide ⭐
│   └── PROJECT_OVERVIEW.md        # This file
│
└── 🎨 Assets (optional)
    └── icon.icns                   # App icon (create with make_icon.sh)
```

## 🎯 Key Features

### The GUI App Does:
✅ One-click reset of CrossOver trial  
✅ Kills running CrossOver processes  
✅ Resets FirstRunDate in preferences  
✅ Removes trial tracking from all bottles  
✅ Shows real-time progress and status  
✅ Displays error details when needed  

### What's Safe:
✅ All bottles remain intact  
✅ All installed Windows apps remain  
✅ All user data remains  
✅ Only trial tracking data is removed  

## 🚀 Quick Usage Guide

### For Developers (Building the app):
```bash
# Easiest way:
./build.sh

# Manual way with py2app:
pip3 install py2app
python3 setup.py py2app

# Manual way with PyInstaller:
pip3 install pyinstaller
pyinstaller --name="CrossOver Reset" --windowed --onefile crossover_reset_gui.py
```

### For End Users:
1. Download the .app file
2. Double-click to run
3. Click "Reset CrossOver Trial"
4. Done!

## 🏗️ Build Methods Comparison

| Feature | py2app | PyInstaller |
|---------|--------|-------------|
| Build Speed | Slower | Faster |
| App Size | 40-50 MB | 35-45 MB |
| macOS Integration | Better | Good |
| Setup Complexity | Medium | Easy |
| **Recommendation** | ⭐ Preferred | Alternative |

## 📦 Distribution Checklist

- [ ] Build the app (`./build.sh`)
- [ ] Test the app (`open "dist/CrossOver Reset.app"`)
- [ ] Create icon (optional, `./make_icon.sh yourimage.png`)
- [ ] Compress for distribution (`zip -r "CrossOver Reset.app.zip" "CrossOver Reset.app"`)
- [ ] Upload to GitHub releases
- [ ] Add release notes

## 🔒 Code Signing (Optional, for wider distribution)

If you want to avoid security warnings:

```bash
# 1. Get Apple Developer account ($99/year)
# 2. Create Developer ID certificate
# 3. Sign the app:
codesign --deep --force --sign "Developer ID Application: Your Name" "CrossOver Reset.app"

# 4. Notarize with Apple (requires Xcode):
xcrun notarytool submit "CrossOver Reset.app.zip" --keychain-profile "AC_PASSWORD"
```

**Note:** For personal use or GitHub distribution, code signing is optional.

## 🛠️ Technology Stack

- **Language**: Python 3.8+
- **GUI Framework**: tkinter (built-in, native on macOS)
- **Packaging**: py2app or PyInstaller
- **Platform**: macOS 10.13+

## 📊 App Behavior Flow

```
User clicks "Reset Trial"
    ↓
Kill CrossOver processes
    ↓
Reset FirstRunDate in preferences
    ↓
For each bottle:
    - Read system.reg
    - Find trial tracking entries
    - Remove 5 lines of trial data
    - Save modified registry
    ↓
Show success message
    ↓
User opens CrossOver with fresh trial
```

## 🐛 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "App is damaged" | `xattr -cr "CrossOver Reset.app"` |
| Build fails | Update py2app: `pip3 install --upgrade py2app` |
| Python not found | Install from python.org |
| Xcode tools missing | `xcode-select --install` |

## 📝 Development Notes

### Why tkinter?
- Built into Python (no extra dependencies)
- Native look on macOS with 'aqua' theme
- Lightweight and fast
- Cross-platform (bonus!)

### Why separate thread for reset?
- Keeps GUI responsive during operation
- Shows real-time progress updates
- Better user experience

### Why no backups in GUI version?
- User requested no backups for now
- Can be added as optional feature later
- Reduces code complexity

## 🎨 Customization Ideas

Want to enhance the app? Here are some ideas:

1. **Add icon**: Use `make_icon.sh` to create icon.icns
2. **Add backup option**: Toggle in settings
3. **Restore feature**: List and restore from backups
4. **Status checking**: Show current trial status
5. **Schedule resets**: Automatic periodic resets
6. **Multi-language**: Add localization
7. **Dark mode**: Support macOS dark theme

## 📄 License

Use at your own risk. Educational purposes only.

## 🙏 Credits

Based on the original CrossOver reset script, enhanced with modern GUI and packaging for easy distribution.

---

**Happy Building! 🚀**

For questions or issues, refer to README.md or create a GitHub issue.
