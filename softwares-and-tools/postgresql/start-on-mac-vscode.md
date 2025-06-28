---
title: start-on-mac-vscode
date: 2024-03-26 15:43:07
tags: []
---
## Install

ref: https://wiki.qiangyin.me:38080/s/12b24b4e-b01e-4a74-b318-4e97d89f415d

```
brew install postgresql@14
brew services start postgresql@14
createdb $USER
```

## Make it run

ref: https://stackoverflow.com/questions/15301826/psql-fatal-role-postgres-does-not-exist

```
For MAC:

Install Homebrew
brew install postgres
initdb /usr/local/var/postgres
/usr/local/Cellar/postgresql/<version>/bin/createuser -s postgres or /usr/local/opt/postgres/bin/createuser -s postgres which will just use the latest version.
start postgres server manually: pg_ctl -D /usr/local/var/postgres start
To start server at startup

mkdir -p ~/Library/LaunchAgents
ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
Now, it is set up, login using psql -U postgres -h localhost or use PgAdmin for GUI.

By default user postgres will not have any login password.

Check this site for more articles like this: https://medium.com/@Nithanaroy/installing-postgres-on-mac-18f017c5d3f7
```

## Vscode extension

Chris Kolkman's PostgreSQL.

