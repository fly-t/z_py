# Abstract

串口工具始终无法知道稳定性, 回环测试数据量大的时候串口助手收发显示不一致,想到了md5值可以做这个.
结合串口助手发送图片音频视频文件可以很直观知道数据是否有错误, 但是不放心还是md5更直观.

![](https://raw.githubusercontent.com/fly-t/images/main/blog/Readme-2026-08-14-08-49-26.png)


打包命令
``` c
pyinstaller --onefile --windowed --icon=md5.ico --name=MD5Tool md5_compare.py
```