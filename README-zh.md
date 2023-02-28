# 快速清理Dynadot迁移至Cloudflare时产生的无效域名
[简体中文](README-zh.md) | [English](README.md)

在Dynadot购买新域名后，迁移至Cloudflare时，偶尔会发生扫出来大量无效域名的情况。

但是Cloudflare不支持批量删除，只能通过api来操作。

## 警告

**请不要在旧的域名上执行，否则会清除已有设置。**

## 如何使用
安装依赖
```shell
pip install cloudflare
```

编辑`main.py`

修改`email`，`key`和`domain`为实际的内容后保存。

运行
```shell
python main.py
```

## 已知问题
如果无效域名过多，脚本可能会在运行中崩溃。

无所谓！再跑一次就行了！