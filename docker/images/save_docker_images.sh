#!/bin/bash

# 创建保存镜像的目录
mkdir -p images

# 导出默认服务使用的镜像
echo "正在导出默认服务的镜像..."
docker save langgenius/dify-api:1.2.0 -o images/dify-api.tar
docker save langgenius/dify-web:1.2.0 -o images/dify-web.tar
docker save postgres:15-alpine -o images/postgres.tar
docker save redis:6-alpine -o images/redis.tar
docker save langgenius/dify-sandbox:0.2.11 -o images/dify-sandbox.tar
#docker save langgenius/dify-plugin-daemon:0.0.6-local -o images/dify-plugin-daemon.tar
docker save ubuntu/squid:latest -o images/squid.tar
docker save nginx:latest -o images/nginx.tar
docker save semitechnologies/weaviate:1.19.0 -o images/weaviate.tar

echo "默认镜像导出完成！"

# 根据VECTOR_STORE的值导出对应的向量数据库镜像
echo "请输入您在.env中配置的VECTOR_STORE值（默认为weaviate）:"
read vector_store

case $vector_store in
  "qdrant")
    echo "导出Qdrant镜像..."
    docker save langgenius/qdrant:v1.7.3 -o images/qdrant.tar
    ;;
  "pgvector")
    echo "导出PGVector镜像..."
    docker save pgvector/pgvector:pg16 -o images/pgvector.tar
    ;;
  "milvus")
    echo "导出Milvus相关镜像..."
    docker save quay.io/coreos/etcd:v3.5.5 -o images/etcd.tar
    docker save minio/minio:RELEASE.2023-03-20T20-16-18Z -o images/minio.tar
    docker save milvusdb/milvus:v2.5.0-beta -o images/milvus.tar
    ;;
  "myscale")
    echo "导出MyScale镜像..."
    docker save myscale/myscaledb:1.6.4 -o images/myscale.tar
    ;;
  "elasticsearch")
    echo "导出Elasticsearch镜像..."
    docker save docker.elastic.co/elasticsearch/elasticsearch:8.14.3 -o images/elasticsearch.tar
    docker save docker.elastic.co/kibana/kibana:8.14.3 -o images/kibana.tar
    ;;
  *)
    echo "使用默认的Weaviate，已经导出"
    ;;
esac

echo "镜像导出完成！所有镜像文件保存在images目录中。"