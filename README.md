# 多媒体取证与安全 lsb图片信息隐藏实验

## 实验步骤

**1. 安装依赖:**

```bash
pip install -r requirements.txt
```

**2. 将隐藏图片嵌入到输入图片:**

```bash
python src/embed.py --input image/input.png --watermark image/watermark.png --output image/output.png
```

将image/watermark.png嵌入到image/input.png，生成图像保存为image/output.png

**3. 提取隐藏图片:**

```bash
python src/extract.py --input image/output.png --output image/extract.png
```

从image/output.png提取隐藏的图片，提取出的图片保存为image/extract.png

## 实验分析

### 原理
LSB 隐写术，即最低有效位（Least Significant Bit）隐写术。是一种基于二进制的隐写方式，能将一个信息隐藏进一张图片中。图像一般都是以RGB三原色的方式存储的，存储后R（红）、G（绿）、B（蓝）三组数据按顺序规律排列，每个的取值范围为0~255，范围对应的二进制值就是00000000-11111111，LSB就是把一个文件的二进制每一位拆分修改到图片的色彩数据的二进制值最低位。

### 实现思路
#### 嵌入
RGB的最高位能够基本还原原始图片的信息，因此我们把隐藏图片的RGB最高位提取出来，然后再将其放置在载体图片的RGB最低位上。由于最低位对于图片本身信息的影响很小，因此载体图片在视觉的区别微乎其微。实验的结果也印证了这一点。
#### 提取
提取隐藏图片的时候，我们将载体图片的RGB最低位提取出来，如果是1，则对应隐藏图片的RGB值设为255，如果是0，则对应隐藏图片的RGB值设为0。虽然有一定程度的信息损失，但是从结果来看，提取出来的图片基本能反映原始图片的特征。
