# weibo-sdk-web

> 用户名+密码的方式，通过https://weibo.com调用API

### Install
```
pip install weibo-sdk-web
```

### 功能
* 登陆
* 发帖：文字
* 发帖：文字+图片

### API
|方法|参数|类型|返回|
|---|---|---|---|
|login|None|None|None|
|get_username|None|None|string|
|post_text|text|string|dict|
|post_text_with_img|text|string|dict|
| |imgs|可访问url的列表| |
|post_text_with_b64img|text|string|dict|
| |imgs|base64的列表| |

### 例子
```python
from weibo_web import Weibo
wb = Weibo('username', 'password')

wb.login()

wb.post_text('文本')

wb.post_text_with_b64img('文本', ['base64Data'])

wb.post_text_with_img('文本', ['https://path/to/img.jpg'])

wb.get_username()
```

### 如何安全地设置账号的用户名和密码？

建议通过环境变量暴露值，在应用中获取
```shell script
$ export WEIBO_USERNAME=你的用户名
$ export WEIBO_PWD=你的密码
```

### Pypi
https://pypi.org/project/weibo-sdk-web/

### Thanks to
* https://github.com/xchaoinfo/fuck-login
