import torch
from torchsummary import summary

from mmdeploy.apis.utils import build_task_processor
from mmdeploy.utils import get_input_shape, load_config

"""
visualize .pth structure.

"""

device = "cpu"

model_cfg = "../configs/solov2_r50_fpn_1x_coco.py"
backend_model = "../configs/solov2_r50_fpn_1x_coco_20220512_125858-a357fa23.pth"
image = "../../mmdeploy/demo/resources/det.jpg"
deploy_cfg = "../../mmdeploy/configs/mmdet/detection/detection_torchscript.py"

deploy_cfg, model_cfg = load_config(deploy_cfg, model_cfg)

task_processor = build_task_processor(model_cfg, deploy_cfg, device)
model = task_processor.build_pytorch_model(backend_model)

# 入力形状の取得とモデルへの適用
# input_shape = get_input_shape(deploy_cfg)
# model_inputs, _ = task_processor.create_input(image, input_shape)
# print(f"input_shape: {input_shape}")
# print(model_inputs["inputs"][0].shape)

model.to("cuda")

from torchinfo import summary

summary(
    model,
    input_size=(1, 3, 800, 1344),
    col_names=["input_size", "output_size", "num_params"],
)
