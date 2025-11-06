# 🚀 How to Upload to GitHub & Create Releases

Complete step-by-step guide to share your CrossOver Reset app on GitHub.

---

## 📋 Prerequisites

- GitHub account (create one at https://github.com)
- Git installed on your Mac
- Your built app in the `dist` folder

---

## Part 1: Create GitHub Repository

### Step 1: Create New Repository on GitHub

1. Go to https://github.com
2. Click the **"+"** button (top right) → **"New repository"**
3. Fill in:
   - **Repository name:** `crossover-reset`
   - **Description:** "Reset CrossOver trial period on macOS with one click"
   - **Public** (so anyone can download)
   - ✅ Check **"Add a README file"** (we'll replace it)
   - **License:** Choose "MIT License"
4. Click **"Create repository"**

---

## Part 2: Upload Your Code

### Step 2: Prepare Your Files

```bash
# Go to your project folder
cd ~/Projects/crossover-reset

# Replace the README with the GitHub version
cp README_GITHUB.md README.md

# Edit README.md and replace YOUR_USERNAME with your GitHub username
nano README.md
# Press Ctrl+X, then Y, then Enter to save
```

### Step 3: Initialize Git (if not already)

```bash
# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: CrossOver Trial Reset Mac App"
```

### Step 4: Push to GitHub

```bash
# Connect to your GitHub repo (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/crossover-reset.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**If asked for credentials:**
- Username: your GitHub username
- Password: use a **Personal Access Token** (not your password)
  - Create token at: https://github.com/settings/tokens
  - Select: `repo` permissions
  - Copy the token and use it as password

---

## Part 3: Create a Release (So Users Can Download)

### Step 5: Prepare the App for Release

```bash
# Go to your dist folder
cd dist

# Create a zip file of the app
zip -r "CrossOver.Reset.app.zip" "CrossOver Reset.app"

# Verify the zip was created
ls -lh CrossOver.Reset.app.zip
```

### Step 6: Create Release on GitHub

1. Go to your repository: `https://github.com/YOUR_USERNAME/crossover-reset`
2. Click **"Releases"** (right sidebar)
3. Click **"Create a new release"**
4. Fill in:
   - **Tag version:** `v1.0.0`
   - **Release title:** `CrossOver Reset v1.0.0`
   - **Description:**
   ```markdown
   ## CrossOver Trial Reset v1.0.0
   
   Reset your CrossOver trial period with one click!
   
   ### 🎯 For Users
   1. Download `CrossOver.Reset.app.zip` below
   2. Unzip the file
   3. Right-click → Open (first time only)
   4. Click "Reset CrossOver Trial" button
   5. Done! 🎉
   
   ### ✨ Features
   - One-click trial reset
   - Safe - keeps all bottles and apps intact
   - Native macOS interface
   - Real-time progress updates
   
   ### 📋 Requirements
   - macOS 10.13 or later
   - CrossOver installed
   
   ### ⚠️ First-Time Use
   Right-click the app and select "Open" to bypass macOS security warning.
   
   ### 🐛 Issues?
   Report bugs in the [Issues](https://github.com/YOUR_USERNAME/crossover-reset/issues) tab.
   ```

5. **Attach the app:**
   - Scroll down to **"Attach binaries"**
   - Click and drag `CrossOver.Reset.app.zip` from your Finder
   - Wait for upload to complete

6. Click **"Publish release"**

---

## Part 4: Update Your README

### Step 7: Fix Download Links

1. After creating the release, copy the release URL
2. Edit your README on GitHub:
   - Click **README.md** in your repo
   - Click the **pencil icon** (edit)
   - Replace `YOUR_USERNAME` with your actual GitHub username
   - Save (click "Commit changes")

---

## 🎉 Done! Your App is Now Public

Your repository is now live at:
```
https://github.com/YOUR_USERNAME/crossover-reset
```

Users can download from:
```
https://github.com/YOUR_USERNAME/crossover-reset/releases
```

---

## 📱 Share Your App

Share these links:
- **Repository:** `https://github.com/YOUR_USERNAME/crossover-reset`
- **Direct Download:** `https://github.com/YOUR_USERNAME/crossover-reset/releases/latest`

Post on:
- Reddit: r/macapps, r/CrossOver
- Twitter/X with #macOS #CrossOver
- MacRumors forums
- Your social media

---

## 🔄 Updating Your App Later

### When you make changes:

```bash
# 1. Make your changes to the code

# 2. Rebuild the app
./build.sh

# 3. Commit changes
git add .
git commit -m "Update: description of changes"
git push

# 4. Create new release
cd dist
zip -r "CrossOver.Reset.app.zip" "CrossOver Reset.app"

# 5. Go to GitHub → Releases → Create new release
# Use tag v1.1.0, v1.2.0, etc.
# Upload the new zip file
```

---

## 🛠️ Optional: Add a Workflow Badge

Add this to your README.md to show build status:

```markdown
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
```

---

## 📊 Track Downloads

- Go to your Releases page to see download counts
- Check **Insights** → **Traffic** to see visitors

---

## ⭐ Get Stars

Encourage users to star your repo:
- Add badges to README
- Ask in your release notes
- More stars = more visibility!

---

## 🆘 Troubleshooting

### "Permission denied" when pushing
```bash
# Use HTTPS with token or set up SSH keys
# SSH guide: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
```

### Can't upload large file
- GitHub has 100MB file limit
- Your app should be under 50MB, so this shouldn't be an issue

### Forgot to add files
```bash
git add filename
git commit -m "Add missing file"
git push
```

---

## 📝 Quick Reference Commands

```bash
# Check status
git status

# Add all changes
git add .

# Commit
git commit -m "Your message"

# Push to GitHub
git push

# Create release zip
cd dist && zip -r "CrossOver.Reset.app.zip" "CrossOver Reset.app"
```

---

**Congratulations! Your app is now on GitHub!** 🎊

Anyone in the world can now download and use your CrossOver Reset app!
