FROM ubuntu:22.04

# 设置环境变量，避免 apt install 时弹出交互式确认
ENV DEBIAN_FRONTEND=noninteractive 

RUN apt update && apt install -y python3 curl

CMD ["python3", "-c", "print('hello robot')"]
