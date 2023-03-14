
<details>
<summary>Directory Structure</summary>
<div>

```
├── cfg.py
├── checkpoints
│   └── cfg
│       └── checkpoint.pth.tar
├── data
│   ├── TestData
│   │   ├── image
│   │   └── txt
│   └── TrainingData
│       ├── image
│       └── txt
├── dataset
│   ├── builder.py
│   ├── __init__.py
│   ├── pan_pp_test.py
│   └── pan_pp_train.py
├── models
│   ├── backbone
│   │   ├── builder.py
│   │   ├── __init__.py
│   │   └── resnet.py
│   ├── builder.py
│   ├── head
│   │   ├── builder.py
│   │   ├── __init__.py
│   │   └── pan_pp_det_head.py
│   ├── __init__.py
│   ├── loss
│   │   ├── acc.py
│   │   ├── builder.py
│   │   ├── dice_loss.py
│   │   ├── emb_loss_v1.py
│   │   ├── emb_loss_v2.py
│   │   ├── __init__.py
│   │   ├── iou.py
│   │   └── ohem.py
│   ├── neck
│   │   ├── builder.py
│   │   ├── fpem_v2.py
│   │   └── __init__.py
│   ├── pan_pp.py
│   └── utils
│       ├── conv_bn_relu.py
│       ├── coordconv.py
│       ├── fuse_conv_bn.py
│       └── __init__.py
├── README.md
├── requirement.txt
├── main.ipynb
├── test.py
├── test.sh
├── train.py
├── train.sh
└── utils
    ├── average_meter.py
    ├── corrector.py
    ├── __init__.py
    ├── logger.py
    ├── result_format.py
    └── visualizer.py
```
</div>
</details>

## Init

```shell
~/Google Drive/내 드라이브$ git clone https://github.com/Team-BoonMoSa/PANPP
```

`~/Google Drive/내 드라이브/PANPP/data`에 `FlickrLogos-v2` 업로드

---

## Train

```shell
!sh train.sh
```

### Prepare Training Data

> [./dataset/pan_pp_train.py](https://github.com/Team-BoonMoSa/PANPP/blob/main/dataset/pan_pp_train.py)

```python
tt_root_dir = './data/TrainingData/'
tt_train_data_dir = tt_root_dir + 'image/'
tt_train_gt_dir = tt_root_dir + 'txt/'
```

### Fine-Tuning

> [./cfg.py](https://github.com/Team-BoonMoSa/PANPP/blob/main/cfg.py)

```python
train_cfg = dict(
    ...
    # pretrain='',
)
```

## Test

```shell
!sh test.sh
```

### Prepare Test Data

> [./cfg.py](https://github.com/Team-BoonMoSa/PANPP/blob/main/cfg.py)

```python
data = dict(
    ...
    test=dict(
        ...
        data='data/TestData/image/'
    )
)
```

### Prepare Weights of Pretrained PAN++

> [./cfg.py](https://github.com/Team-BoonMoSa/PANPP/blob/main/cfg.py)

```python
test_cfg = dict(
    ...
    pretrain='./checkpoints/cfg/checkpoint.pth.tar', # tmp
)
```

---

> Reference
+ [PAN++: Towards Efficient and Accurate End-to-End Spotting of Arbitrarily-Shaped Text](https://arxiv.org/abs/2105.00405)
+ [pan_pp.pytorch](https://github.com/whai362/pan_pp.pytorch)
