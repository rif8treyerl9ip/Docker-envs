from mmengine.runner import Runner
from mmengine.config import Config

# !mim download mmdet --config rtmdet_tiny_8xb32-300e_coco --dest .

def change_cfg(cfg, dataset='coco'):
    cfg.work_dir = './work_dir'

    if dataset=='coco':
        cfg.data_root = '/workspace/ML_data/coco2017/coco'
        cfg.train_dataloader.dataset.data_root = cfg.data_root
        cfg.val_dataloader.dataset.data_root = cfg.data_root
        cfg.test_dataloader.dataset.data_root = cfg.data_root
        cfg.val_dataloader.dataset.ann_file = cfg.data_root + '/annotations/instances_val2017.json'
        cfg.val_evaluator.ann_file = cfg.data_root + '/annotations/instances_val2017.json'
        cfg.test_dataloader.dataset.ann_file = cfg.data_root + '/annotations/instances_val2017.json'
        cfg.test_evaluator.ann_file = cfg.data_root + '/annotations/instances_val2017.json'
    elif dataset=='cityscapes':
        cfg.data_root = '/workspace/ML_data/cityscapes/'
        cfg.train_dataloader.dataset.data_root = cfg.data_root
        cfg.val_dataloader.dataset.data_root = cfg.data_root
        cfg.test_dataloader.dataset.data_root = cfg.data_root
        cfg.train_dataloader.dataset.data_prefix.seg_map_path='gtFine_trainvaltest/gtFine/train/'
        cfg.val_dataloader.dataset.data_prefix.seg_map_path='gtFine_trainvaltest/gtFine/val/'
        cfg.test_dataloader.dataset.data_prefix.seg_map_path='gtFine_trainvaltest/gtFine/val/'
        cfg.train_dataloader.dataset.data_prefix.img_path='leftImg8bit_trainvaltest/leftImg8bit/train/'
        cfg.val_dataloader.dataset.data_prefix.img_path='leftImg8bit_trainvaltest/leftImg8bit/val/'
        cfg.test_dataloader.dataset.data_prefix.img_path='leftImg8bit_trainvaltest/leftImg8bit/val/'

    # Number of samples in the dataset
    cfg.train_dataloader.dataset.indices = 100
    cfg.val_dataloader.dataset.indices = 100
    cfg.test_dataloader.dataset.indices = 100

def main():
    # mmdet ------------------------
    # rtmdet
    # cfg = Config.fromfile('../all_cfg/rtmdet_tiny_8xb32-300e_coco.py')
    # change_cfg(cfg, 'coco')

    # solov2 x memory error
    # cfg = Config.fromfile('../all_cfg/solov2_r50_fpn_1x_coco.py')
    # change_cfg(cfg, 'coco')

    # yolov3
    # cfg = Config.fromfile('../all_cfg/yolov3_d53_320_273e_coco.py')
    # load_from (str, optional): The checkpoint file to load from.Defaults to None.
    # cfg.load_from = '../all_cfg/yolov3_d53_320_273e_coco-421362b6.pth'
    # change_cfg(cfg, 'coco')

    # BoxInst o
    cfg = Config.fromfile('../all_cfg/boxinst_r50_fpn_ms-90k_coco.py')
    # load_from (str, optional): The checkpoint file to load from.Defaults to None.
    # cfg.load_from = '../all_cfg/boxinst_r50_fpn_ms-90k_coco_20221228_163052-6add751a.pth'
    change_cfg(cfg, 'coco')

    # mmseg ------------------------

    # FCN o
    # cfg = Config.fromfile('../all_cfg/fcn_r18-d8_4xb2-80k_cityscapes-512x1024.py')
    # cfg.load_from = '../all_cfg/fcn_r18-d8_512x1024_80k_cityscapes_20201225_021327-6c50f8b4.pth'
    # change_cfg(cfg, 'cityscapes')

    # pointend o
    # cfg = Config.fromfile('../all_cfg/pointrend_r50_4xb2-80k_cityscapes-512x1024.py')
    # cfg.load_from = '../all_cfg/pointrend_r50_512x1024_80k_cityscapes_20200711_015821-bb1ff523.pth'
    # change_cfg(cfg, 'cityscapes')

    runner = Runner.from_cfg(cfg)
    # # runner.train()
    runner.test()

if __name__ == '__main__':
    main()
