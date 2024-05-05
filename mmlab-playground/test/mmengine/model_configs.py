model_configs = {
    "solov2": {
        "config_path": "../configs/solov2_r50_fpn_1x_coco.py",
        "dataset": "coco",
        "checkpoint_path": None,
    },
    "yolov3": {
        "config_path": "../configs/yolov3_d53_320_273e_coco.py",
        "dataset": "coco",
        "checkpoint_path": "../configs/yolov3_d53_320_273e_coco-421362b6.pth",
    },
    "boxinst": {
        "config_path": "../configs/boxinst_r50_fpn_ms-90k_coco.py",
        "dataset": "coco",
        "checkpoint_path": "../configs/boxinst_r50_fpn_ms-90k_coco_20221228_163052-6add751a.pth",
    },
    "fcn": {
        "config_path": "../configs/fcn_r18-d8_4xb2-80k_cityscapes-512x1024.py",
        "dataset": "cityscapes",
        "checkpoint_path": "../configs/fcn_r18-d8_512x1024_80k_cityscapes_20201225_021327-6c50f8b4.pth",
    },
    "pointrend": {
        "config_path": "../configs/pointrend_r50_4xb2-80k_cityscapes-512x1024.py",
        "dataset": "cityscapes",
        "checkpoint_path": "../configs/pointrend_r50_512x1024_80k_cityscapes_20200711_015821-bb1ff523.pth",
    },
    "rtmdet": {
        "config_path": "../configs/rtmdet_tiny_8xb32-300e_coco.py",
        "dataset": "coco",
        "checkpoint_path": None,
    },
}
