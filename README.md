## 服务器的监控脚本，监控服务器的内存、网络等情况 

大概实现的方法有两种：

1. 调取linux系统下的shell，通过系统API 获取当前系统的各项指标。

2. Linux 系统下有一个/proc的目录，/proc目录是一种文件系统，即proc文件系统。/proc是一种伪文件系统（也即虚拟文件系统），存储的是当前内核运行状态的一系列特殊文件，用户可以通过这些文件查看有关系统硬件及当前正在运行进程的信息，甚至可以通过更改其中某些文件来改变内核的运行状态。

相比之下，通过shell去获取系统信息无疑是多了一步操作了，进程少的时候体现不出来，但一旦进程达到一定数量，就会大量减慢读取速度（尽管这是一个小玩意，考虑考虑也是没有问题的…）

对于一个对前端毫无兴趣的后端人士而言，web界面我默默地扒了别人的用（文末会贴出地址）手动滑稽

**环境说明：**



> Server：win10 PyCharm 

> Client：Ubuntu 16.0

Python标本均为3.6。由于2和3的版本之间有一些兼容性的问题，推荐使用python3，并保持server和client端的python版本一致。注意Ubuntu默认的phthon版本为2.7。

记得在Client.py里面手动配置一下Server的ip，User和Password 随你开心。后面有空可能会写一下shell脚本自动配置。 

就酱。

![image](https://wx3.sinaimg.cn/mw1024/95dda403ly1fnvnvyej49j20z1050my5.jpg)

部分参考：
https://github.com/tenyue/ServerStatus

