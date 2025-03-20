searxng安装命令
```
cd dify

[//]: # (docker run --name searxng-latest -d -p 8082:8080 -v "/root/dify/dify-latest/api/core/tools/provider/builtin/searxng/docker:/etc/searxng" searxng/searxng)
docker run --name searxng-latest -d -p 8082:8080 -v "${PWD}/api/core/tools/builtin_tool/providers/searxng/docker:/etc/searxng" searxng/searxng
```

如果安装时提示没权限：
进到settings.yml
把原来对应部分代码改为：
```
formats:
    - html
    - json
```