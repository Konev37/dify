# 导入所有保存的镜像
for image in images/*.tar; do
  echo "正在导入 $image..."
  docker load -i $image
done