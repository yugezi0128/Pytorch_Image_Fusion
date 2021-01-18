# Pytorch_Image_Fusion  
&emsp;&emsp;基于Pytorch框架的多源图像像素级融合，包含针对多种网络的复现。  
&emsp;&emsp;The pixel level fusion of multi-source images based on the pytorch framework includes the reproduction of multiple networks.  
## 环境要求 / Environmental Requirements  
&emsp;&emsp;Python 3.7  
&emsp;&emsp;Pytorch 1.6  

## 参数设置 / Parameter Setting  
  
```python
# ./config/VIF_Net.yaml

PROJECT: # 项目参数
  name: 'VIF_Net_Image_Fusion' # 项目名称
  save_path: './work_dirs/' # 项目保存路径，训练模型会保存至此路径下的项目名称文件夹中、

TRAIN_DATASET: # 训练数据集参数
  root_dir: './datasets/TNO_crop/' # 训练数据集根目录
  sensors: [ 'Vis', 'Inf' ] # 训练数据集包含的数据类型
  channels: 1 # 训练数据中图片的通道数
  input_size: 128 # 训练数据中图片的尺寸
  mean: [ 0.485, 0.456, 0.406 ] # 训练数据中图片的归一化均值（暂时用不到）
  std: [ 0.229, 0.224, 0.225 ] # 训练数据中图片的归一化标准差（暂时用不到）

TRAIN: # 训练参数
  batch_size: 32 # 训练批次大小
  max_epoch: 200 # 训练最大代数
  lr: 0.01 # 训练学习率
  gamma: 0.01 # 训练学习率衰减系数
  milestones: [ 100, 150, 175 ] # 训练学习率衰减的里程碑
  opt: Adam # 训练优化器
  val_interval: 1 # 训练每过多少代数后保存权重
  debug_interval: 100 # 训练每过多少批次后进行可视化，结果可视化在tensorboard中
  resume: None # 训练停止后继续训练加载权重路径
  loss_weights: [ 1000, 1 ] # 对VIF_Net的两个损失的权值

TEST_DATASET: # 测试数据集参数
  root_dir: './datasets/TNO/' # 测试数据集根目录
  sensors: [ 'Vis', 'Inf' ] # 测试数据集包含的数据类型
  channels: 1 # 测试数据中图片的通道数
  input_size: 512 # 测试数据中图片的尺寸
  mean: [ 0.485, 0.456, 0.406 ] # 测试数据中图片的归一化均值（暂时用不到）
  std: [ 0.229, 0.224, 0.225 ] # 测试数据中图片的归一化标准差（暂时用不到）

TEST: # 测试参数
  batch_size: 2 # 测试批次大小
  weight_path: './work_dirs/VIF_Net_Image_Fusion/model_50.pth' # 测试加载的权重路径
  save_path: './test/' # 测试结果保存路径

MODEL: # 模型参数
  model_name: 'VIF_Net' # 模型名称
  input_channels: 1 # 模型输入通道数
  out_channels: 16 # 模型每一层输出的通道数
  input_sensors: [ 'Vis', 'Inf' ] # 模型输入数据类型
  coder_layers: 4 # 模型编码器层数
  decoder_layers: 4 # 模型解码器层数

```  

## 训练与测试 / Training And Testing  
  
### 训练 / Training  
&emsp;&emsp;运行  ` python run.py --train `  进行训练。训练的模型权重会保存再指定的路径下。  

#### tensorboardX进行训练可视化  
&emsp;&emsp;运行  ` tensorboard --logdir= XXX `  进行训练可视化。将  ` XXX `  替换为模型储存的路径。例如，config中有如下参数：  
```python
PROJECT:
  name: 'VIF_Net_Image_Fusion'
  save_path: './work_dirs/'
  weight_path: ''
```  
&emsp;&emsp;可运行  ` tensorboard --logdir= ./work_dirs/VIF_Net_Image_Fusion/ `  进行训练可视化。再次训练后最好删除之前的  ` events `  文件。  
### 测试 / Testing  
&emsp;&emsp;运行  ` python run.py --test `  进行测试。结果回批量保存至指定路径下。  

## 预训练模型 / Pre-training Model
 - [x] VIF_Net 👉   
 - [ ] DenseFuse 👉   
 
## 计划中 / To Do  
 - [x] VIF_Net 👉 https://blog.csdn.net/qq_36449741/article/details/104562999  
 - [ ] DenseFuse 👉 https://blog.csdn.net/qq_36449741/article/details/104776319  
