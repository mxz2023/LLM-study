# -*- coding: utf-8 -*-
"""
@Time ： 2026/1/12 07:23
@Auth ： Vincent_Gemini
@File ： app_handler.py
@IDE ： PyCharm
@Motto：Code changes Everything
"""
import os
from dataclasses import dataclass

from injector import inject

from flask import request
from openai import OpenAI


@inject
@dataclass
class AppHandler:
    """应用控制器"""

    # app_service: AppService
    #
    # def create_app(self):
    #     """调用服务创建新的APP记录"""
    #     app = self.app_service.create_app()
    #     return success_message(f"应用已经成功创建，id为{app.id}")
    #
    # def get_app(self, id: uuid.UUID):
    #     app = self.app_service.get_app(id)
    #     return success_message(f"应用已经成功获取，名字是{app.name}")
    #
    # def update_app(self, id: uuid.UUID):
    #     app = self.app_service.update_app(id)
    #     return success_message(f"应用已经成功修改，修改的名字是:{app.name}")
    #
    # def delete_app(self, id: uuid.UUID):
    #     app = self.app_service.delete_app(id)
    #     return success_message(f"应用已经成功删除，id为:{app.id}")

    def completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取的输入，POST
        queue = request.json.get("queue", "")

        # 2. 构建OpenAI客户端，并发起请求
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )

        # 3. 得到请求相应，然后将OpanAI的相应传给前端
        completion = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是OpenAI的助手,帮助用户解答问题。"},
                {"role": "user", "content": queue}
            ]
        )

        content = completion.choices[0].message.content

        return {"code": 200, "message": "success", "data": content}

    def ping(self):
        """ping接口"""
        return {"code": 200, "message": "success", "data": "pong"}
