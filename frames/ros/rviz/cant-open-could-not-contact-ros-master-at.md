---
rviz shows:
date: 2024-03-26 22:00:01
title: cant-open-could-not-contact-ros-master-at
tags: []
---

```
user@server:~$ rviz  
[ INFO] [1711457974.411129714]: rviz version 1.14.20
[ INFO] [1711457974.411172314]: compiled against Qt version 5.12.8
[ INFO] [1711457974.411184184]: compiled against OGRE version 1.9.0 (Ghadamon)
```

- rviz error box:

```
Could not contact ROS master at [http://localhost:11311], retrying... #37
```

- roscore shows:

```
RLException: Unable to contact my own server
```

## Sol

Your `ROS_HOSTNAME` env var is not correctly set.

ref: https://answers.ros.org/question/301509/cant-run-roscore-unable-to-contact-my-own-server/

Use output of `hostname -I` to set your `ROS_MASTER_URI` and `ROS_HOSTNAME`, like:

```
export ROS_MASTER_URI=http://10.53.21.95:11311
export ROS_HOSTNAME=10.53.21.95
```

