# -*- coding: utf-8 -*-
"""
@Time ： 2026/1/18 22:19
@Auth ： Vincent_Gemini
@File ： app.py
@IDE ： PyCharm
@Motto：Code changes Everything
"""
import dotenv

from injector import Injector
from internal.server import Http
from internal.router import Router

# 将env变量加载到环境 - 必须在其他导入之前执行
dotenv.load_dotenv()

injector = Injector()

app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
