FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    python3-dev

RUN pip3 install --upgrade pip
RUN pip3 install openmim

# CPU
RUN pip3 install torch torchvision

RUN pip install mmengine==0.7.1
RUN pip install mmcv==2.0.0 -f https://download.openmmlab.com/mmcv/dist/cu118/torch2.0/index.html
RUN pip install mmdet==3.0.0

WORKDIR /workspace

CMD ["/bin/bash"]

# install latest version of mmcv-full
# RUN mim install mmcv-full
# install master branch
# RUN mim install git+https://github.com/open-mmlab/mmclassification.git
