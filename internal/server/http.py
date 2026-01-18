# -*- coding: utf-8 -*-
"""
@Time ： 2026/1/18 22:16
@Auth ： Vincent_Gemini
@File ： http.py
@IDE ： PyCharm
@Motto：Code changes Everything
"""

from flask import Flask
from internal.router import Router


class Http(Flask):
    """http服务引擎"""

    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)
