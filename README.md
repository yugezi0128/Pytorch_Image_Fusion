# Pytorch_Image_Fusion  
&emsp;&emsp;基于Pytorch框架的多源图像像素级融合，包含针对多种网络的复现。  
&emsp;&emsp;The pixel level fusion of multi-source images based on the pytorch framework includes the reproduction of multiple networks.  
## 环境要求 / Environmental Requirements  
&emsp;&emsp;Python 3.7  
&emsp;&emsp;Pytorch 1.6  

## 代码结构 / Code Structure  
  .  
├── [config]  
│   └── VIF_Net.yaml  
├── core  
│   ├── dataset  
│   │   ├── crop_datasets.py  
│   │   ├── fusion_datasets.py  
│   │   └── __init__.py  
│   ├── loss  
│   │   ├── dist_loss.py  
│   │   ├── __init__.py  
│   │   ├── ssim_loss.py  
│   │   ├── tv_loss.py  
│   │   └── vif_ssim_loss.py  
│   ├── model  
│   │   ├── __init__.py  
│   │   ├── model.py  
│   │   └── VIF_Net.py  
│   └── util  
│       ├── __init__.py  
│       └── utils.py  
├── datasets  
│   ├── TNO  
│   │   ├── Inf  
│   │   └── Vis  
│   └── TNO_crop  
│       ├── Inf  
│       └── Vis  
├── img  
├── run.py  
├── test  
├── tools  
│   ├── __init__.py  
│   ├── test.py  
│   └── train.py  
└── work_dirs  
    └── VIF_Net_Image_Fusion  
        ├── events.out.tfevents.1610973669.ymhj-Z10PA-U8-Series  
        └── model_1.pth  

## 参数设置 / Parameter Setting  
  
## 训练与测试 / Training And Testing  
  
## 计划中 / To Do  
 - [x] VIF_Net 👉 https://blog.csdn.net/qq_36449741/article/details/104562999  
 - [ ] DenseFuse 👉 https://blog.csdn.net/qq_36449741/article/details/104776319  
