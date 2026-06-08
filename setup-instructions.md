# Setup Instructions: AI for Urban Health Course Website

Step-by-step instructions for building, previewing, and deploying the course website.

---

## 1. Install Quarto

Quarto is the tool that converts the `.qmd` files into a website.

**Option A: Homebrew (macOS)**

```bash
brew install quarto
```

**Option B: Download installer**

Go to [https://quarto.org/docs/get-started/](https://quarto.org/docs/get-started/) and download the installer for your operating system.

**Verify installation:**

```bash
quarto --version
```

You should see a version number (1.4 or later recommended).

---

## 2. Create a GitHub Repository

1. Go to [github.com](https://github.com) and sign in (or create an account)
2. Click the **+** button in the top right and select **New repository**
3. Name it something like `ai-urban-health-course`
4. Set it to **Public** (required for free GitHub Pages hosting)
5. Do NOT initialize with a README (we already have files)
6. Click **Create repository**

---

## 3. Clone the Repository Locally

```bash
# Navigate to where you want the project
cd ~/Documents

# Clone the empty repo
git clone https://github.com/YOUR-USERNAME/ai-urban-health-course.git

# Enter the directory
cd ai-urban-health-course
```

---

## 4. Copy the Course Website Files

Copy all the files from the `course-website/` folder into your cloned repository:

```bash
# Copy all course files into the repo
cp -r "/Users/daq26/Library/CloudStorage/OneDrive-DrexelUniversity/Anthropic/AI for UH Course/course-website/"* .
```

Your repository should now contain:

```
ai-urban-health-course/
├── _quarto.yml
├── styles.css
├── index.qmd
├── day1.qmd
├── day2.qmd
├── day3.qmd
├── day4.qmd
├── day5.qmd
├── readings.qmd
├── resources.qmd
└── setup-instructions.md
```

---

## 5. Preview Locally

Run the following command from inside the repository directory:

```bash
quarto preview
```

This will:
- Render the website
- Open it in your browser at `http://localhost:####`
- Watch for changes and auto-refresh

Press `Ctrl+C` in the terminal to stop the preview.

---

## 6. Render the Website

When you are ready to build the final version:

```bash
quarto render
```

This creates a `docs/` folder containing the static HTML website. The `docs/` folder is what GitHub Pages will serve.

---

## 7. Deploy to GitHub Pages

### Initial Setup (one time)

1. Commit and push all files:

```bash
git add .
git commit -m "Initial course website"
git push origin main
```

2. Go to your repository on GitHub
3. Click **Settings** (gear icon)
4. In the left sidebar, click **Pages**
5. Under **Source**, select:
   - Branch: `main`
   - Folder: `/docs`
6. Click **Save**

Your site will be live at `https://YOUR-USERNAME.github.io/ai-urban-health-course/` within a few minutes.

---

## 8. Update Content During the Course

The typical workflow for making changes:

```bash
# 1. Edit the .qmd file(s) in your text editor or VS Code

# 2. Preview your changes
quarto preview

# 3. When satisfied, render the final version
quarto render

# 4. Commit and push
git add .
git commit -m "Updated Day 3 with additional activity"
git push origin main
```

The website will update automatically within a few minutes of pushing.

### Quick edits with Claude Code

If you have Claude Code installed, you can make updates quickly:

```bash
# Example: Add a new announcement to the home page
claude "Add a callout box at the top of index.qmd announcing that Day 2 slides are now available for download"

# Example: Fix a broken link
claude "Check all links in resources.qmd and flag any that look incorrect"

# Example: Add a reading
claude "Add this reading to the Day 3 section of readings.qmd: Smith et al. 2024, 'AI Agents in Public Health', Journal of Public Health Informatics"

# After Claude Code makes changes:
quarto render
git add .
git commit -m "Updates via Claude Code"
git push origin main
```

---

## 9. Troubleshooting

### "quarto: command not found"

Quarto is not in your PATH. Try:

```bash
# Check if it was installed
ls /usr/local/bin/quarto
ls /opt/homebrew/bin/quarto

# Or reinstall
brew reinstall quarto
```

### Render errors

If `quarto render` fails:

- Check the error message carefully --- it usually points to the exact file and line
- Common issues: unclosed code blocks (missing ```), malformed YAML front matter, broken callout syntax
- Try rendering a single file to isolate the problem: `quarto render day1.qmd`

### GitHub Pages not updating

- Make sure the `docs/` folder was committed and pushed
- Check Settings > Pages to confirm the source is set correctly
- It can take 2-5 minutes for changes to appear
- Check the **Actions** tab in your repository for build status

### CSS not loading

- Make sure `styles.css` is in the same directory as `_quarto.yml`
- Check that `_quarto.yml` references it correctly: `css: styles.css`
- Try a hard refresh in your browser (Cmd+Shift+R)

### Images not showing

If you add images later:

1. Create an `images/` folder in the repository
2. Place images there
3. Reference them in .qmd files as: `![Alt text](images/filename.png)`
4. Make sure to `git add images/` before committing

---

## 10. Optional: Custom Domain

If you want to use a custom domain (e.g., `ai-urbanhealth.drexel.edu`):

1. In your repository, go to **Settings > Pages**
2. Under **Custom domain**, enter your domain
3. Work with Drexel IT to create a CNAME record pointing to `YOUR-USERNAME.github.io`
4. Check **Enforce HTTPS**

---

## Quick Reference

| Task | Command |
|------|---------|
| Preview site locally | `quarto preview` |
| Render site | `quarto render` |
| Commit changes | `git add . && git commit -m "message"` |
| Push to GitHub | `git push origin main` |
| Check Quarto version | `quarto --version` |
| Render single file | `quarto render day1.qmd` |
