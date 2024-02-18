## &

cmd &

## Screen

```
sudo apt install screen
screen -xRR
# （上面的意思是：如果后台有一个现有的screen，则连上去，否则创建一个新的。）
```

退出 screen: 

```
Ctrl-A, d
# （上面的意思是：按Ctrl-A，抬手，然后按 d 键。功能是：退出screen并将当前screen放到后台。）
```

进阶的使用大致需要掌握 Ctrl-A, a （创建新标签），Ctrl-A, 数字（切换到指定标签）以及screenrc的撰写（设计标签栏的显示样式）这三项也就能满足基本使用，这是在一个screen内部使用多标签页的办法。

ref: https://www.zhihu.com/question/442188249/answer/1710936130 by pansz

