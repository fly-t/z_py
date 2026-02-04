# Abstract

出现该串口助手的目的是因为长时间的使用习惯是大小串口助手

但是大虾串口助手在win11上启动每次都会卡顿, 找不到原因, 于是仿照大虾串口助手的习惯

开发了小虾串口助手


- 原大虾

![](https://raw.githubusercontent.com/fly-t/images/main/blog/README-2026-02-04-12-58-30.png)

- 新小虾
  主题会根据系统颜色自动调整黑白主题



![](https://raw.githubusercontent.com/fly-t/images/main/blog/README-2026-02-04-13-09-53.png)

![](https://raw.githubusercontent.com/fly-t/images/main/blog/README-2026-02-04-13-10-28.png)



交流群:1003899431


## pack

``` c
pyside6-rcc images.qrc -o images_rc.py
Pyinstaller -F -w -i .\logo\sscom6.ico .\z_serial.py --distpath build
```


