# Train

```shell
!sh train.sh
```

## Prepare Training Data

> [./dataset/pan_pp_train.py](https://github.com/Team-BoonMoSa/PANPP/blob/main/dataset/pan_pp_train.py)

```python
tt_root_dir = './data/TrainingData/'
tt_train_data_dir = tt_root_dir + 'image/'
tt_train_gt_dir = tt_root_dir + 'txt/'
```

## Fine-Tuning

> [./cfg.py](https://github.com/Team-BoonMoSa/PANPP/blob/main/cfg.py)

```python
train_cfg = dict(
    ...
    # pretrain='',
)
```

---

# Test

```shell
!sh test.sh
```

## Prepare Test Data

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

## Prepare Weights of Pretrained PAN++

> [./cfg.py](https://github.com/Team-BoonMoSa/PANPP/blob/main/cfg.py)

```python
test_cfg = dict(
    ...
    pretrain='./checkpoints/cfg/checkpoint.pth.tar', # tmp
)
```

---

> Reference

[PAN++: Towards Efficient and Accurate End-to-End Spotting of Arbitrarily-Shaped Text](https://arxiv.org/abs/2105.00405)
