FROM python:3.8.1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# 更改文件夹权限
RUN chmod -R 755 /code/app01/static/