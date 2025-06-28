---
date: 2024-03-21
os: macos 13.4 M1
---

ref (_unreliable_): https://stackoverflow.com/questions/15450091/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-tmp-mys

+ Download dmg from official. Something like https://cdn.mysql.com//Downloads/MySQL-8.3/mysql-8.3.0-macos14-arm64.dmg .
+ Run the dmg. You will have cli tools then, now you have:

```
~ λ mysql --version
mysql  Ver 8.3.0 for macos13.6 on arm64 (Homebrew)
```

+ `brew services start mysql` or something else to start mysql service.

```
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)
```

+ `mysql_secure_installation`

+ Next, see the following history:

```
~ λ sudo mysql
Password:
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
~ λ sudo chown -R _mysql:mysql /usr/local/var/mysql

chown: /usr/local/var/mysql: No such file or directory
~ λ sudo mysql.server start

Starting MySQL
. ERROR! The server quit without updating PID file (/opt/homebrew/var/mysql/floriandeMacBook-Air.local.pid).
~ λ mysql -u root -p h127.0.0.1

Enter password:
ERROR 1049 (42000): Unknown database 'h127.0.0.1'
~ λ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
Server version: 8.3.0 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE USER 'julyfun'@'localhost' IDENTIFIED BY 'guest123';
Query OK, 0 rows affected (0.03 sec)
```

+ You can now install, in vscode, the MySql extension by Wejian Chen.

## Better not

+ brew install mysql / mariadb


