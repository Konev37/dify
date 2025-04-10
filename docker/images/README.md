## 插件迁移

1. 使用 docker commit 保存容器为新镜像：

    ```bash
    docker commit dify-plugin-daemon-container fs-tele/dify-plugin-daemon:0.0.6-local
    ```

2. 使用 docker save 保存新镜像为 tar 文件：

    ```bash
    docker save fs-tele/dify-plugin-daemon:0.0.6-local > fs-tele-dify-plugin-daemon-0.0.6-local.tar
    ```

3. 在其他机器上使用 docker load 加载镜像：

    ```bash
    docker load < fs-tele-dify-plugin-daemon-0.0.6-local.tar
    ```

4. 修改 docker-compose.yml 文件中的镜像名称：

    ```yaml
    image: fs-tele/dify-plugin-daemon:0.0.6-local
    ```