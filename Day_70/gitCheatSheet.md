# Git Cheatsheet

## Basic Commands

### Initialize a Repository
```bash
git init
```

### Clone a Repository
```bash
git clone <repository_url>
```

### Check Repository Status
```bash
git status
```

### Add Changes to Staging
```bash
git add <file>
git add . # Add all changes
```

### Commit Changes
```bash
git commit -m "Your commit message"
```

### View Commit History
```bash
git log
```

## Branching and Merging

### Create a New Branch
```bash
git branch <branch_name>
```

### Switch to a Branch
```bash
git checkout <branch_name>
```

### Create and Switch to a Branch
```bash
git checkout -b <branch_name>
```

### Merge a Branch
```bash
git merge <branch_name>
```

### Delete a Branch
```bash
git branch -d <branch_name>
```

### List Branches
```bash
git branch
```

## Remote Repositories

### Add a Remote Repository
```bash
git remote add origin <repository_url>
```

### View Remote Repositories
```bash
git remote -v
```

### Push Changes
```bash
git push origin <branch_name>
```

### Pull Changes
```bash
git pull origin <branch_name>
```

### Push with Upstream
```bash
git push -u origin <branch_name>
```

## Undoing Changes

### Unstage Changes
```bash
git reset <file>
```

### Undo Last Commit (Keep Changes)
```bash
git reset --soft HEAD~1
```

### Undo Last Commit (Discard Changes)
```bash
git reset --hard HEAD~1
```

### Discard Changes in a File
```bash
git checkout -- <file>
```

## Advanced Commands

### Rebase
```bash
git rebase <branch_name>
```

### Stash Changes
```bash
git stash
```

### Apply Stashed Changes
```bash
git stash apply
```

### List Stashes
```bash
git stash list
```

### Tagging
```bash
git tag <tag_name>
git push origin <tag_name>
```

## Collaboration

### Resolve Merge Conflicts
1. Open conflicted files and edit manually.
2. Stage resolved files:
   ```bash
   git add <file>
   ```
3. Continue the merge or rebase:
   ```bash
   git merge --continue
   git rebase --continue
   ```

### Fetch Changes
```bash
git fetch origin
```

### Revert a Commit
```bash
git revert <commit_hash>
```

## SSH Setup

### Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Add SSH Key to Agent
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### Test SSH Connection
```bash
ssh -T git@github.com
