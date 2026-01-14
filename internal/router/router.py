# -*- coding: utf-8 -*-
"""
@Time ： 2026/1/12 07:25
@Auth ： Vincent_Gemini
@File ： router.py
@IDE ： PyCharm
@Motto：Code changes Everything
"""

from flask import Flask, Blueprint

from internal.handler import AppHandler


class Router:
    """路由"""

    def register(self, app: Flask):
        """注册路由"""
        # 1 创建蓝图
        bp = Blueprint('llmops', __name__, url_prefix='')
        # 2 将url与对应的控制器方法进行绑定
        app_handler = AppHandler()
        bp.add_url_rule("/ping", view_func=app_handler.ping)

        # 3 在应用上注册蓝图
        app.register_blueprint(bp)
