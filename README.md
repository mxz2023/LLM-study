## 代码规范

文件名

* 全部使用小写字母
* 单词之间使用下划线分隔
* 示例: app_service.py

类名

* 采用驼峰命名法
* 首字母及每个单词首字母大写
* 禁止使用下划线分隔单词
* 示例: class AppService

函数名和方法名

* 全部采用小写字母
* 使用下划线分隔单词
* 示例: get_account

变量名

* 与函数名规范相同
* 示例: my_variable

常量名

* 全部字母大写
* 使用下划线分隔单词
* 示例: MAX_CONNECTIONS

私有变量和方法

* 以单个下划线开头
* 示例: _private_variable, _private_method()

模块名

* 与文件名规范相同（小写字母+下划线）
* 需要包含 __init__.py 文件声明模块
* 建议在初始化文件中使用简化导出
* 示例: my_module.py 对应模块名 my_module