import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pycocotools import mask as mask_utils

"""
mmdet/evaluation/metrics/coco_metric.pyから作成されたresults.segm.jsonを読み込み、
指定されたJSONファイルからセグメンテーションデータを読み込み、指定された画像IDに対応する画像にセグメンテーションマスクを適用する。
coco_metric.pyから作成されたresults.segm.jsonに対してのみ動作確認済み
"""

# with open("results.segm.json") as f:
with open("results.segm_pth.json") as f:
    segmentation_data = json.load(f)

image = cv2.imread("/workspace/ML_data/coco2017/coco/val2017/000000397133.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 指定したimage_idのみを抽出
# target_image_id = 174482
target_image_id = 397133
filtered_data = [obj for obj in segmentation_data if obj["image_id"] == target_image_id]

print(len(filtered_data))

# セグメンテーション結果を描画
i=0
for obj in filtered_data:
    bbox = obj["bbox"]
    score = obj["score"]
    segmentation = obj["segmentation"]

    if score > 0.5:
        # write boundingbox
        x, y, w, h = map(int, bbox)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        decoded_mask = mask_utils.decode(segmentation)
        color_mask = np.random.randint(0, 255, (1, 3), dtype=np.uint8)
        for c in range(3):
            image[:, :, c] = np.where(decoded_mask == 1,
                                      image[:, :, c] * 0.5 + color_mask[0, c] * 0.5,
                                      image[:, :, c])
    i+=1

plt.imshow(image)
plt.axis("off")
plt.savefig(f"{i}_segmentation_result.png", bbox_inches="tight", pad_inches=0)
