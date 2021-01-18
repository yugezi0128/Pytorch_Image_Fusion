# Pytorch_Image_Fusion  
&emsp;&emsp;基于Pytorch框架的多源图像像素级融合，包含针对多种网络的复现。  
&emsp;&emsp;The pixel level fusion of multi-source images based on the pytorch framework includes the reproduction of multiple networks.  
## 环境要求 / Environmental Requirements  
&emsp;&emsp;Python 3.7  
&emsp;&emsp;Pytorch 1.6  

## 参数设置 / Parameter Setting  
  
```python
PROJECT: # 项目
  name: 'VIF_Net_Image_Fusion'
  save_path: './work_dirs/'
  weight_path: ''

TRAIN_DATASET:
  root_dir: './datasets/TNO_crop/'
  sensors: [ 'Vis', 'Inf' ]
  channels: 1
  input_size: 128
  mean: [ 0.485, 0.456, 0.406 ]
  std: [ 0.229, 0.224, 0.225 ]

TRAIN:
  batch_size: 32
  max_epoch: 200
  lr: 0.01
  gamma: 0.01
  milestones: [ 100, 150, 175 ]
  opt: Adam
  val_interval: 1
  debug_interval: 100
  resume: None
  loss_weights: [ 1000, 1 ]

TEST_DATASET:
  root_dir: './datasets/TNO/'
  sensors: [ 'Vis', 'Inf' ]
  channels: 1
  input_size: 512
  mean: [ 0.485, 0.456, 0.406 ]
  std: [ 0.229, 0.224, 0.225 ]

TEST:
  batch_size: 2
  weight_path: './work_dirs/VIF_Net_Image_Fusion/model_50.pth'
  save_path: './test/'

MODEL:
  model_name: 'VIF_Net'
  input_channels: 1
  out_channels: 16
  input_sensors: [ 'Vis', 'Inf' ]
  black_type: 'dense'
  coder_layers: 4
  decoder_layers: 4

```  

## 训练与测试 / Training And Testing  
  
### 训练 / Training  
&emsp;&emsp;运行  ` python run.py --train `  进行训练。训练的模型权重会保存再指定的路径下。  

#### tensorboardX进行训练可视化  
&emsp;&emsp;运行  ` tensorboard --logdir= XXX `  进行训练可视化。将  ` XXX `  替换为模型储存的路径。例如，config中有如下参数：  
```
PROJECT:
  name: 'VIF_Net_Image_Fusion'
  save_path: './work_dirs/'
  weight_path: ''
```  
&emsp;&emsp;可运行  ` tensorboard --logdir= ./work_dirs/VIF_Net_Image_Fusion/ `  进行训练可视化。再次训练后最好删除之前的  ` events `  文件。  
### 测试 / Testing  
&emsp;&emsp;运行  ` python run.py --test `  进行测试。结果回批量保存至指定路径下。  

## 代码结构 / Code Structure  
  
## 计划中 / To Do  
 - [x] VIF_Net 👉 https://blog.csdn.net/qq_36449741/article/details/104562999  
 - [ ] DenseFuse 👉 https://blog.csdn.net/qq_36449741/article/details/104776319  
