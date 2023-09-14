## 编译报错

```
[ 42%] Building CXX object CMakeFiles/pyflex.dir/workspace/cloth-funnels/PyFlex/core/mesh.cpp.o
make[2]: *** No rule to make target '/workspace/cloth-funnels/PyFlex/lib/linux64/NvFlexExtReleaseCUDA_x64.a', needed by 'pyflex.cpython-39-x86_64-linux-gnu.so'.  Stop.
make[2]: *** Waiting for unfinished jobs....
[ 47%] Building CXX object CMakeFiles/pyflex.dir/workspace/cloth-funnels/PyFlex/core/perlin.cpp.o
```

这是因为 Pyclex 子仓库的 lib 文件夹和 external 文件夹有丢失。

[https://github.com/columbia-ai-robotics/flingbot](https://github.com/columbia-ai-robotics/flingbot)

从上面这个链接里 Pyflex/lib 和 external 文件夹拷贝过来就可编译成功了。

编译成功日期：2023.9.14

uname 结果:

```
Linux julyfun-Lenovo-XiaoXinAir-14IIL-2020 5.19.0-46-generic #47~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Jun 21 15:35:31 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
```

显卡：MX350

git-sha: 1fb231e0633b0603eb940aec130ab903e41c2d03

