---
title: create-a-tag-in-a-github-repository
date: 2024-03-28 21:44:00
tags: ["softwares-and-tools", "git", "tag"]
---
ref: https://stackoverflow.com/questions/18216991/create-a-tag-in-a-github-repository

You can create tags for GitHub by either using:

* the Git command line, or
* GitHub's web interface.

## Creating tags from the command line

To create a tag on your current branch, run this:

    git tag <tagname>

If you want to include a description with your tag, add `-a` to create an [annotated tag][1]:

    git tag <tagname> -a

This will create a `local` tag with the current state of the branch you are on. When pushing to your remote repo, tags are NOT included by default. You will need to explicitly say that you want to push your tags to your remote repo:

    git push origin --tags

From the [official Linux Kernel Git documentation for `git push`](https://www.kernel.org/pub/software/scm/git/docs/git-push.html):

>     --tags
> All refs under refs/tags are pushed, in addition to refspecs explicitly listed on the command line.

Or if you just want to push a single tag:

    git push origin <tag>

See also my answer to https://stackoverflow.com/questions/5195859/push-a-tag-to-a-remote-repository-using-git/23217431#23217431 for more details about that syntax above.

## Creating tags through GitHub's web interface

You can find GitHub's instructions for this at their [Creating Releases help page](https://help.github.com/articles/creating-releases). Here is a summary:

1. Click the **releases** link on our repository page,
 
   ![Screenshot 1][2]

2. Click on **Create a new release** or **Draft a new release**,

   ![Screenshot 2][3]

3. Fill out the form fields, then click **Publish release** at the bottom,

   ![Screenshot 3][4]
   ![Screenshot 4][5]

4. After you create your tag on GitHub, you might want to fetch it into your local repository too:

        git fetch

Now next time, you may want to create one more tag within the same release from website. For that follow these steps:

Go to release tab

1. Click on edit button for the release

2. Provide name of the new tag ABC_DEF_V_5_3_T_2 and hit tab

3. After hitting tab, UI will show this message: Excellent! This tag will be created from the target when you publish this release. Also UI will provide an option to select the branch/commit

4. Select branch or commit

5. Check "This is a pre-release" checkbox for qa tag and uncheck it if the tag is created for Prod tag.

6. After that click on "Update Release"

7. This will create a new Tag within the existing Release.

  [1]: https://stackoverflow.com/questions/11514075/what-is-the-difference-between-an-annotated-and-unannotated-tag
  [2]: http://i.stack.imgur.com/uHyjG.png
  [3]: http://i.stack.imgur.com/MMAgk.png
  [4]: http://i.stack.imgur.com/KArgA.png
  [5]: http://i.stack.imgur.com/QzIbj.png

