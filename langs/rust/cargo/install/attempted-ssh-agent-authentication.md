```
✗ cargo build
    Updating crates.io index
error: failed to get `async-std` as a dependency of package `app-name v0.1.0 (/Users/sathia/Developer/rust-codebase/app-name)`
Caused by:
  failed to load source for dependency `async-std`
Caused by:
  Unable to update registry `https://github.com/rust-lang/crates.io-index`
Caused by:
  failed to fetch `https://github.com/rust-lang/crates.io-index`
Caused by:
  failed to authenticate when downloading repository: git@github.com:rust-lang/crates.io-index
  * attempted ssh-agent authentication, but no usernames succeeded: `git`
  if the git CLI succeeds then `net.git-fetch-with-cli` may help here
  https://doc.rust-lang.org/cargo/reference/config.html#netgit-fetch-with-cli
Caused by:
  no authentication available
```

## Sol

ref: https://stackoverflow.com/questions/62640383/how-to-make-gitconfigs-insteadof-work-with-cargo

For bash, `export CARGO_NET_GIT_FETCH_WITH_CLI=true`.

For fish , `set -gx CARGO_NET_GIT_FETCH_WITH_CLI true`.

