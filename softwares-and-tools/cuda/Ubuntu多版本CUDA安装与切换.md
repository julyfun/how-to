---
title: Ubuntu多版本CUDA安装与切换
date: 2025-03-12 02:39:15
tags: ["softwares-and-tools", "cuda"]
---

- this article is for backpack
发表于2022-01-04|更新于2022-06-07|[教程](https://qiyuan-z.github.io/categories/%E6%95%99%E7%A8%8B/)

|字数总计:521|阅读时长:2分钟|阅读量:15646

本文主要介绍CUDA多版本如何共存与切换，这里以cuda10.1为例。

## [](https://qiyuan-z.github.io/2022/01/04/Ubuntu%E5%A4%9A%E7%89%88%E6%9C%ACcuda%E5%AE%89%E8%A3%85%E4%B8%8E%E5%88%87%E6%8D%A2/#%E5%AE%89%E8%A3%85%E6%96%B0%E7%89%88%E6%9C%ACcuda "安装新版本cuda")安装新版本cuda

去[官网](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10)选择对应安装包，这里选择runfile类型的安装文件`cuda_10.1.243_418.87.00_linux.run`。

执行以下命令，开始安装：  

plaintext

|   |   |
|---|---|
|1|sudo sh cuda_10.1.243_418.87.00_linux.run|

依次出现如下界面：

选择continue，继续。

输入accept，回车接受。

- 是否安装显卡驱动，本机已有，这里一般取消勾选
- 是否安装工具包，默认勾选
- 是否安装样例， 默认勾选
- 是否安装演示套件，默认勾选
- 是否安装文档，默认勾选

勾选完毕，点击install开始安装。

过程中会叫你选择是否创建指向cuda的链接：

plaintext

|   |   |
|---|---|
|1  <br>2|Do you want to install a symbolic link at /usr/local/cuda?  <br>(y)es/(n)o/(q)uit:|

如果马上想要使用当前版本，这里就选yes，否则就选no，等有需要时再设置。

## [](https://qiyuan-z.github.io/2022/01/04/Ubuntu%E5%A4%9A%E7%89%88%E6%9C%ACcuda%E5%AE%89%E8%A3%85%E4%B8%8E%E5%88%87%E6%8D%A2/#%E5%AE%89%E8%A3%85cuDNN "安装cuDNN")安装cuDNN

同样去[官网](https://developer.nvidia.com/rdp/cudnn-archive)下载好与CUDA版本对应的安装包，文件格式为tar压缩文件`cudnn-10.1-linux-x64-v7.6.4.38.tgz`。

① 进行解压

plaintext

|   |   |
|---|---|
|1|tar -zxvf cudnn-10.1-linux-x64-v7.6.4.38.tgz|

② 将解压后的文件复制到新版本cuda目录

plaintext

|   |   |
|---|---|
|1  <br>2|sudo cp cuda/include/cudnn.h  /usr/local/cuda-10.1/include  <br>sudo cp cuda/lib64/libcudnn*  /usr/local/cuda-10.1/lib64|

③ 更改权限

plaintext

|   |   |
|---|---|
|1|sudo chmod a+r /usr/local/cuda-10.1/include/cudnn.h  /usr/local/cuda-10.1/lib64/libcudnn*|

## [](https://qiyuan-z.github.io/2022/01/04/Ubuntu%E5%A4%9A%E7%89%88%E6%9C%ACcuda%E5%AE%89%E8%A3%85%E4%B8%8E%E5%88%87%E6%8D%A2/#%E9%85%8D%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F "配置环境变量")配置环境变量

修改 ~/.bashrc 文件，在末尾添加：

plaintext

|   |   |
|---|---|
|1  <br>2  <br>3|export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64  <br>export PATH=$PATH:/usr/local/cuda/bin  <br>export CUDA_HOME=$CUDA_HOME:/usr/local/cuda|

按此设置后，以后更换CUDA版本无需再动环境配置。

## [](https://qiyuan-z.github.io/2022/01/04/Ubuntu%E5%A4%9A%E7%89%88%E6%9C%ACcuda%E5%AE%89%E8%A3%85%E4%B8%8E%E5%88%87%E6%8D%A2/#%E5%A4%9A%E7%89%88%E6%9C%AC%E5%88%87%E6%8D%A2 "多版本切换")多版本切换

CUDA默认安装在`/usr/local`下，可至此目录查看已安装版本。

使用stat命令可查看当前CUDA软链接指向哪个CUDA版本：

切换版本只需将软链接指向新的CUDA版本：

① 删除原来的链接：

plaintext

|   |   |
|---|---|
|1|sudo rm -rf /usr/local/cuda|

② 建立新链接，指向指定的CUDA版本：

plaintext

|   |   |
|---|---|
|1|sudo ln -s /usr/local/cuda-10.1 /usr/local/cuda|

切换完毕后可再次通过`stat`命令或`nvcc -V`查看：

文章作者: [Qiyuan-Z](mailto:undefined)

文章链接: [https://qiyuan-z.github.io/2022/01/04/Ubuntu%E5%A4%9A%E7%89%88%E6%9C%ACcuda%E5%AE%89%E8%A3%85%E4%B8%8E%E5%88%87%E6%8D%A2/](https://qiyuan-z.github.io/2022/01/04/Ubuntu%E5%A4%9A%E7%89%88%E6%9C%ACcuda%E5%AE%89%E8%A3%85%E4%B8%8E%E5%88%87%E6%8D%A2/)

版权声明: 本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。转载请注明来自 [Yuan](https://qiyuan-z.github.io/)！

[Ubuntu](https://qiyuan-z.github.io/tags/Ubuntu/)[CUDA](https://qiyuan-z.github.io/tags/CUDA/)[cuDNN](https://qiyuan-z.github.io/tags/cuDNN/)

