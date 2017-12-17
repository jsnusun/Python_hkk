#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ship.py
# @Author: huangkeke
# @Date  : 2017/12/11
# @Contact : hkkhuang@163.com

import pygame

class Ship():
    """飞船类"""

    def __init__(self,screen):
        """
        初始化飞船并设置其初始位置
        函数返回一个表示飞船的surface，而我们将这个surface存储到了self.image中
        """
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect

        # 将每一艘新飞船放在屏幕底部中央位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


