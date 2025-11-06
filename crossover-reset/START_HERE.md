# 🎉 Welcome to CrossOver Reset Mac App!

Your standalone Mac application is ready to build!

## 📦 What You Got

✅ **Full GUI application** - Professional interface with tkinter  
✅ **One-click reset** - Automatic trial reset  
✅ **No installation needed** - Just download and run  
✅ **Safe operation** - Keeps all bottles and apps intact  
✅ **Build scripts** - Everything automated  
✅ **Complete documentation** - Step-by-step guides  

---

## 🚀 Quick Start (3 Easy Steps)

### Step 1: Check if Ready
```bash
./check_ready.py
```
This will verify you have everything needed.

### Step 2: Build the App
```bash
./build.sh
```
Choose option 1 (py2app) or 2 (PyInstaller), then wait 2-3 minutes.

### Step 3: Test It!
```bash
open "dist/CrossOver Reset.app"
```
Or double-click in Finder!

**That's it!** 🎊

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| **QUICKSTART.md** | Fast build guide (start here!) |
| **README.md** | Complete documentation |
| **PROJECT_OVERVIEW.md** | Technical details & architecture |

---

## 📂 Project Files

```
crossover-reset/
├── 📱 crossover_reset_gui.py    ← Main GUI app
├── 🔧 build.sh                  ← Automated builder
├── ✓ check_ready.py             ← Pre-flight check
├── 🎨 make_icon.sh              ← Icon generator
├── ⚙️ setup.py                  ← py2app config
└── 📚 Documentation files       ← Guides
```

---

## 🎯 What the App Does

When users click "Reset CrossOver Trial":

1. ✓ Stops running CrossOver processes
2. ✓ Resets FirstRunDate in preferences  
3. ✓ Removes trial tracking from all bottles
4. ✓ Shows real-time progress
5. ✓ Displays success message

**Safe:** Bottles, Windows apps, and data remain intact!

---

## 🛠️ Build Options

### Option A: Automated (Recommended)
```bash
./build.sh
```
Handles everything automatically!

### Option B: Manual with py2app
```bash
pip3 install py2app
python3 setup.py py2app
```

### Option C: Manual with PyInstaller
```bash
pip3 install pyinstaller
pyinstaller --windowed --onefile crossover_reset_gui.py
```

---

## 🎨 Want a Custom Icon?

```bash
# 1. Create or download a 1024x1024 PNG image
# 2. Convert it:
./make_icon.sh yourimage.png

# 3. Rebuild with the new icon
./build.sh
```

---

## 📤 Sharing Your App

To distribute:

```bash
cd dist
zip -r "CrossOver Reset.app.zip" "CrossOver Reset.app"
```

Upload to GitHub releases or share directly!

---

## ⚠️ First-Time macOS Warning

When others download your app, macOS may show:
> "CrossOver Reset can't be opened because it's from an unidentified developer"

**Solution for users:**
1. Right-click the app → Open
2. Click "Open" in the dialog
3. App opens (only needed once!)

**Or run:**
```bash
xattr -cr "CrossOver Reset.app"
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python not found" | Install from python.org |
| "xcode-select error" | Run: `xcode-select --install` |
| Build fails | Run: `./check_ready.py` |
| "App is damaged" | Run: `xattr -cr "CrossOver Reset.app"` |

---

## 💡 Pro Tips

- Test the app before distributing
- Read QUICKSTART.md for fastest build
- Check PROJECT_OVERVIEW.md for technical details
- Add your own icon for professional look
- The app is ~40-50MB (includes Python runtime)

---

## 🎓 How It Works

The app is your Python script packaged as a native Mac application:

```
User double-clicks app
    ↓
macOS launches bundled Python
    ↓
Runs your GUI script
    ↓
Shows beautiful interface
    ↓
Resets CrossOver trial
    ↓
Success! 🎉
```

---

## 📋 Next Steps

1. **First time?** → Read **QUICKSTART.md**
2. **Ready to build?** → Run `./build.sh`
3. **Need details?** → See **README.md**
4. **Want to understand?** → Check **PROJECT_OVERVIEW.md**

---

## ✨ Features You Got

- ✅ Modern GUI with native macOS look
- ✅ Real-time progress updates
- ✅ Error handling with details
- ✅ Multi-threaded (UI stays responsive)
- ✅ Automatic process management
- ✅ Professional status logging
- ✅ Success/error notifications
- ✅ No confirmation prompts (as requested!)

---

## 🙌 You're All Set!

Everything is ready to go. Just run:

```bash
./build.sh
```

And in a few minutes, you'll have a professional Mac app!

**Questions?** Check the documentation files or create a GitHub issue.

---

**Happy Building! 🚀**

Made with ❤️ for Mac users who want CrossOver to just work.
