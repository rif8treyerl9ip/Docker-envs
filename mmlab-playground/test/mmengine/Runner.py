from mmengine.runner import Runner
from mmengine.config import Config

# !mim download mmdet --config rtmdet_tiny_8xb32-300e_coco --dest .

cfg = Config.fromfile('../all_cfg/rtmdet_tiny_8xb32-300e_coco.py')
cfg.work_dir = './work_dir'

def change_cfg():
    cfg.data_root = '/workspace/coco2017/coco'

    cfg.train_dataloader.dataset.data_root = cfg.data_root
    cfg.val_dataloader.dataset.data_root = cfg.data_root
    cfg.test_dataloader.dataset.data_root = cfg.data_root

    cfg.val_dataloader.dataset.ann_file = cfg.data_root + '/annotations/instances_val2017.json'
    cfg.val_evaluator.ann_file = cfg.data_root + '/annotations/instances_val2017.json'
    cfg.test_dataloader.dataset.ann_file = cfg.data_root + '/annotations/instances_val2017.json'
    cfg.test_evaluator.ann_file = cfg.data_root + '/annotations/instances_val2017.json'

    print("cfg.data_root:{cfg.data_root}")
    print("cfg.train_dataloader.dataset.data_root:{cfg.train_dataloader.dataset.data_root}")
    print("cfg.val_dataloader.dataset.data_root:{cfg.val_dataloader.dataset.data_root}")
    print("cfg.test_dataloader.dataset.data_root:{cfg.test_dataloader.dataset.data_root}")
    print("cfg.val_dataloader.dataset.ann_file:{cfg.val_dataloader.dataset.ann_file}")
    print("cfg.val_evaluator.ann_file:{cfg.val_evaluator.ann_file}")
    print("cfg.test_dataloader.dataset.ann_file:{cfg.test_dataloader.dataset.ann_file}")
    print("cfg.test_evaluator.ann_file:{cfg.test_evaluator.ann_file}")

change_cfg()

runner = Runner.from_cfg(cfg)
# # runner.train()
runner.test()
