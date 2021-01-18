# Pytorch_Image_Fusion  
&emsp;&emsp;基于Pytorch框架的多源图像像素级融合，包含针对多种网络的复现。  
&emsp;&emsp;The pixel level fusion of multi-source images based on the pytorch framework includes the reproduction of multiple networks.  
## 环境要求 / Environmental Requirements  
&emsp;&emsp;Python 3.7  
&emsp;&emsp;Pytorch 1.6  

## 参数设置 / Parameter Setting  
  
## 训练与测试 / Training And Testing  
  
### 训练 / Training  
&emsp;&emsp;运行  ` python run.py --train `  进行训练。  

#### tensorboardX进行训练可视化  
&emsp;&emsp;运行  ` tensorboard --logdir= XXX `  进行训练可视化。将XXX替换为模型储存的路径，即` ./config['PROJECT']['save_path']/config['PROJECT']['name']/ `下。例如，config中有如下参数：  
`
PROJECT:
  name: 'VIF_Net_Image_Fusion'
  save_path: './work_dirs/'
  weight_path: ''
`

### 测试 / Testing  
&emsp;&emsp;运行  ` python run.py --test `  进行测试。  

## 代码结构 / Code Structure  
  
## 计划中 / To Do  
 - [x] VIF_Net 👉 https://blog.csdn.net/qq_36449741/article/details/104562999  
 - [ ] DenseFuse 👉 https://blog.csdn.net/qq_36449741/article/details/104776319  
