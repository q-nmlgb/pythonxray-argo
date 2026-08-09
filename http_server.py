import modal

app = modal.App("simple")

image = modal.Image.from_dockerfile("Dockerfile").add_local_file("D:/work/123/app.py", remote_path="/root/app.py")

@app.function(
    image=image,
    max_containers=1,       # 限制全球最多只拉起 1 个容器实例
    scaledown_window=300,   # 闲置 300 秒无请求自动休眠
    timeout=86400,
)
@modal.web_server(port=8001, startup_timeout=60)
def run_server():
    import subprocess
    # 使用 Popen 后台非阻塞启动 Python 简易 HTTP 服务器

    subprocess.Popen(["python", "/root/app.py"])
