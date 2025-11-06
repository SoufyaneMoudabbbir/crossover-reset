# ✅ GitHub Upload Checklist

Quick checklist to get your app on GitHub.

---

## Before You Start

- [ ] GitHub account created
- [ ] App built successfully (`dist/CrossOver Reset.app` exists)
- [ ] Git installed (`git --version` works)

---

## Step 1: Create Repository

- [ ] Go to https://github.com
- [ ] Click **"+"** → **"New repository"**
- [ ] Name: `crossover-reset`
- [ ] Set to **Public**
- [ ] Add MIT License
- [ ] Click **"Create repository"**

---

## Step 2: Prepare Files

```bash
# In your project folder
cd ~/Projects/crossover-reset

# Replace README with GitHub version
cp README_GITHUB.md README.md

# Edit to add your GitHub username
nano README.md
# (Replace YOUR_USERNAME with SoufyaneMoudabbbir)
```

- [ ] README updated with your username

---

## Step 3: Upload Code

```bash
# Initialize git
git init
git add .
git commit -m "Initial commit: CrossOver Trial Reset Mac App"

# Push to GitHub
git remote add origin https://github.com/SoufyaneMoudabbbir/crossover-reset.git
git branch -M main
git push -u origin main
```

- [ ] Code pushed to GitHub

---

## Step 4: Create Release

```bash
# Create zip of app
cd dist
zip -r "CrossOver.Reset.app.zip" "CrossOver Reset.app"
```

- [ ] Zip file created

**On GitHub:**
1. Go to your repository
2. Click **"Releases"** → **"Create a new release"**
3. Tag: `v1.0.0`
4. Title: `CrossOver Reset v1.0.0`
5. Add description (see GITHUB_UPLOAD_GUIDE.md)
6. Upload `CrossOver.Reset.app.zip`
7. Click **"Publish release"**

- [ ] Release published
- [ ] App zip uploaded

---

## Step 5: Share

- [ ] Test download link works
- [ ] Share on social media
- [ ] Post on Reddit (r/macapps)

---

## 🎉 You're Done!

Your app is live at:
`https://github.com/SoufyaneMoudabbbir/crossover-reset`

Download link:
`https://github.com/SoufyaneMoudabbbir/crossover-reset/releases`

---

## Need Help?

See **GITHUB_UPLOAD_GUIDE.md** for detailed instructions!
