# -*- coding: utf-8 -*-
# @Date         : 2021-01-21
# @Author       : AaronJny
# @LastEditTime : 2021-01-21
# @FilePath     : /LuWu/luwu/core/models/classifier/preset/desnet.py
# @Desc         :
import os
import random

import tensorflow as tf
from jinja2 import Template
from luwu.core.preprocess.data.data_generator import ImageClassifierDataGnenrator
from luwu.core.preprocess.image.load import (
    read_classify_dataset_from_dir,
    write_tfrecords_to_target_path,
)


class LuwuImageClassifier:
    def __init__(
        self,
        origin_dataset_path: str = "",
        target_dataset_path: str = "",
        model_save_path: str = "",
        validation_split: float = 0.2,
        batch_size: int = 32,
        epochs: int = 30,
    ):
        """
        Args:
            origin_dataset_path (str): 处理前的数据集路径
            target_dataset_path (str): 处理后的数据集路径
            model_save_path (str): 模型保存路径
            validation_split (float): 验证集切割比例
            batch_size (int): mini batch 大小
            epochs (int): 训练epoch数
        """
        self.origin_dataset_path = origin_dataset_path
        # 当未给定处理后数据集的路径时，默认保存到原始数据集相同路径
        if target_dataset_path:
            self.target_dataset_path = target_dataset_path
        else:
            self.target_dataset_path = origin_dataset_path
        # 当未给定模型保存路径时，默认保存到处理后数据集相同路径
        if model_save_path:
            self.model_save_path = model_save_path + "best_weights.h5"
        else:
            self.model_save_path = os.path.join(
                self.target_dataset_path, "best_weights.h5"
            )
        self.validation_split = validation_split
        self.batch_size = batch_size
        self.epochs = epochs

    def build_model(self) -> tf.keras.Model:
        """构建模型

        Raises:
            NotImplementedError: 待实现具体方法
        """
        raise NotImplementedError

    def preprocess_dataset(self):
        """对数据集进行预处理"""
        # 读取原始数据
        data, classes_num_dict = read_classify_dataset_from_dir(
            self.origin_dataset_path
        )
        # 类别->编号的映射
        self.classes_num_dict = classes_num_dict
        # 编号->类别的映射
        self.classes_num_dict_rev = {
            value: key for key, value in self.classes_num_dict.items()
        }
        # 切分数据
        total = len(data)
        dev_nums = int(total * self.validation_split)
        dev_data = random.sample(data, dev_nums)
        train_data = list(set(data) - set(dev_data))
        del data
        # 制作tfrecord数据集
        self.target_train_dataset_path = os.path.join(
            self.target_dataset_path, "train_dataset"
        )
        self.target_dev_dataset_path = os.path.join(
            self.target_dataset_path, "dev_dataset"
        )
        write_tfrecords_to_target_path(
            train_data, len(classes_num_dict), self.target_train_dataset_path
        )
        write_tfrecords_to_target_path(
            dev_data, len(classes_num_dict), self.target_dev_dataset_path
        )
        # 读取tfrecord数据集
        self.train_dataset = ImageClassifierDataGnenrator(
            self.target_train_dataset_path, batch_size=self.batch_size
        )
        self.dev_dataset = ImageClassifierDataGnenrator(
            self.target_dev_dataset_path, batch_size=self.batch_size, shuffle=False
        )

    def train(self):
        # callbacks
        checkpoint = tf.keras.callbacks.ModelCheckpoint(
            self.model_save_path, monitor="val_accuracy", verbose=1, save_best_only=True
        )
        # 训练
        self.model.fit(
            self.train_dataset.for_fit(),
            epochs=self.epochs,
            steps_per_epoch=self.train_dataset.steps,
            validation_data=self.dev_dataset.for_fit(),
            validation_steps=self.dev_dataset.steps,
            callbacks=[
                checkpoint,
            ],
        )

    def generator_train_code(self):
        """导出模型定义和训练代码"""
        raise NotImplementedError

    def generate_code(self):
        """导出模型定义和模型调用的代码"""
        raise NotImplementedError


class LuwuPreTrainedImageClassifier(LuwuImageClassifier):
    def __init__(self, net_name, *args, **kwargs):
        super(LuwuPreTrainedImageClassifier, self).__init__(*args, **kwargs)
        self.net_name = net_name

    def build_model(self, num_classes=10):
        pre_trained_net: tf.keras.Model = getattr(
            tf.keras.applications, self.net_name
        )()
        pre_trained_net.trainable = False
        # 记录densenet
        self.pre_trained_net = pre_trained_net
        model = tf.keras.Sequential(
            [
                pre_trained_net,
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(1000, activation="relu"),
                tf.keras.layers.Dropout(0.3),
                tf.keras.layers.Dense(num_classes, activation="softmax"),
            ]
        )
        model.compile(
            optimizer=tf.keras.optimizers.Adam(),
            loss=tf.keras.losses.categorical_crossentropy,
            metrics=["accuracy"],
        )
        self.model = model
        return model

    def generate_code(self):
        """导出模型定义和模型调用的代码"""
        template_path = os.path.join(
            __file__, "./templates/LuwuPreTrainedImageClassifier.txt"
        )
        with open(template_path, "r") as f:
            text = f.read()
        data = {
            "net_name": self.net_name,
            "num_classes": len(self.classes_num_dict),
            "num_classes_map": str(self.classes_num_dict_rev),
            "model_path": self.model_save_path,
        }
        template = Template(text)
        code = template.render(**data)
        code_path = os.path.join(os.path.dirname(self.model_save_path), "code.py")
        with open(code_path, "w") as f:
            f.write(code)


class LuwuDenseNet121ImageClassifier(LuwuPreTrainedImageClassifier):
    def __init__(self, net_name="DenseNet121", **kwargs):
        super(LuwuDenseNet121ImageClassifier, self).__init__(net_name, **kwargs)


class LuwuDenseNet169ImageClassifier(LuwuPreTrainedImageClassifier):
    def __init__(self, net_name="DenseNet169", **kwargs):
        super(LuwuDenseNet121ImageClassifier, self).__init__(net_name, **kwargs)


class LuwuDenseNet201ImageClassifier(LuwuPreTrainedImageClassifier):
    def __init__(self, net_name="DenseNet201", **kwargs):
        super(LuwuDenseNet121ImageClassifier, self).__init__(net_name, **kwargs)