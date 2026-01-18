# -*- coding: utf-8 -*-
"""
@Time ： 2026/1/12 07:23
@Auth ： Vincent_Gemini
@File ： app_handler.py
@IDE ： PyCharm
@Motto：Code changes Everything
"""
from flask import request
from openai import OpenAI


class AppHandler:
    """应用控制器"""

    def ping(self):
        """ping接口"""
        return {"code": 200, "message": "success", "data": "pong"}

    def completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取的输入，POST
        queue = request.json.get("queue", "")

        # 2. 构建OpenAI客户端，并发起请求
        client = OpenAI(
            api_key="sk-8bd1a5ffec144461b3ac51c99d07f261",
            base_url="https://api.deepseek.com")

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
