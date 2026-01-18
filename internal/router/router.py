# -*- coding: utf-8 -*-
"""
@Time ： 2026/1/12 07:25
@Auth ： Vincent_Gemini
@File ： router.py
@IDE ： PyCharm
@Motto：Code changes Everything
"""

from flask import Flask, Blueprint
from dataclasses import dataclass
from injector import inject

from internal.handler import AppHandler


class Router:
    """路由"""
    app_handler = AppHandler()

    def register_router(self, app: Flask):
        """注册路由"""
        # 1 创建蓝图
        bp = Blueprint('llmops', __name__, url_prefix='')

        # 2 将url与对应的控制器方法进行绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)

        # 3 在应用上注册蓝图
        app.register_blueprint(bp)
