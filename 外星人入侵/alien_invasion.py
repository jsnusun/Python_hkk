#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : alien_invasion.py
# @Author: huangkeke
# @Date  : 2017/12/11
# @Contact : hkkhuang@163.com

"""外星人入侵"""

from settings import Settings
from ship import Ship
import sys
import pygame

def run_game():
    """初始化游戏,并创建一个屏幕对象"""


    ai_setting = Settings()

    # 创建一个名为screen的显示窗口 游戏的所有元素都在其中绘制 实参是一个元组 规定窗口尺寸
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 设置背景色  该颜色只需要指定一次 在进入主循环之前定义
    # bg_color = (230, 230, 230)  # 颜色是以RGB的形式指定  这里是浅灰色

    pygame.init()  # 初始化背景设置

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都会重新绘制屏幕
        screen.fill(ai_setting.bg_color)  # 方法screen.fill() 用背景色填充屏幕  接受一个实参:一种颜色

        ship.blitme()

        # 让绘制的屏幕可见
        pygame.display.flip()


run_game()

