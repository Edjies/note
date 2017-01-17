### 从Jinja2 模板开始

Flask的render_template(template_name, **kw) 函数使用Jinja2引擎渲染页面， 模板默认存储在 templates文件夹中

#### 模板中的变量和方法
* 模板通过 {{ object  }} 使用变量
* 第一种变量是通过render_template()函数传入
* 一部分flask默认提供的变量和方法（context），包括：

对象 | 说明 | 备注
-|-|-
config|配置对象|flask.config
request|请求对象|flask.request
session||flask.session
g||flask.g
url_for()||
get_flashed_messages()||
* 在模板中导入宏时需要注意： `{% from '_helpers.html' import my_macro with context %}` flask 不会为宏默认提供context, 所以需要主动传递

#### 模板中的控制结构
* 通过 {% %}使用语句
* for 循环结构
* if 结构






