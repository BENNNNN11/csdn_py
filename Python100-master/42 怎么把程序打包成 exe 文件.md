# Python100



## 怎么把程序打包成 exe 文件

用 Setuptools 里的 py2exe 库

## 怎么把程序打包成 Mac 系统可运行的 .app 文件

- 安装py2app

```
pip3 install py2app
```

- cd 到Demo.py文件所在的目录

- py2applet --make-setup Demo.py
完成显示生成setup.py