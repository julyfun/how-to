- reliability: "20% (author)"
- date: 2025-03-24
- os: "Linux DESKTOP-VDB57PP 5.15.153.1-microsoft-standard-WSL2+ #2 SMP Sun Oct 27 22:02:06 CST 2024 x86_64 x86_64 x86_64 GNU/Linux"
- author: "deepseek V3"
- assume-you-know: [computer]

# Copy all upstream branches after forking only main branch

If you've forked a Git repository but only have the `main` (or `master`) branch locally, you can fetch and track **other remote branches** from the original repository (upstream) into your fork. Here's how:

---

### **Step 1: Add the Original Repository as `upstream`**
If you haven't already, add the original repo as a remote named `upstream`:
```bash
git remote add upstream https://github.com/original-owner/original-repo.git
```

Verify remotes:
```bash
git remote -v
# Should show:
# origin    https://github.com/your-username/forked-repo.git (fetch/push)
# upstream  https://github.com/original-owner/original-repo.git (fetch)
```

---

### **Step 2: Fetch All Branches from Upstream**
Fetch all branches and their commits from the original repository:
```bash
git fetch upstream
```

This downloads all branches (e.g., `feature`, `dev`, etc.) but doesn’t create local copies yet.

---

### **Step 3: List Available Remote Branches**
Check which branches exist upstream:
```bash
git branch -r  # Shows remote branches (upstream/*)
```

Example output:
```
upstream/main
upstream/feature-x
upstream/dev
```

---

### **Step 4: Create Local Branches Tracking Upstream**
For each branch you want to copy (e.g., `feature-x`), create a local branch that tracks the upstream version:
```bash
git checkout -b feature-x upstream/feature-x
```
This:
1. Creates a local branch `feature-x`.
2. Sets it to track `upstream/feature-x`.
3. Switches you to the new branch.

Repeat for other branches you need.

---

### **Step 5: Push Branches to Your Fork (Optional)**
To make these branches available in **your fork** (on GitHub/GitLab), push them to `origin`:
```bash
git push origin feature-x
```

Now they’ll appear in your fork’s remote repository.

---

### **Alternative: One-Liner to Copy All Branches**
To copy *all* upstream branches to local and push them to your fork:
```bash
git fetch upstream
for branch in $(git branch -r | grep -vE "HEAD|main"); do
  git checkout -b ${branch#upstream/} $branch
  git push origin ${branch#upstream/}
done
```
This script:
1. Fetches all upstream branches.
2. Loops through each (excluding `HEAD` and `main`).
3. Creates local branches and pushes them to your fork.

---

### **Key Notes**
- **Tracking Branches**: Local branches will track `upstream` (original repo). To track your fork instead:
  ```bash
  git branch -u origin/feature-x feature-x
  ```
- **Avoid Conflicts**: If branches already exist locally, use `git checkout -B` to reset them.
- **Permissions**: Ensure you have push access to your fork (`origin`).

Let me know if you need help with a specific branch or error!

