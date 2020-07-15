# 基于的基础镜像
FROM python:3.6.9

# 维护者信息

MAINTAINER LHM  lhm@ikahe.com

# 代码添加到code文件夹

ADD ./TCP /code

# 设置code文件夹是工作目录

WORKDIR /code

# 安装支持

RUN pip install -r requirements.txt

CMD ["python", "/code/server.py"]