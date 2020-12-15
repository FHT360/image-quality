FROM registry.cn-beijing.aliyuncs.com/aliyunfc/runtime-python3.6:build-1.9.9
RUN fun-install pip install flask
RUN fun-install pip install requests
RUN fun-install pip install image-quality