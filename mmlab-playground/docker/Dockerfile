ARG PYTORCH="2.2.2"
ARG CUDA="11.8"
ARG CUDNN="8"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES utility,compute

#setup environment
ENV FORCE_CUDA="1"
ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0 7.5 8.0 8.6+PTX"
ENV PATH="/usr/local/cuda/bin:$PATH"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV MMCV_WITH_OPS="1"
# ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"

RUN apt update && apt install -y \
    build-essential \
    ffmpeg \
    git \
    libgl1 \
    libglib2.0-0 \
    libturbojpeg \
    libsm6 \
    libxext6 \
    libxrender-dev \
    mesa-utils libgl1-mesa-glx \
    ninja-build \
    && apt clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 --index-url https://download.pytorch.org/whl/cu118 \
    && pip install openmim

ENV MMCV_WITH_OPS=1

RUN pip install mmengine \
    && pip install mmcv==2.0.0 -f https://download.openmmlab.com/mmcv/dist/cu118/torch2.0/index.html \
    && pip install mmdet \
    && pip install mmsegmentation \
    && pip install mmdet3d \
    && pip install mmdeploy

ENV LANG C.UTF-8
ENV LANGUAGE en_US
ENV DISPLAY host.docker.internal:0.0

WORKDIR /workspace
