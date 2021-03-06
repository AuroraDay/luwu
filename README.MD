<!--
 * @Author       : AaronJny
 * @LastEditTime : 2021-02-01
 * @FilePath     : /LuWu/README.MD
 * @Desc         : 
-->
<h1 align="center">Welcome to LuWu 陆吾 👋</h1>

![](./asserts/247e8519e0b04397a74d0c49177bf001.png)

-----------

<p>
  <img alt="Python Version" src="https://img.shields.io/badge/Python-3.7-blue"></img>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.2-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/AaronJny/luwu" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/AaronJny/luwu/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/AaronJny/luwu" />
  </a>
  <a><img alt="Stars" src="https://img.shields.io/github/stars/AaronJny/luwu"></a>
</p>


### 🏠 [Homepage](https://github.com/AaronJny/luwu)


> LuWu——陆吾，一个简单的无代码深度学习平台。

写这个项目的最初动力是:
> 深度学习项目中存在大量重复而繁琐的开发工作，这些低价值的任务不应该浪费我们宝贵的时间，因而萌发了自动化的想法。
> 
> 鼠标点几下就能完成全部开发工作，它不香嘛？

这个项目的诉求是：
> - 使无深度学习相关背景的开发人员也能轻松完成深度学习任务开发
> 
> - 使深度学习开发人员能够更快、更简单地完成一般深度学习任务


模型都自己写嘛？
> 不是，至少不全是。
> 
> `陆吾` 希望成为一个无代码的深度学习平台，其核心在于怎么无代码进行深度学习上。故，模型编写很重要，但不是最重要的，众多模型开发工作量很大，一切以平台功能为优先。
> 
> 所以，模型**有好的轮子就用现成的轮子，没有合适的轮子就自己造**。
> 
> PS：模型编写不是最重要的 **!=** 模型编写不重要

项目使用TensorFlow作为后端。

当前项目只是一个勉强可以运行的超简陋版本，等待持续迭代……

功能规划（只是一个大概的规划，用于引导项目前进，持续调整中……）：

- 任务类型
  - [x] 分类任务
    - [x] 图像分类
    - [ ] 文本分类
    - [ ] 时间序列分类
  - [ ] 回归任务
    - [ ] 图像回归
    - [ ] 文本回归
    - [ ] 时间序列回归
  - [ ] 综合场景任务
    - [ ] 图像类
      - [ ] 目标检测
      - [ ] 语义分割
      - [ ] 实体分割
    - [ ] 文本类
      - [ ] 命名实体识别
      - [ ] 关系抽取
      - [ ] 文本生成
    - [ ] 时间序列
      - [ ] 序列标注
  - [ ] 搭积木式拖拽自由定制模型
- [x] 模型引擎
  - [x] 预设模型（也就是提前写好的、固定的模型）
  - [ ] 半自动化的网络结构搜索
    - [ ] KerasTuner
    - [ ] NNI 
  - [ ] 全自动的网络结构搜索
    - [ ] AutoKeras
- [x] 架构和辅助功能
  - [x] 任务进程调度模块（乞丐版）
  - [x] Web交互 (乞丐版，坐等前端和UI大佬用爱发电)
  - [x] 数据集组织方式
    - [x] 图像分类 
      - [x] 按文件夹组织（每一个类别的图片放在一个单独文件夹下，这些文件夹又放在同一个文件夹下）
      - [ ] 以路径+类别的文本文件组织
    - [ ] 文本分类
      - [ ] [doccano](https://github.com/doccano/doccano)的导出格式
        - [ ] csv
        - [ ] jsonl
    - [ ] 更多...
  - [x] 代码生成
    - [x] 生成简单的调用示例脚本
    - [ ] 生成可用于生产环境部署的项目
  - [ ] 训练进度提示和指标展示
  - [x] 在线查看训练日志
  - [ ] 训练优化
    - [ ] EarlyStopping
    - [ ] 迁移学习解冻特征抽取器做二次 Fine turn
    - [ ] 自动样本均衡

### ✨ [Demo](https://github.com/AaronJny/luwu)

## 运行项目

当前支持两种运行方式，使用 `Docker` 或 `Clone` 项目代码。

### Clone 项目代码

**建议使用Anaconda管理Python环境**。

如果没有安装Anaconda，可以先自行安装。下载链接：[https://www.anaconda.com/products/individual#Downloads](https://www.anaconda.com/products/individual#Downloads)

使用Anaconda配置环境并启动项目：

```sh
conda create -n luwu python=3.7
conda activate luwu
git clone https://github.com/AaronJny/luwu.git
cd luwu
pip install -r requirements.txt
python luwu/run.py
```

使用非Anaconda版本的Python启动项目：

```sh
git clone https://github.com/AaronJny/luwu.git
cd luwu
pip install -r requirements.txt
python3 luwu/run.py
```

### 使用 Docker 运行

```
待补充
```

## 使用说明

1.按照上面的说明之一，将项目运行起来。

项目默认运行在 7788 端口，在浏览器中打开 [http://localhost:7788/](http://localhost:7788/) 即可进入项目主页。

项目主页当前默认为图像分类页面。

![](./asserts/图像分类.png)

2.选择模型引擎，当前只支持预设模型。

选择后会展开该引擎支持的模型列表。

![](./asserts/图像分类-模型列表.png)

图中的这些模型主要都是对tf.keras.applications下的模型的封装，支持使用少量样本做迁移学习。

模型默认选中 `DenseNet121`，你也可以换成其他想使用的模型。

3.配置数据集路径和训练参数

![](./asserts/数据集路径配置.png)

数据集类型当前只支持“按文件夹组织”，即每一个类别的图片放在一个单独文件夹下，这些文件夹又放在同一个文件夹下，比如我这里的猫狗分类数据集：

![](./asserts/数据集-文件夹.png)

`陆吾` 在进行模型训练前，会先尝试将原始数据集转成TFRecordDataset的格式，并切分验证集。

页面中的“清洗后数据集保存路径”即为保存转换后的TFRecordDataset格式的数据集的路径，只需要指定放在哪个文件夹下即可。

如果不填写，默认与“原始数据集路径”保持一致。

训练过程中，`陆吾` 会保存训练过程中的当前最佳模型参数、日志文件，并在训练完成后生成调用代码模板。

这些文件将被保存到页面上“模型及生成代码的保存路径”中填写的文件夹下。

如果不填写，默认与“清洗后数据集保存路径”保持一致。

再下面是两项配置：
- Batch Size，表示训练时mini batch 的大小，即一次训练几个样本
- Epochs，即最多在训练集上进行几次完整遍历

如果不清楚这两项的作用，可以先不调整它，并以如下原则为指导：
- 当训练过程中内存溢出时，请选择更小的Batch Size
- 当训练完成后，训练效果不够好时，可以选择更大的 Epochs

如果只是想体验一下，可以将Epochs设为1或2，这样可以更快看到结果。

为什么可以选择的参数这么少？
> 为了简单。

这样不是牺牲了灵活性吗？
> 是的。后面会考虑怎么在开放更多可配置参数满足灵活性需求的同时，也不会对新手玩家造成干扰。

然后点击“添加项目”即可，将自动跳转到项目列表页面。

4.项目列表

我们可以在项目列表看到刚刚创建的项目。

![](./asserts/项目列表1.png)

鼠标移动到“配置参数”上，可以展开详情：

![](./asserts/项目列表2.png)

点击“开始训练”按钮，项目会进入调度，开始训练：

![](./asserts/训练1.png)

![](asserts/训练2.png)

一段时间后，训练完成。

![](asserts/训练3.png)

我们可以在“模型及生成代码的保存路径”中找到训练日志、训练好的模型文件以及调用代码模板。

![](asserts/训练4.png)

你也可以在浏览器中，点击“调用方式”在线浏览调用代码模板。

![](asserts/训练5.png)

使用说明就到这里了，训练好的模型和调用方法都给你了，还要啥自行车？


## Code Contributors

饭碗已摆好，坐等各路大佬贡献代码~

不过大佬们应该也看不上我这弱鸡项目(卑微.jpg)……

## Author

👤 **AaronJny**

* Website: https://blog.csdn.net/aaronjny
* Github: [@AaronJny](https://github.com/AaronJny)


## 🤝 Contributing

使用中出现什么问题，或者有什么建议，都欢迎在项目里发起 [issues](https://github.com/AaronJny/luwu/issues)。

另外欢迎有兴趣的大佬们贡献代码，共同开发~

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/AaronJny/luwu/issues). You can also take a look at the [contributing guide](https://github.com/AaronJny/luwu).

## Show your support

如果这个项目对你有所帮助的话，麻烦给点个 star ⭐️ 哈~

多谢多谢~

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [AaronJny](https://github.com/AaronJny).<br />
This project is [MIT](https://github.com/AaronJny/luwu/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_