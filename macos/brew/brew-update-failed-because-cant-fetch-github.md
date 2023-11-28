## reproduction

brew update, but failed to fetch https://xxx.git after 75012ms.

## solution

https://github.com/Homebrew/legacy-homebrew/issues/34363

There one says add this in your `~/.gitconfig`:

```
[url "git@github.com:"]
    insteadOf = "https://github.com/"
```

It surely works...

