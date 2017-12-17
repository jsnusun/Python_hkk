#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : settings.py
# @Author: huangkeke
# @Date  : 2017/12/11
# @Contact : hkkhuang@163.com


class Settings():
    """存储游戏的所有设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)