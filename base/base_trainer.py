# -*- coding:utf-8 -*-
"""
Project Name: dl_seq2seq_demo
File Name: base_trainer.py
Author: gaoyw
Create Date: 2021/4/13
Description: 训练器的基类
"""


class Trainer(object):
    def __init__(self):
        pass

    def train(self):
        """
        定义训练行为
        :return:
        """
        pass

    def evaluate(self):
        """
        定义评估行为
        :return:
        """
        pass

    def test(self):
        """
        定义测试行为
        :return:
        """
        pass

    def predict(self):
        """
        定义预测行为
        :return:
        """
        pass

    def generate(self, inputs):
        """
        定义一种生成行为，利用模型去生成一个句子，该方法被train,test,evaluate,predict方法调用组织
        :return:
        """
        pass
