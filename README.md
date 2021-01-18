# Pytorch_Image_Fusion  
&emsp;&emsp;基于Pytorch框架的多源图像像素级融合，包含针对多种网络的复现。  
&emsp;&emsp;The pixel level fusion of multi-source images based on the pytorch framework includes the reproduction of multiple networks.  
## 环境要求 / Environmental Requirements  
&emsp;&emsp;Python 3.7  
&emsp;&emsp;Pytorch 1.6  

## 代码结构 / Code Structure  
  .
├── config
│   └── VIF_Net.yaml
├── core
│   ├── dataset
│   │   ├── crop_datasets.py
│   │   ├── fusion_datasets.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── loss
│   │   ├── dist_loss.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── ssim_loss.py
│   │   ├── tv_loss.py
│   │   └── vif_ssim_loss.py
│   ├── model
│   │   ├── __init__.py
│   │   ├── model.py
│   │   ├── __pycache__
│   │   └── VIF_Net.py
│   └── util
│       ├── __init__.py
│       ├── __pycache__
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
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── test.cpython-37.pyc
│   │   ├── test.cpython-38.pyc
│   │   ├── train.cpython-37.pyc
│   │   └── train.cpython-38.pyc
│   ├── test.py
│   └── train.py
└── work_dirs
    └── VIF_Net_Image_Fusion
        ├── events.out.tfevents.1610973669.ymhj-Z10PA-U8-Series
        ├── model_10.pth
        ├── model_11.pth
        ├── model_12.pth
        ├── model_13.pth
        ├── model_14.pth
        ├── model_15.pth
        ├── model_16.pth
        ├── model_17.pth
        ├── model_18.pth
        ├── model_19.pth
        ├── model_1.pth
        ├── model_20.pth
        ├── model_21.pth
        ├── model_22.pth
        ├── model_23.pth
        ├── model_24.pth
        ├── model_25.pth
        ├── model_26.pth
        ├── model_27.pth
        ├── model_28.pth
        ├── model_29.pth
        ├── model_2.pth
        ├── model_30.pth
        ├── model_31.pth
        ├── model_32.pth
        ├── model_33.pth
        ├── model_34.pth
        ├── model_35.pth
        ├── model_3.pth
        ├── model_4.pth
        ├── model_5.pth
        ├── model_6.pth
        ├── model_7.pth
        ├── model_8.pth
        └── model_9.pth

## 参数设置 / Parameter Setting  
  
## 训练与测试 / Training And Testing  
  
## 计划中 / To Do  
 - [x] VIF_Net 👉 https://blog.csdn.net/qq_36449741/article/details/104562999  
 - [ ] DenseFuse 👉 https://blog.csdn.net/qq_36449741/article/details/104776319  
