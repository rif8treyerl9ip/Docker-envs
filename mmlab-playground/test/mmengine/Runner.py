from model_configs import model_configs

from mmengine.config import Config
from mmengine.runner import Runner

# !mim download mmdet --config rtmdet_tiny_8xb32-300e_coco --dest .


def change_cfg(cfg, dataset="coco"):
    cfg.work_dir = "./work_dir"

    if dataset == "coco":
        cfg.data_root = "/workspace/ML_data/coco2017/coco"
        cfg.train_dataloader.dataset.data_root = cfg.data_root
        cfg.val_dataloader.dataset.data_root = cfg.data_root
        cfg.test_dataloader.dataset.data_root = cfg.data_root
        cfg.val_dataloader.dataset.ann_file = (
            cfg.data_root + "/annotations/instances_val2017.json"
        )
        cfg.val_evaluator.ann_file = (
            cfg.data_root + "/annotations/instances_val2017.json"
        )
        cfg.test_dataloader.dataset.ann_file = (
            cfg.data_root + "/annotations/instances_val2017.json"
        )
        cfg.test_evaluator.ann_file = (
            cfg.data_root + "/annotations/instances_val2017.json"
        )
    elif dataset == "cityscapes":
        cfg.data_root = "/workspace/ML_data/cityscapes/"
        cfg.train_dataloader.dataset.data_root = cfg.data_root
        cfg.val_dataloader.dataset.data_root = cfg.data_root
        cfg.test_dataloader.dataset.data_root = cfg.data_root
        cfg.train_dataloader.dataset.data_prefix.seg_map_path = (
            "gtFine_trainvaltest/gtFine/train/"
        )
        cfg.val_dataloader.dataset.data_prefix.seg_map_path = (
            "gtFine_trainvaltest/gtFine/val/"
        )
        cfg.test_dataloader.dataset.data_prefix.seg_map_path = (
            "gtFine_trainvaltest/gtFine/val/"
        )
        cfg.train_dataloader.dataset.data_prefix.img_path = (
            "leftImg8bit_trainvaltest/leftImg8bit/train/"
        )
        cfg.val_dataloader.dataset.data_prefix.img_path = (
            "leftImg8bit_trainvaltest/leftImg8bit/val/"
        )
        cfg.test_dataloader.dataset.data_prefix.img_path = (
            "leftImg8bit_trainvaltest/leftImg8bit/val/"
        )

    # Number of samples in the dataset
    cfg.train_dataloader.dataset.indices = 100
    cfg.val_dataloader.dataset.indices = 100
    cfg.test_dataloader.dataset.indices = 100


def load_and_configure_model(model_name):

    config = model_configs.get(model_name)
    if config is None:
        raise ValueError(
            f"Model name '{model_name}' is not found in the configuration dictionary."
        )

    cfg = Config.fromfile(config["config_path"])

    if config["checkpoint_path"]:
        cfg.load_from = config["checkpoint_path"]

    change_cfg(cfg, config["dataset"])

    return cfg


def main():

    cfg = load_and_configure_model("yolov3")
    cfg.device='cpu'

    runner = Runner.from_cfg(cfg)
    # # runner.train()
    runner.test()


if __name__ == "__main__":
    main()
