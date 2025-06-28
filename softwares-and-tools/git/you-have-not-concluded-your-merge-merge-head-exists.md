---
title: "you-have-not-concluded-your-merge-merge-head-exists"
date: 2024-02-28 20:09:57
tags: []
---
ref: https://stackoverflow.com/questions/11646107/you-have-not-concluded-your-merge-merge-head-exists

The problem is your previous pull failed to merge automatically and went to conflict state. And the conflict wasn't resolved properly before the next pull.

Undo the merge and pull again.

To undo a merge:

git merge --abort [Since git version 1.7.4]

git reset --merge [prior git versions]

Resolve the conflict.

Don't forget to add and commit the merge.

git pull now should work fine.


