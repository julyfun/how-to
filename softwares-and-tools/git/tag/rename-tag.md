---
title: rename-tag
date: 2024-04-20 22:18:03
tags: []
---
ref: https://stackoverflow.com/questions/1028649/how-do-you-rename-a-git-tag

```
git tag new old           # Create a new local tag named `new` from tag `old`.
git tag -d old            # Delete local tag `old`.
git push origin new :old  # Push `new` to your remote named "origin", and delete
                          #     tag `old` on origin (by pushing an empty tag
                          #     name to it).
```

## for co-workers

```
git fetch --prune --prune-tags
```

