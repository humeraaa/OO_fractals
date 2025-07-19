
---

### ✅ To commit & upload this `README.md` to GitHub:

1. **Save it** in your local `chat_application` folder.
2. Then **run this mini `.bat` script** (`push_readme.bat`) to push the change:

```bat
@echo off
SETLOCAL

echo Adding updated README.md to Git...
git add README.md

echo Committing...
git commit -m "Updated README with student and setup guide"

echo Pushing to GitHub...
git push origin main

echo ✅ README pushed successfully.
pause
