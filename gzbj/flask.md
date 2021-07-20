项目结构

# Flask文档(相关记录)

参考https://dormousehole.readthedocs.io/en/latest/

## 一.快速上手

### 1.调试模式

1. 1  set FLASK_ENV=off（关闭开发调试模shell下，linux set换成export）

   1.2   set FLASK_ENV=development  (开发调试模式开启shell下，linux set换成export)

### 2.路由

#### 1.路由demo

```
from  flask import  Flask 
app = Flask(__name__)
@app.route('/')
def index():
	return  'Index page'
@app.route('/hello')
def hello():
	return  'Hello,World'
if  __name__ == '__main__':
	app.run()
```

#### 2.变量规则

```
from  flask  import  Flask,escape 
app = Flask(__name__)
@app.route('/user/<username>')
def show_user_profile(username)
	return  'User %s '% escape(username)
@app.route('/post/int:post_id')
def show_post(post_id):
	return 'Post %d' %post_id
@app.route('/path/<path:subpath>')
def show_subpath(subpath:)
	return 'Subpath %s' % escape(subpath)
```

string （缺省值）接受任何不包含斜杠的文本
int 接受正整数
float 接受正浮点数
path 类似 string ，但可以包含斜杠
uuid 接受 UUID 字符串



#### 3.重定向行为



```
#访问一个没有斜杠结尾的,会自动进行重定向，帮你在尾部加上一个斜杠。
@app.route('/projects/')
def projects():
	return 'The project page'
#about 的 URL 没有尾部斜杠,如果访问这个 URL 时添加了尾部斜杠就会
得到一个 404 错误。这样可以保持 URL 唯一，
@app.route('/about')
def about():
	return 'the about page'
```



#### 4.URL构建(ur_lfor)

暂时理解就是找路由

```
# -*- coding: utf-8 -*-
#!/usr/bin/python3
from flask import Flask,request,url_for,escape
app = Flask(__name__)
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'
@app.route('/user/<username>')
def profile(username):
    return '{}\' profile'.format(escape(username))
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == "__main__":
    app.run(debug=True)
    
    
控制台结果
/ 
/login
/login?next=/
/user/John%20Doe
```

#### 5.HTTP方法

```
from flask import request
@app.route('/login', methods=['GET', 'POST']) 
def login(): 
	if request.method == 'POST': 
		return do_the_login() 
	else:
    	return show_the_login_form()

```

#### 

### 3.静态文件

```
url_for('static', filename='style.css')
```

这个静态文件在文件系统中的位置应该是 static/style.css 

### 4.渲染模板

```
from  flask import  Flask
from  flask  import  render_template
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<mame>')
def hello(mame=None):
    return render_template('hello.html', mame=mame)


if  __name__ == '__main__':
    app.run()
```

```
情形1: 一个模块:
/application.py 
/templates 
	/hello.html
情形2: 一个包:
/application 
	/__init__.py 
	/templates 
		/hello.html

```

```
<!doctype html> 
<title>Hello from Flask</title> 
{% if name %} 
<h1>Hello {{ name }}!</h1>
{% else %} 
<h1>Hello, World!</h1>
{% endif %}

```

#### 1.Markup方法的使用案例

##### 1.app.py

```
from flask import render_template
from flask import Flask
from flask import Markup
from flask import abort, redirect
app = Flask(__name__)
@app.route('/')
def hello_site():
  return "welcome my site!!!!!" #返回给客户端
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = None):
  print (Markup('<strong> Hi %s!</strong>' %(name)))
  return render_template('hello.html', name = Markup('%s'%(name))) #模板渲染在html文件中， Markup装换特殊字符！
if __name__ == "__main__":
  app.run()
```



##### 2.hello.html

```
<!DOCTYPE html>
<title>Hello from flask</title>
{%if name %}
  <h1>Hello {{name}}!</h1>
{%else%}
  <h1>Hello World!No name!</h1>
{%endif%}
```



### 5.操作请求数据

#### 1.文件上传

```
不要忘记表单中设置 enctype="multipart/ form-data" 属性

from flask import request
@app.route('/upload', methods=['GET', 'POST'])
def upload_file(): 
	if request.method == 'POST': 
		f = request.files['the_file']
		f.save('/var/www/uploads/uploaded_file.txt')
		
		
如果想要把客户端的文件名作为服务器上的文件名，可以通过Werkzeug提供 的 secure_filename() 函数:
from flask import request
from werkzeug.utils import secure_filename
@app.route('/upload', methods=['GET', 'POST'])
def upload_file(): 
	if request.method == 'POST':
    f = request.files['the_file'] 		
    f.save('/var/www/uploads/' + secure_filename(f.filename)) 		

```

#### 2.cookies

```
要访问cookies，可以使用cookies 属性。可以使用响应对象的set_cookie 方法来设置cookies。请求对 象的cookies 属性是一个包含了客户端传输的所有cookies的字典。在Flask中，如果使用会话 ，那么就不 要直接使用cookies，因为会话比较安全一些。
读取cookies:
from flask import request
@app.route('/') 
def index(): 
	username = request.cookies.get('username') 
# use cookies.get(key) instead of cookies[key] to not get a # KeyError if the cookie is missing.

储存cookies:
from flask import make_response
@app.route('/') 
def index(): 
	resp = make_response(render_template(...)) 
	resp.set_cookie('username', 'the username') 
	return resp
注意，cookies 设置在响应对象上。通常只是从视图函数返回字符串，Flask 会把它们转换为响应对象。如果 你想显式地转换，那么可以使用make_response() 函数，然后再修改它。 使用延迟的请求回调方案可以在没有响应对象的情况下设置一个cookie。 同时可以参见关于响应。

```

#### 



### 6.重定向和错误

#使用redirect() 函数可以重定向。使用abort() 可以更早退出请求，并返回错误代码:

```
from flask import abort, redirect, url_for
@app.route('/') 
def index(): 
	return redirect(url_for('login'))
@app.route('/login') 
def login():
	abort(401) 
	this_is_never_executed()

```

使用errorhandler() 装饰器可以定制出错 页面:

```


from  flask import  Flask
from flask import render_template
from  flask import  abort,redirect,url_for
app = Flask(__name__)
@app.route('/')
def index():
    return  redirect(url_for('login'))

@app.route('/login')
def login():
    return ('重定向到的login')


from flask import render_template
@app.errorhandler(404)
def page_not_found(error):
    return '-------不好意思---页面走丢了---',404


if  __name__ == '__main__':
    app.run()
```

### 7.关于响应(格式)

#### 1.HTTP简介：

1.HTTP是Hyper Text Transfer Protocol的缩写（超文本传输协议），是用于从万维网（WWW:World Wide Web）服务器传输超文本到本地浏览器的传送协议。你问我什么是[超文本](https://baike.baidu.com/item/超文本/2832422?fr=aladdin)？



2.是基于TCP/IP通信协议来传递数据的（HTML文件，图片文件，查询结果等）。



3.HTTP基于C/S架构模型（客户端/服务端），通过一个可靠的链接来交换信息。浏览器作为HTTP客户端向WEB服务器发送所有的请求，WEB服务器收到请求以后，向HTTP客户端发送响应消息。



#### 2.特点：		

1.简单快速：客户端每次向服务器发出请求的时候只需要传递请求方法和路径。常用方法比如：GET，POST，每种方法规定了客户端和服务端联系方式的不同。由于HTTP协议简单，使得HTTP服务器程序规模小，因此通信速度较快。



2.灵活：HTTP允许传输任意类型的数据对象。正在传输的类型由Content-Type标记。



3.无连接：无连接的意思是每次连接只会处理一个请求（相对的也会有一个响应）。服务器处理完客户的请求以后，客户端拿到了服务器发出的响应，随后断开连接。采用这种方式节省传输时间。



4.无状态：HTTP协议是无状态协议。无状态是指协议对事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息时它的应答就较快。





#### 3.HTTP请求/响应报文：

1.**HTTP请求报文由三部分组成**



![img](https://img-blog.csdn.net/20170707143243946?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaGV5dWVfOTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

**请求行**由（123）组成：1是请求方法；2是url地址，它和报文头的Host属性组成完整的请求URL；3是协议名称和版本号。



**请求头**（4）：是HTTP的报文头，报文头包含若干个属性，\**格式均为"属性名：属性值"，服务端由此获得客户端的信息\**。与缓存有关的信息都放在头部（header）。（key:value的形式，一个key对应一个value，一个key对应多个value，但是其实一个key也可以对应多个value。结果区别就是aa：bb和aa：bb，cc）



**请求体**（5）：它将一个\**页面表单中的组件值\**通过param1=value1&param2=value2的键值对形式编码成一个格式化串，它承载着多个请求参数的数据。





**2.HTTP响应报文也由三部分组成**



![img](https://img-blog.csdn.net/20170707145557633?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaGV5dWVfOTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



**响应行（12） 组成：1是报文协议及版本，2是\**状态码及描述\**。**



**响应头（3）：和请求头一样，由属性组成。**



**响应体（4）：是服务器返回给客户端的文本信息。**



#### 4.设置响应信息的方法（返回自定响应头，两种方式）

(1) 第一种是：视图函数return的时候，使用元组，返回自定义的信息返回的时候的状态码可以自定义信息："状态码  自定义的信息"，例如： 可以把下面代码中的400，改成自定义的状态码：  "666 custom info"

```
from flask import Flask

app = Flask(__name__)

@app.route("/index")

def index():、
    """
      1. 使用元组，返回自定义的响应信息

        返回响应体，状态码，响应头

        return 多个值时，就会是一个元组的形式

    """
    """
        除了用字典的形式，也可以用字典的形式

        return "index page", 400, {"Itcast": "python", "City": "beijing"}

    """

    return "index page", 400, [("Itcast", "python"), ("City", "beijing")]

if __name__ == '__main__':

    app.run(debug=True)
```

访问网页后，可以看到自定义的响应头信息， 当然可以设置标准的响应头信息，根据需求，这是通过元组的方式。

![img](https://img-blog.csdnimg.cn/20181221145209186.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaTE4NzkxOTU3MjQz,size_16,color_FFFFFF,t_70)





注意， 在return值的时候可以只给前端传响应体和状态码，不传响应头但不可以只传响应体和响应头，即有响应头，必须要有状态码它是有顺序的，第一个响应体，第二个状态码，第三个响应头，可以从后面省但不可从前面省。





  (2) 第二种方式： 使用make_response 来构造响应信息（从flask中导入make_response）s

resp = make_response("响应体")

 resp.status = "状态码，可以是自定义的状态码"

resp.headers["键"] = "值"  # 通过字典的形式设置响应头

```
from flask import Flask, make_response
app = Flask(__name__)
@app.route("/index")

def index():
    # 2. 使用make_response 来构造响应信息

    resp = make_response("index page2")  # 响应体数据

    resp.status = "999 itcast"  # 状态码

    resp.headers["City"] = "ShangHai"  # 通过字典的形式添加响应头

    return resp
if __name__ == '__main__':

    app.run(debug=True)
```

访问网页看到的结果是一样的



![img](https://img-blog.csdnimg.cn/20181221152541840.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaTE4NzkxOTU3MjQz,size_16,color_FFFFFF,t_70)

​    

#### 5.给前端返回数据

1.通过传统的方式，先构造一个字典，然后经过json模块转化为字符串，视图函数返回字符串以及修改响应头的类型接口

2.通过flask中的 jsonify来进行返回

​	有两种方式 

​	**第一种**是把构造好的字典直接传进去返回即可  return jsonify(构造的字典) **第二种**是直接在jsonify() 里面进行构造   return jsonify(键=值,键=值) ，其效果是一样的

```
from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route("/index")
def index():

    """向前端返回json类型的数据"""

    data = {

        "name": "python",

        "age": 18

    }

    """

        传统的方式去传递

        # json.dumps(字典)  将Python的字典转换为json的字符串

        # json.loads(字符串)  将字符串转换为Python中的字典

        json_str = json.dumps(data)

        # 改变，响应头的类型

        return json_str,200,{"Content-Type":"application/json"}

    """

    '''

        jsonify()的使用

        1.jsonify()帮助转为json数据，并设置响应头 Content-Type 为 application/json

        2. 可以不用提前构造好字典，直接返回,结果是一样的

            return jsonify(City="Beijing",age=20)

    '''

    return jsonify(data)

if __name__ == '__main__':

    app.run(debug=True)
```

访问网页后：

![img](https://img-blog.csdnimg.cn/2018122116001439.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaTE4NzkxOTU3MjQz,size_16,color_FFFFFF,t_70)

### 8.会话（案例）

#### app.py

```

from  flask  import Flask,render_template,request,redirect,session,url_for
app = Flask(__name__)
app.debug = True
# 使用会话之前你必须设置一个密钥
# import os; print(os.urandom(16))
app.secret_key=b'\xde~\x89\xe7.$\n}\xa4\xfcwB|\xf9\xca\xd3'

USERS = {
    1:{'name':'张三','age':18,'gender':'男','text':'道路千万条'},
    2:{'name':'李四','age':28,'gender':'男','text':'安全第一条'},
    3:{'name':'王五','age':18,'gender':'女','text':'行车不规范'}
}

@app.route('/detail/<int:nid>',methods=['GET'])
def  detail(nid):
    user = session.get('user_info')
    if  not  user:
        return  redirect('/login')
    info = USERS.get(nid)
    return render_template('detail.html',info=info)

@app.route('/home',methods  =['GET'])
def home():
    user = session.get('user_info')
    if  not  user:
        url = url_for('l1')
        return redirect(url)
    return render_template('home.html',user_dict=USERS)

@app.route('/login',methods=['GET','POST'],endpoint='l1')
def login():
    if  request.method == 'GET':
        return   render_template('login.html')
    else:
        user=request.form.get('user')
        pwd=request.form.get('pwd')
        if  user =='cxw' and  pwd =='123':
            session['user_info'] = user
            return  redirect('/home')
        return  render_template('login.html',error='用户名密码错误')
if  __name__ == '__main__':
    app.run()
```



#### login.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>用户登录</h1>
<form method="post">
    <input type="text" name="user">
    <input type="text" name="pwd">
    <input type="submit" value="登录">{{error}}

</form>
</body>
</html>
```

#### home.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>用户列表</h1>
<table>
    {% for index,items in user_dict.items() %}
    <tr>
        <td>{{index}}</td>
        <td>{{items.name}}</td>
        <td>{{items['age']}}</td>
        <td>{{items.get('gender')}}</td>
        <td><a href="{{url_for('detail',nid=index)}}">查看详细</a></td>
    </tr>
    {% endfor %}
</table>
</body>
</html>
```

#### detail.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>详细信息{{info.name}}</h1>
<div>
    {{info.text}}
</div>
</body>
</html>
```

### 9.消息闪现？

现用现搜  有问题

### 10.日志

```
from flask import Flask
import logging

app = Flask(__name__)


@app.route('/')
def root():
    try:
        a = [ 1, 3 ,3 ,4]
        print(a[7])
    except Exception as e:
        app.logger.info('info log')
        app.logger.warning(e)
        app.logger.error('An error occurred')

    return 'hello'

if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    # 即设置日志记录最低级别为DEBUG，低于DEBUG级别的日志记录会被忽略，不设置setLevel()则默认为NOTSET级别。
    # handler.setLevel(logging.DEBUG)
    '''
    %(asctime)s 即日志记录时间，精确到毫秒
    %(levelname)s 即此条日志级别
    %(filename)s 即触发日志记录的python文件名
    %(funcName)s 即触发日志记录的函数名
    %(lineno)s 即触发日志记录代码的行号
    %(message)s 这项即调用如app.logger.info('info log')中的参数，即message
    '''
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run()
```



### 11.集成WSGI中间件？

### 12.Flask扩展

##### 1.sqllite数据库 对应python SQLAlchemy





## 二.教程

### 1.项目布局

```
from flask import Flask
app = Flask(__name__)
@app.route('/') 
def hello(): 
	return 'Hello, World!'
	
然而，当项目越来越大的时候，把所有代码放在单个文件中就有点不堪重负了。Python项目使用包来管理代 码，把代码分为不同的模块，然后在需要的地方导入模块。本教程也会按这一方式管理代码。 教程项目包含如下内容: 
• flaskr/ ，一个包含应用代码和文件的Python包。 
• tests/ ，一个包含测试模块的文件夹。 
• venv/ ，一个Python虚拟环境，用于安装Flask和其他依赖的包。 • 告诉Python如何安装项目的安装文件。 
• 版本控制配置，如git。不管项目大小，应当养成使用版本控制的习惯。 
• 项目需要的其他文件。


```



```
参考flask文档：
  https://dormousehole.readthedocs.io/en/latest/
  
  ctrl+F  '最后，项目布局如下' 看目录
```



### 2.应用设置

一个Flask应用是一个Flask 类的实例。应用的所有东西（例如配置和URL）都会和这个实例一起注册。 创建一个Flask应用最粗暴直接的方法是在代码的最开始创建一个全局Flask 实例。前面的“Hello,World!” 示例就是这样做的。有的情况下这样做是简单和有效的，但是当项目越来越大的时候就会有些力不从心了。
可以在一个函数内部创建Flask 实例来代替创建全局实例。这个函数被称为 应用工厂。所有应用相关的配 置、注册和其他设置都会在函数内部完成，然后返回这个应用。

#### 1.应用工厂

```
# __init__.py 有两个作用：一是包含应用工厂；二是告诉Python flaskr 文件夹应当视作为一个包。
#可以在一个函数内部创建Flask 实例来代替创建全局实例
#所有应用相关的配 置、注册和其他设置都会在函数内部完成，然后返回这个应用。

import os
from flask import Flask

def create_app(test_config=None):
    # 创建和配置应用程序,创建Flask实例
    # __name__ 是当前Python模块的名称。应用需要知道在哪里设置路径，使用 __name__ 是一个方便的方法。
    # instance_relative_config=True告诉应用配置文件是相对于instancefolder的相对路径。
    # 实 例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当提交到版本控制系统。
    app = Flask(__name__, instance_relative_config=True)
    # 设置一个应用的默认配置
    # SECRET_KEY 是被Flask和扩展用于保证数据安全的。在开发过程中，为了方便可以设置为'dev' ，但是在发布的时候应当使用一个随机值来重载它。
    # DATABASE SQLite 数据库文件存放在路径。它位于 Flask 用于存放实例的app.instance_path 之内
    app.config.from_mapping( SECRET_KEY='dev',
                             DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
                             )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        # 使用 config.py 中的值来重载缺省配置，如果 config.py 存在的 话。
        # 例如，当正式部署的时候，用于设置一个正式的 SECRET_KEY 。
        # test_config 也会被传递给工厂，并且会替代实例配置。这样可以实现测试和开发的配置分离， 相互独立。
        app.config.from_pyfile('config.py', silent=True)
    else:
    # load the test config if passed in

        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    # 可以确保app.instance_path存在。Flask不会自动创建实例文件夹，
    # 但是必须确 保创建这个文件夹，因为SQLite数据库文件会被保存在里面。
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    return app


```



#### 2.运行应用

```
Linux and Mac  下
$ export FLASK_APP=flaskr 
$ export FLASK_ENV=development
$ flask run


windows 
> set FLASK_APP=flaskr 
> set FLASK_ENV=development 
> flask run

在浏览器中访问http://127.0.0.1:5000/hello，就可以看到“Hello,World!”信息。恭喜你，Flask网络应用成功 运行了！

```



### 3.定义和操作数据库

应用使用一个 SQLite 数据库来储存用户和博客内容。Python 内置了 SQLite 数据库支持，相应的模块为 sqlite3 。 使用SQLite的便利性在于不需要单独配置一个数据库服务器，并且Python提供了内置支持。但是当并发请 求同时要写入时，会比较慢一点，因为每个写操作是按顺序进行的。小应用没有问题，但是大应用可能就需 要考虑换成别的数据库了。

#### 1.链接数据库

当使用SQLite数据库（包括其他多数数据库的Python库）时，第一件事就是创建一个数据库的连接。所有 查询和操作都要通过该连接来执行，完事后该连接关闭。
在网络应用中连接往往与请求绑定。在处理请求的某个时刻，连接被创建。在发送响应之前连接被关闭。

flaskr/db.py

```
import  sqlite3
import click
# g是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存可能多个函数都会用到的数据。
# 把连接储存于其中，可以多次使用，而不用在同一个请求中每次调用 get_db 时都创建一个新的连接。

# current_app 是另一个特殊对象，该对象指向处理请求的 Flask 应用。这里使用了应用工厂，那么在其 余的代码中就不会出现应用对象。
# 当应用创建后，在处理一个请求时，get_db 会被调用。这样就需要使 用current_app 。

from flask  import  current_app,g
from flask.cli  import  with_appcontext

def get_db():
    if 'db' not in g :
        # sqlite3.connect() 建立一个数据库连接，该连接指向配置中的 DATABASE 指定的文件。这个文件现在
        # 还没有建立，后面会在初始化数据库的时候建立该文件。
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        #sqlite3.Row 告诉连接返回类似于字典的行，这样可以通过列名称来操作数据。
        g.db.row_factory=sqlite3.Row
    return g.db

#close_db 通过检查 g.db 来确定连接是否已经建立。如果连接已建立，那么就关闭连接。
# 以后会在应用工 厂中告诉应用 close_db 函数，这样每次请求后就会调用它。

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()

```



#### 2.创建表

在 SQLite 中，数据储存在 表和 列中。在储存和调取数据之前需要先创建它们。Flaskr 会把用户数据储存在 user 表中，把博客内容储存在 post 表中。下面创建一个文件储存用于创建空表的SQL命令：

```
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL );
CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id)
);

```

在 db.py 文件中添加Python函数，用于运行这个SQL命令：

flaskr/db.py

```
import  sqlite3
import click
# g是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存可能多个函数都会用到的数据。
# 把连接储存于其中，可以多次使用，而不用在同一个请求中每次调用 get_db 时都创建一个新的连接。

# current_app 是另一个特殊对象，该对象指向处理请求的 Flask 应用。这里使用了应用工厂，那么在其 余的代码中就不会出现应用对象。
# 当应用创建后，在处理一个请求时，get_db 会被调用。这样就需要使 用current_app 。

from flask  import  current_app,g
from flask.cli  import  with_appcontext

def get_db():
    if 'db' not in g :
        # sqlite3.connect() 建立一个数据库连接，该连接指向配置中的 DATABASE 指定的文件。这个文件现在
        # 还没有建立，后面会在初始化数据库的时候建立该文件。
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        #sqlite3.Row 告诉连接返回类似于字典的行，这样可以通过列名称来操作数据。
        g.db.row_factory=sqlite3.Row
    return g.db

#close_db 通过检查 g.db 来确定连接是否已经建立。如果连接已建立，那么就关闭连接。
# 以后会在应用工 厂中告诉应用 close_db 函数，这样每次请求后就会调用它。

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()



#用于运行这个SQL命令：
def  init_db():
    db = get_db()
    #open_resource()打开一个文件，该文件名是相对于flaskr包的。这样就不需要考虑以后应用具体部署在哪个位置。get_db
    # 返回一个数据库连接，用于执行文件中的命令
    with  current_app.open_resource('schema.sql') as f :
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    #清除现有数据并创建表
    init_db()
    #初始化数据库
    click.echo('Initialized the database.')
```

#### 3.在应用中注册

flaskr/db.py

```
import  sqlite3
import click
# g是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存可能多个函数都会用到的数据。
# 把连接储存于其中，可以多次使用，而不用在同一个请求中每次调用 get_db 时都创建一个新的连接。

# current_app 是另一个特殊对象，该对象指向处理请求的 Flask 应用。这里使用了应用工厂，那么在其 余的代码中就不会出现应用对象。
# 当应用创建后，在处理一个请求时，get_db 会被调用。这样就需要使 用current_app 。

from flask  import  current_app,g
from flask.cli  import  with_appcontext

def get_db():
    if 'db' not in g :
        # sqlite3.connect() 建立一个数据库连接，该连接指向配置中的 DATABASE 指定的文件。这个文件现在
        # 还没有建立，后面会在初始化数据库的时候建立该文件。
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        #sqlite3.Row 告诉连接返回类似于字典的行，这样可以通过列名称来操作数据。
        g.db.row_factory=sqlite3.Row
    return g.db

#close_db 通过检查 g.db 来确定连接是否已经建立。如果连接已建立，那么就关闭连接。
# 以后会在应用工 厂中告诉应用 close_db 函数，这样每次请求后就会调用它。

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()



#用于运行这个SQL命令：
def  init_db():
    db = get_db()
    #open_resource()打开一个文件，该文件名是相对于flaskr包的。这样就不需要考虑以后应用具体部署在哪个位置。get_db
    # 返回一个数据库连接，用于执行文件中的命令
    with  current_app.open_resource('schema.sql') as f :
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    #清除现有数据并创建表
    init_db()
    #初始化数据库
    click.echo('Initialized the database.')


#在应用中注册
#close_db 和 init_db_command 函数需要在应用实例中注册，否则无法使用。
# 然而，既然我们使用了工 厂函数，那么在写函数的时候应用实例还无法使用。代替地，我们写一个函数，把应用作为参数，在函数中 进行注册。

#在工厂中导入并调用这个函数。在工厂函数中把新的代码放到函数的尾部，返回应用代码的前面。

def init_app(app):
    # 告诉Flask在返回响应后进行清理的时候调用此函数
    app.teardown_appcontext(close_db)
    # 添加一个新的可以与 flask 一起工作的命令。
    app.cli.add_command(init_db_command)
```

在工厂中导入并调用这个函数。在工厂函数中把新的代码放到函数的尾部，返回应用代码的前面。

__init__.py

```
# __init__.py 有两个作用：一是包含应用工厂；二是告诉Python flaskr 文件夹应当视作为一个包。
#可以在一个函数内部创建Flask 实例来代替创建全局实例
#所有应用相关的配 置、注册和其他设置都会在函数内部完成，然后返回这个应用。

import os
from flask import Flask

def create_app(test_config=None):
    # 创建和配置应用程序,创建Flask实例
    # __name__ 是当前Python模块的名称。应用需要知道在哪里设置路径，使用 __name__ 是一个方便的方法。
    # instance_relative_config=True告诉应用配置文件是相对于instancefolder的相对路径。
    # 实 例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当提交到版本控制系统。
    app = Flask(__name__, instance_relative_config=True)
    # 设置一个应用的默认配置
    # SECRET_KEY 是被Flask和扩展用于保证数据安全的。在开发过程中，为了方便可以设置为'dev' ，但是在发布的时候应当使用一个随机值来重载它。
    # DATABASE SQLite 数据库文件存放在路径。它位于 Flask 用于存放实例的app.instance_path 之内
    app.config.from_mapping( SECRET_KEY='dev',
                             DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
                             )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        # 使用 config.py 中的值来重载缺省配置，如果 config.py 存在的 话。
        # 例如，当正式部署的时候，用于设置一个正式的 SECRET_KEY 。
        # test_config 也会被传递给工厂，并且会替代实例配置。这样可以实现测试和开发的配置分离， 相互独立。
        app.config.from_pyfile('config.py', silent=True)
    else:
    # load the test config if passed in

        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    # 可以确保app.instance_path存在。Flask不会自动创建实例文件夹，
    # 但是必须确 保创建这个文件夹，因为SQLite数据库文件会被保存在里面。
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    # 后加入的二行代码
    #在工厂中导入并调用这个函数。在工厂函数中把新的代码放到函数的尾部，返回应用代码的前面。
    #$ flask init-db
    #  Initialized the database.

    from . import db
    db.init_app(app)

    return app
```

#### 4.初始化数据库文件

现在 init-db 已经在应用中注册好了，可以与 flask 命令一起使用了。使用的方式与前一页的 run 命令 类似。

```
$ flask init-db    Initialized the database
```



### 4.蓝图和视图

视图是一个应用对请求进行响应的函数。Flask通过模型把进来的请求URL匹配到对应的处理视图。视图返 回数据，Flask把数据变成出去的响应。Flask也可以反过来，根据视图的名称和参数生成URL。

#### 1.创建蓝图

是一种组织一组相关视图及其他代码的方式。与把视图及其他代码直接注册到应用的方式不同， 蓝图方式是把它们注册到蓝图，然后在工厂函数中把蓝图注册到应用。 

Flaskr有两个蓝图，一个用于**认证**功能，另一个用于博客帖子管理。每个蓝图的代码都在一个单独的模块中。 使用博客首先需要认证，因此我们先写认证蓝图。

flaskr/auth.py

```
import functools
from flask import ( Blueprint, flash, g, redirect, render_template, request, session, url_for )
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
# 这里创建了一个名称为 'auth' 的Blueprint (蓝图)
# 和应用对象一样，蓝图需要知道是在哪里定义的，因此把 __name__ 作为函数的第二个参数。
# url_prefix 会添加到所有与该蓝图关联的URL前面。
bp = Blueprint('auth', __name__, url_prefix='/auth')
```

flaskr/__init__.py

使用app.register_blueprint() 导入并注册蓝图。新的代码放在工厂函数的尾部返回应用之前。

```
# __init__.py 有两个作用：一是包含应用工厂；二是告诉Python flaskr 文件夹应当视作为一个包。
#可以在一个函数内部创建Flask 实例来代替创建全局实例
#所有应用相关的配 置、注册和其他设置都会在函数内部完成，然后返回这个应用。

import os
from flask import Flask

def create_app(test_config=None):
    # 创建和配置应用程序,创建Flask实例
    # __name__ 是当前Python模块的名称。应用需要知道在哪里设置路径，使用 __name__ 是一个方便的方法。
    # instance_relative_config=True告诉应用配置文件是相对于instancefolder的相对路径。
    # 实 例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当提交到版本控制系统。
    app = Flask(__name__, instance_relative_config=True)
    # 设置一个应用的默认配置
    # SECRET_KEY 是被Flask和扩展用于保证数据安全的。在开发过程中，为了方便可以设置为'dev' ，但是在发布的时候应当使用一个随机值来重载它。
    # DATABASE SQLite 数据库文件存放在路径。它位于 Flask 用于存放实例的app.instance_path 之内
    app.config.from_mapping( SECRET_KEY='dev',
                             DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
                             )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        # 使用 config.py 中的值来重载缺省配置，如果 config.py 存在的 话。
        # 例如，当正式部署的时候，用于设置一个正式的 SECRET_KEY 。
        # test_config 也会被传递给工厂，并且会替代实例配置。这样可以实现测试和开发的配置分离， 相互独立。
        app.config.from_pyfile('config.py', silent=True)
    else:
    # load the test config if passed in

        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    # 可以确保app.instance_path存在。Flask不会自动创建实例文件夹，
    # 但是必须确 保创建这个文件夹，因为SQLite数据库文件会被保存在里面。
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
 

    #使用app.register_blueprint() 导入并注册蓝图。新的代码放在工厂函数的尾部返回应用之前
    from . import auth
    app.register_blueprint(auth.bp)

    return app


```

#### **2.认证蓝图包括注册、登录和注销视图**。

##### 1.第一个视图，注册

当用访问 /auth/register URL 时，register 视图会返回用于填写注册内容的表单的 HTML 。当用户 提交表单时，视图会验证表单内容，然后要么再次显示表单并显示一个出错信息，要么创建新用户并显示登 录页面。 这里是视图代码，下一页会写生成HTML表单的模板

flaskr/auth.py

```
import functools
from flask import ( Blueprint, flash, g, redirect, render_template, request, session, url_for )
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
# 这里创建了一个名称为 'auth' 的Blueprint (蓝图)
# 和应用对象一样，蓝图需要知道是在哪里定义的，因此把 __name__ 作为函数的第二个参数。
# url_prefix 会添加到所有与该蓝图关联的URL前面。
# template_folder="sv_template",static_folder="sv_static"  可以指定这个蓝图的模板 
bp = Blueprint('auth', __name__, url_prefix='/auth')
# @bp.route 关联了 URL /register 和 register 视图函数。当 Flask 收到一个指向 /auth/ register 的请求时就会调用 register
# 视图并把其返回值作为响应
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        #request.form 是一个特殊类型的 dict ，其映射了提交表单的键和值。表单中，用户将会输入其 username 和 password
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        #验证username 和password不为空
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute( 'SELECT id FROM user WHERE username = ?', (username,) ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)
        if error is None:
            db.execute( 'INSERT INTO user (username, password) VALUES (?, ?)', (username, generate_password_hash(password)) )
            db.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')
```

##### 2.第二个视图登录

flaskr/auth.py

```
import functools
from flask import ( Blueprint, flash, g, redirect, render_template, request, session, url_for )
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
# 这里创建了一个名称为 'auth' 的Blueprint (蓝图)
# 和应用对象一样，蓝图需要知道是在哪里定义的，因此把 __name__ 作为函数的第二个参数。
# url_prefix 会添加到所有与该蓝图关联的URL前面。
bp = Blueprint('auth', __name__, url_prefix='/auth')
# @bp.route 关联了 URL /register 和 register 视图函数。当 Flask 收到一个指向 /auth/ register 的请求时就会调用 register
# 视图并把其返回值作为响应
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        #request.form 是一个特殊类型的 dict ，其映射了提交表单的键和值。表单中，用户将会输入其 username 和 password
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        #验证username 和password不为空
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute( 'SELECT id FROM user WHERE username = ?', (username,) ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)
        if error is None:
            db.execute( 'INSERT INTO user (username, password) VALUES (?, ?)', (username, generate_password_hash(password)) )
            db.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')



@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM user WHERE username = ?', (username,) ).fetchone()
        #首先需要查询用户并存放在变量中，以备后用。
        if user is None:
            error = 'Incorrect username.'
            #以相同的方式哈希提交的密码并安全的比较哈希值。如果匹配成功，那么 密码就是正确的。
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        if error is None:
            session.clear()
            # session 是一个 dict ，它用于储存横跨请求的值。当验证成功后，用户的 id 被储存于一个新的会 话中。
            # 会话数据被储存到一个向浏览器发送的 cookie 中，在后继请求中，浏览器会返回它。
            # Flask会安 全对数据进行签名以防数据被篡改。
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        #。flash() 用于储存在渲染模块时可以调用的信息。
        flash(error)
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    #注册一个在视图函数之前运 行的函数，不论其 URL 是什么。 load_logged_in_user 检查用户 id 是否已经储存在session 中，并从数据库中获取用户数据，
    #然后储存在g.user 中。g.user 的持续时间比请求要长。如果没有用户id，或者id不存在，那么 g.user 将 会是 None 。

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute( 'SELECT * FROM user WHERE id = ?', (user_id,) ).fetchone()

```

##### 3.注销：

flaskr/auth.py

```
#注销的时候需要把用户 id 从session 中移除。然后 #load_logged_in_user 就不会在后继请求中载入用户了。

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

##### 4.在其他视图中验证

flaskr/auth.py

用户登录以后才能创建、编辑和删除博客帖子。在每个视图中可以使用装饰器来完成这个工作

```
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
```

装饰器返回一个新的视图，该视图包含了传递给装饰器的原视图。新的函数检查用户是否已载入。如果已载 入，那么就继续正常执行原视图，否则就重定向到登录页面。我们会在博客视图中使用这个装饰器



##### 5.端点和URL

url_for() 函数根据视图名称和发生成URL。视图相关联的名称亦称为端点，缺省情况下，端点名称与视 图函数名称相同。
例如，前文被加入应用工厂的 hello() 视图端点为 'hello' ，可以使用 url_for('hello') 来连接。如 果视图有参数，后文会看到，那么可使用 url_for('hello', who='World') 连接。
当使用蓝图的时候，蓝图的名称会添加到函数名称的前面。上面的 login 函数的端点为 'auth.login' ， 因为它已被加入 'auth' 蓝图中





### 5.模板

#### 1.基础布局

flaskr/templates/base.html

```
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
    <h1>Flaskr</h1>
    <ul>
        {% if g.user %}
        <li><span>{{ g.user['username'] }}</span>
        <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
        {% else %}
        <li><a href="{{ url_for('auth.register') }}">Register</a>
        <li><a href="{{ url_for('auth.login') }}">Log In</a>
        {% endif %}
    </ul>
</nav>
<section class="content">
    <header>
        {% block header %}{% endblock %}
    </header>
    {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
    {% endfor %}
    {% block content %}{% endblock %}
</section>

```

```
在模板中自动可用。根据 g.user 是否被设置（在 load_logged_in_user 中进行），要么显示用户名和 注销连接，要么显示注册和登录连接。url_for() 也是自动可用的，可用于生成视图的URL，而不用手动 来指定。
在标题下面，正文内容前面，模板会循环显示get_flashed_messages() 返回的每个消息。在视图中使 用flash() 来处理出错信息，在模板中就可以这样显示出出来。
模板中定义三个块，这些块会被其他模板重载。
1. {% block title %} 会改变显示在浏览器标签和窗口中的标题。
2. {% block header %} 类似于 title ，但是会改变页面的标题。
3. {% block content %} 是每个页面的具体内容，如登录表单或者博客帖子。 其他模板直接放在 templates 文件夹内。为了更好地管理文件，属于某个蓝图的模板会被放在与蓝图同名 的文件夹内。

```

#### 2.注册

flaskr/templates/auth/register.html

```
{% extends 'base.html' %}


{% block header %}
`<h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}


{% block content %}
<form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
</form>
{% endblock %}


{% extends 'base.html' %} 告诉 Jinja 这个模板基于基础模板，并且需要替换相应的块。所有替换的 内容必须位于 {% block %} 标签之内。

```

#### 3.登录

flaskr/templates/auth/login.html

```
{% extends 'base.html' %}


{% block header %}
<h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}


{% block content %}
<form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
</form>
{% endblock %}
```

#### 4.注册一个用户

现在验证模板已写好，你可以注册一个用户了。请确定服务器还在运行（如果没有请使用 flask run ），然 后访问http://127.0.0.1:5000/auth/register。 在不填写表单的情况，尝试点击“Register”按钮，浏览器会显示出错信息。尝试在 register.html 中删除 required 属性后再次点击“Register”按钮。页面会重载并显示来自于视图中的flash() 的出错信息，而 不是浏览器显示出错信息。
填写用户名和密码后会重定向到登录页面。尝试输入错误的用户名，或者输入正常的用户名和错误的密码。 如果登录成功，那么会看到一个出错信息，因为还没有写登录后要转向的 index 视图。

### 6.静态文件

Flask自动添加一个 static 视图，视图使用相对于flaskr/static 的相对路径。

```
用了一个 style.css 文件连接：
{{ url_for('static', filename='style.css') }}

```





### 7.博客蓝图

#### 1.蓝图

定义蓝图并注册到应用工厂。



博客蓝图与验证蓝图所使用的技术一样。博客页面应当列出所有的帖子，允许已登录用户创建帖子，并允许 帖子作者修改和删除帖子。 当你完成每个视图时，请保持开发服务器运行。当你保存修改后，请尝试在浏览器中访问 URL ，并进行测 试。

flask/blog.py

```
from  flask  import(
Blueprint,flash,g,redirect,render_template,request,url_for
)
from  werkzeug.exceptions import abort

from  flaskr.auth import login_required
from flaskr.db import  get_db
bp = Blueprint('blog',__name__)
```

使用app.register_blueprint() 在工厂中导入和注册蓝图。将新代码放在工厂函数的尾部，返回应用 之前。

```
# __init__.py 有两个作用：一是包含应用工厂；二是告诉Python flaskr 文件夹应当视作为一个包。
#可以在一个函数内部创建Flask 实例来代替创建全局实例
#所有应用相关的配 置、注册和其他设置都会在函数内部完成，然后返回这个应用。

import os
from flask import Flask

def create_app(test_config=None):
    # 创建和配置应用程序,创建Flask实例
    # __name__ 是当前Python模块的名称。应用需要知道在哪里设置路径，使用 __name__ 是一个方便的方法。
    # instance_relative_config=True告诉应用配置文件是相对于instancefolder的相对路径。
    # 实 例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当提交到版本控制系统。
    app = Flask(__name__, instance_relative_config=True)
    # 设置一个应用的默认配置
    # SECRET_KEY 是被Flask和扩展用于保证数据安全的。在开发过程中，为了方便可以设置为'dev' ，但是在发布的时候应当使用一个随机值来重载它。
    # DATABASE SQLite 数据库文件存放在路径。它位于 Flask 用于存放实例的app.instance_path 之内
    app.config.from_mapping( SECRET_KEY='dev',
                             DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
                             )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        # 使用 config.py 中的值来重载缺省配置，如果 config.py 存在的 话。
        # 例如，当正式部署的时候，用于设置一个正式的 SECRET_KEY 。
        # test_config 也会被传递给工厂，并且会替代实例配置。这样可以实现测试和开发的配置分离， 相互独立。
        app.config.from_pyfile('config.py', silent=True)
    else:
    # load the test config if passed in

        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    # 可以确保app.instance_path存在。Flask不会自动创建实例文件夹，
    # 但是必须确 保创建这个文件夹，因为SQLite数据库文件会被保存在里面。
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    # 后加入的二行代码
    #在工厂中导入并调用这个函数。在工厂函数中把新的代码放到函数的尾部，返回应用代码的前面。
    #$ flask init-db
    #  Initialized the database.
    from . import db
    db.init_app(app)

    #使用app.register_blueprint() 导入并注册蓝图。新的代码放在工厂函数的尾部返回应用之前
    from . import auth
    app.register_blueprint(auth.bp)

 #注册博客蓝图
    from . import blog
    app.register_blueprint(blog.bp)
    #，博客蓝图没有 url_prefix
    app.add_url_rule('/',endpoint='index')
    return app


```

与验证蓝图不同，博客蓝图没有 url_prefix 。因此 index 视图会用于 / ，create 会用于 /create ，以 此类推。博客是Flaskr的主要功能，因此把博客索引作为主索引是合理的。 但是，下文的 index 视图的端点会被定义为 blog.index 。一些验证视图会指定向普通的 index 端 点。我们使用app.add_url_rule() 关联端点名称 'index' 和 / URL ，这样 url_for('index') 或 url_for('blog.index') 都会有效，会生成同样的 / URL。 在其他应用中，可能会在工厂中给博客蓝图一个 url_prefix 并定义一个独立的 index 视图，类似前文中 的 hello 视图。在这种情况下 index 和 blog.index 的端点和URL会有所不同。

#### 2.索引

索引会显示所有帖子，最新的会排在最前面。为了在结果中包含 user 表中的作者信息，使用了一个 JOIN   **通过数据库索引来进行排列显示的**

#### 3.博客蓝图的增删改查

flaskr/blog.py

```
from  flask  import(
Blueprint,flash,g,redirect,render_template,request,url_for
)
from  werkzeug.exceptions import abort

from  flaskr.auth import login_required
from flaskr.db import  get_db
bp = Blueprint('blog',__name__)
# 登录成功到index界面
@bp.route('/')
def index():
    db=get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id' 
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html',posts=posts)


#create 视图与 register 视图原理相同。要么显示表单，要么发送内容已通过验证且内容已加入数据库， 或者显示一个出错信息。
@bp.route('/create', methods=('GET', 'POST'))
#用户必须登录
@login_required
def create():
    if  request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        if  not title:
            error ='Title is required'
        if  error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)' ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')


def get_post(id,check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username' 
        ' FROM post p JOIN user u ON p.author_id = u.id' 
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()
    if post is  None:
        abort(404,"Post id {0} doesn't exist.".format(id))

    if  check_author and  post['author_id']!=g.user['id']:
        abort(403)
    return  post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        if not title:
            error = 'Title is required.'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute( 'UPDATE post SET title = ?, body = ?' ' WHERE id = ?', (title, body, id) )
            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))


```

#### 4.博客蓝图的html

**create**

```
{% extends 'base.html' %}
{% block header %}
<h1>{% block title %}New Post{% endblock %}</h1>
{% endblock %}

{% block content %}
<form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
    </form>
{% endblock %}

```

**index.html**

```
{% extends 'base.html' %}

{% block header %}
<h1>{% block title %}Posts{% endblock %}</h1>
{% if g.user %}
<a class="action" href="{{ url_for('blog.create') }}">New</a>
{% endif %}
{% endblock %}

{% block content %}
{% for post in posts %}
<article class="post">
    <header>
        <div>
            <h1>{{ post['title'] }}</h1>
            <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
        <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
    </header>
    <p class="body">{{ post['body'] }}</p>
    </article>
{% if not loop.last %}
    <hr>
{% endif %}
{% endfor %}
{% endblock %}

```

**update.html**

```
{% extends 'base.html' %}
{% block header %}
<h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
<form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
           value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
</form>
<hr>
<form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
    </form>

{% endblock %}

```



### 8.项目可安装化

项目可安装化是指创建一个项目 发行文件，以使用项目可以安装到其他环境，就像在你的项目中安装Flask 一样。这样可以使你的项目如同其他库一样进行部署，可以使用标准的Python工具来管理项目。 可安装化还可以带来如下好处，这些好处在教程中可以不太明显或者初学者可能没注意到： 

• 现在，Python和Flask能够理解如何 flaskr 包，是因为你是在项目文件夹中运行的。可安装化后，可 以从任何地方导入项目并运行。 • 可以和其他包一样管理项目的依赖，即使用**pip install yourproject.whl**来安装项目并安装相 关依赖。

 • 测试工具可以分离测试环境和开发环境

#### 1.描述项目

setup.py 文件描述项目及其从属的文件。

```
from setuptools import find_packages, setup
setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[ 'flask',
                       ],
)

```

packages 告诉 Python 包所包括的文件夹（及其所包含的 Python 文件）。find_packages() 自动找到这 些文件夹，这样就不用手动写出来。为了包含其他文件夹，如静态文件和模板文件所在的文件夹，需要设置 include_package_data 。Python还需要一个名为 MANIFEST.in 文件来说明这些文件有哪些

 **MANIFEST.in**



```
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

这告诉 Python 复制所有 static 和 templates 文件夹中的文件，schema.sql 文件，但是排除所有字节 文件。



#### 2.安装项目

使用 pip 在虚拟环境中安装项目。

```
pip install -e .
```

这个命令告诉pip在当前文件夹中寻找 setup.py 并在 编辑或 开发模式下安装。编辑模式是指当改变本地 代码后，只需要重新项目。比如改变了项目依赖之类的元数据的情况下。
可以通过 pip list 来查看项目的安装情况。

### 9.测试覆盖

为应用写单元测试可以检查代码是否按预期执行。Flask 提供了测试客户端，可以模拟向应用发送请求并返 回响应数据。
应当尽可能多地进行测试。函数中的代码只有在函数被调用的情况下才会运行。分支中的代码，如 if 块中 的代码，只有在符合条件的情况下才会运行。测试应当覆盖每个函数和每个分支。 越接近100%的测试覆盖，越能够保证修改代码后不会出现意外。但是100%测试覆盖不能保证应用没有错 误。通常，测试不会覆盖用户如何在浏览器中与应用进行交互。尽管如此，在开发过程中，测试覆盖仍然是 非常重要的。

我们使用pytest和coverage来进行测试和衡量代码。先安装它

```
pip install pytest coverage

```

#### 1.配置和固件

测试代码位于 tests 文件夹中，该文件夹位于 flaskr 包的旁边，而不是里面。tests/conftest.py 文 件包含名为 ﬁxtures （固件）的配置函数。每个测试都会用到这个函数。测试位于Python模块中，以 test_ 开头，并且模块中的每个测试函数也以 test_ 开头。 每个测试会创建一个新的临时数据库文件，并产生一些用于测试的数据。写一个SQL文件来插入数据。

##### **1.tests/data.sql**

```
INSERT INTO user (username, password)
VALUES
('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created) VALUES
('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```



##### **2.tests/conftest.py**

```
import os
import tempfile
import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db
with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')
@pytest.fixture
def app():
    # 创建并打开一个临时文件，返回该文件对象和路径。DATABASE 路径被重载，这样 它会指向临时路径，而不是实例文件夹。设置好路径之后，数据库表被创建，
    # 然后插入数据。测试结束后，临 时文件会被关闭并删除。

    db_fd, db_path = tempfile.mkstemp()
    # ESTING告诉 Flask 应用处在测试模式下。Flask 会改变一些内部行为以方便测试。其他的扩展也可以使用 这个标志方便测试。
    app = create_app({ 'TESTING': True, 'DATABASE': db_path, })
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)
    yield app
    os.close(db_fd)
    os.unlink(db_path)
@pytest.fixture
#client 固件调用app.test_client() 由 app 固件创建的应用对象。测试会使用客户端来向应用发送请 求，而不用启动服务器。
def client(app):
    return app.test_client()
@pytest.fixture
#runner固件类似于client。app.test_cli_runner()创建一个运行器，可以调用应用注册的Click命 令。
def runner(app):
    return app.test_cli_runner()

```

##### 3.简单测试案例tests/test_factory.py

```

#Pytest 通过匹配固件函数名称和测试函数的参数名称来使用固件。例如下面要写 test_hello 函数有一个 client 参数。Pytest会匹配 client 固件函数，
# 调用该函数，把返回值传递给测试函数

from flaskr import create_app
def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

#### 2.数据库

在一个应用环境中，每次调用 get_db 都应当返回相同的连接。退出环境后，连接应当已关闭

##### **1.tests/test_db.py**

```
import sqlite3
import pytest
from flaskr.db import get_db
# 在一个应用环境中，每次调用 get_db 都应当返回相同的连接。退出环境后，连接应当已关闭。
def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()
    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')
    assert 'closed' in str(e.value)
#init-db 命令应当调用 init_db 函数并输出一个信息。

def test_init_db_command(runner, monkeypatch):
    class Recorder(object): called = False
    def fake_init_db():
        Recorder.called = True
    #这个测试使用Pytest’s monkeypatch 固件来替换 init_db 函数。前文写的 runner 固件用于通过名称调 用 init-db 命令。

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called

```

#### 3.验证

对于大多数视图，用户需要登录。在测试中最方便的方法是使用客户端制作一个POST请求发送给login视 图。与其每次都写一遍，不如写一个类，用类的方法来做这件事，并使用一个固件把它传递给每个测试的客 户端。

#####  1.tests/conftest.py

```
#对于大多数视图，用户需要登录。
# 在测试中最方便的方法是使用客户端制作一个POST请求发送给login视 图。
# 与其每次都写一遍，不如写一个类，用类的方法来做这件事，并使用一个固件把它传递给每个测试的客 户端。

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            #通过 auth 固件，可以在调试中调用 auth.login() 登录为 test 用户。这个用户的数据已经在 app 固件 中写入了数据。
            '/auth/login',
            data={'username': username,'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')
```



register 视图应当在 GET 请求时渲染成功。在 POST 请求中，表单数据合法时，该视图应当重定向到登录 URL，并且用户的数据已在数据库中保存好。数据非法时，应当显示出错信息。

##### 2.tests/test_auth.py

```
import pytest
from flask import g, session
from flaskr.db import get_db
# register 视图应当在 GET 请求时渲染成功。在 POST 请求中，表单数据合法时，该视图应当重定向到登录 URL，
# 并且用户的数据已在数据库中保存好。数据非法时，应当显示出错信息
def test_register(client, app):
    #client.get() 制作一个 GET 请求并由 Flask 返回Response 对象。类似的 client.post() 制作一个 POST 请求，转换 data 字典为表单数据。
    #为了测试页面是否渲染成功，制作一个简单的请求，并检查是否返回一个 200 OK status_code 。如果渲 染失败，Flask会返回一个 500 Internal Server Error 代码。
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'} )
    #当注册视图重定向到登录视图时，headers 会有一个包含登录URL的 Location 头部。
    assert 'http://localhost/auth/login' == response.headers['Location']
    with app.app_context():
        assert get_db().execute( "select * from user where username = 'a'",
                                 ).fetchone() is not None


#pytest.mark.parametrize 告诉Pytest以不同的参数运行同一个测试。这里用于测试不同的非法输入和 出错信息，避免重复写三次相同的代码。
@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('', '', b'Username is required.'),
        ('a', '', b'Password is required.'),
        ('test', 'test', b'already registered'),
))



def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password} )
    assert message in response.data



# login 视图的测试与 register 的非常相似。后者是测试数据库中的数据，前者是测试登录之后session 应当包含 user_id 。
def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'
    #在 with 块中使用 client ，可以在响应返回之后操作环境变量，比如session 。通常，在请求之外操作 session 会引发一个异常
    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'
@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('a', 'test', b'Incorrect username.'),
        ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data



#logout 测试与 login 相反。注销之后，session 应当不包含 user_id 。

def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session

```

#### 4.博客

##### 1. tests/test_blog.py

```
import pytest
from flaskr.db import get_db
def test_index(client, auth):
    response = client.get('/')
    #当没有登录时，每个页面显示登录或注册连接。
    assert b"Log In" in response.data
    assert b"Register" in response.data
    #当登录之 后，应当有一个注销连接。
    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data


@pytest.mark.parametrize('path', ( '/create', '/1/update', '/1/delete', ))
def test_login_required(client, path):
    response = client.post(path)
    #用户必须登录后才能访问 create 、update 和 delete
    assert response.headers['Location'] == 'http://localhost/auth/login'
def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()
    auth.login()
    # 当前用户不能修改其他用户的帖子
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403

    #当前用户看不到编辑链接
    assert b'href="/1/update"' not in client.get('/').data

@pytest.mark.parametrize('path', ( '/2/update', '/2/delete', ))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404



def test_create(client, auth, app):
    auth.login()
    #对于 GET 请求，create 和 update 视图应当渲染和返回一个 200 OK 状态码。
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})
    #with 代表并且
    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2

def test_update(client, auth, app):
    auth.login()
    #对于 GET 请求，create 和 update 视图应当渲染和返回一个 200 OK 状态码。
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})
    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'

@pytest.mark.parametrize('path',(
        '/create', '/1/update',
))
def test_create_update_validate(client, auth,path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data


#delete 视图应当重定向到索引URL，并且帖子应当从数据库中删除。

def test_delete(client, auth, app):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers['Location'] == 'http://localhost/'
    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None


```

#### 5.运行测试

使用 pytest 来运行测试。该命令会找到并且运行所有测试

```
$  pytest
```

可以使用 coverage 命令代替直接使用pytest来运行测试，这样可以衡量测试覆盖率。

```
$ coverage run -m pytest

```

还可以生成HTML报告，可以看到每个文件中测试覆盖了哪些行：

```
coverage html
```

### 10.部署产品

#### 1.构建和安装

当需要把应用部署到其他地方时，需要构建一个发行文件。当前Python的标准发行文件是 wheel 格式的，扩 展名为 .whl 。先确保已经安装好wheel库：

```
$ pip install wheel

```

用 Python 运行 setup.py 会得到一个命令行工具，以使用构建相关命令。bdist_wheel 命令会构建一个 wheel发行文件。

```
$ python setup.py bdist_wheel
```

构建的文件为 dist/flaskr-1.0.0-py3-none-any.whl 。文件名由项目名称、版本号和一些关于项目 安装要求的标记组成。
复制这个文件到另一台机器，创建一个新的虚拟环境，然后用 pip 安装这个文件。

```
 $ pip install flaskr-1.0.0-py3-none-any.whl

```

Pip会安装项目和相关依赖。 既然这是一个不同的机器，那么需要再次运行 init-db 命令，在实例文件夹中创建数据库。

```
$ export FLASK_APP=flaskr 
$ flask init-db

```

#### 2.配置密钥

在教程开始的时候给了SECRET_KEY 一个缺省值。在产品中我们应当设置一些随机内容。否则网络攻击者就 可以使用公开的 'dev' 键来修改会话cookie，或者其他任何使用密钥的东西。 可以使用下面的命令输出一个随机密钥：

```
$ python -c 'import os; print(os.urandom(16))'
b'_5#y2L"F4Q8z\n\xec]/'

```

在实例文件夹创建一个 config.py 文件。工厂会读取这个文件，如果该文件存在的话。提制生成的值到该 文件中。

**venv/var/flaskr-instance/config.py**

```
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

```

其他必须的配置也可以写入该文件中。Flaskr只需要 SECRET_KEY 即可。

#### 3.运行产品服务器

当运行公开服务器而不是进行开发的时候，应当不使用内建的开发服务器（flask run ）。开发服务器由 Werkzeug提供，目的是为了方便开发，但是不够高效、稳定和安全。 替代地，应当选用一个产品级的WSGI服务器。例如，使用Waitress。首先在虚拟环境中安装它：

```
$ pip install waitress

```

需要把应用告知Waitree，但是方式与 flask run 那样使用 FLASK_APP 不同。需要告知Waitree导入并调 用应用工厂来得到一个应用对象。

```
$ waitress-serve --call 'flaskr:create_app'
Serving on http://0.0.0.0:8080

```





## 三.模板

视图函数的主要作用是生成请求的响应，这是最简单的请求。实际上，视图函数有两个作用：处理业务逻辑和返回响应内容。在大型应用中，把业务逻辑和表现内容放在一起，会增加代码的复杂度和维护成本。本节学到的模板，它的作用即是承担视图函数的另一个作用，即返回响应内容。

```
模板其实是一个包含响应文本的文件，其中用占位符(变量)表示动态部分，告诉模板引擎其具体的值需要从使用的数据中获取
使用真实值替换变量，再返回最终得到的字符串，这个过程称为“渲染”
Flask是使用 Jinja2 这个模板引擎来渲染模板
```

**使用模板的好处：**

```
视图函数只负责业务逻辑和数据处理(业务逻辑方面)
而模板则取到视图函数的数据结果进行展示(视图展示方面)
代码结构清晰，耦合度低
```

**Jinja2 两个概念：**

```
Jinja2：是 Python 下一个被广泛应用的模板引擎，是由Python实现的模板语言，他的设计思想来源于 Django 的模板引擎，并扩展了其语法和一系列强大的功能，其是Flask内置的模板语言。
模板语言：是一种被设计来自动生成文档的简单文本格式，在模板语言中，一般都会把一些变量传给模板，替换模板的特定位置上预先定义好的占位变量名。
官方文档
```

**渲染模版函数**

```
Flask提供的 render_template 函数封装了该模板引擎
render_template 函数的第一个参数是模板的文件名，后面的参数都是键值对，表示模板中变量对应的真实值。
```

**使用**

```
{{}} 来表示变量名，这种 {{}} 语法叫做变量代码块

<h1>{{ post.title }}</h1>
```



### 1.注释

```
使用 {# #} 进行注释，注释的内容不会在html中被渲染出来
```

### 2.模板demo

#### 1.app.py

```
# https://blog.csdn.net/troysps/article/details/80466916
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    list1 = list(range(10))
    my_list = [{"id": 1, "value": "我爱工作"},
               {"id": 2, "value": "工作使人快乐"},
               {"id": 3, "value": "沉迷于工作无法自拔"},
               {"id": 4, "value": "日渐消瘦"},
               {"id": 5, "value": "以梦为马，越骑越傻"}]
    your_list = [{"id": 1, "value": "我爱工作"},
               {"id": 2, "value": "工作使人快乐"},
               {"id": 3, "value": "沉迷于工作无法自拔"},
               { "value": "日渐消瘦"},
               { "value": "以梦为马，越骑越傻"}]

    post={'name': 'liyanliang','liyanliang':'26','nianling':'94','94':'建军节'}

    #动态传值
    #传字符串
    param_str = '我是字符串传值'
    #传列表
    param_list = [1,2,3,4]
    #传字典
    param_dict = {
        'name': 'weiming',
        'age':18
    }
    return render_template(
        # 渲染模板语言
        'index.html',
        title='hello world',
        list2=list1,
        my_list=my_list,
        name =post,
        param_str = param_str,
        param_list = param_list,
        param_dict = param_dict,
        your_list=your_list

    )


# step1 定义过滤器
def do_listreverse(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li

# step2 添加自定义过滤器
app.add_template_filter(do_listreverse, 'listreverse')



if __name__ == '__main__':
    app.run(debug=True)


```

#### 2.index.html

```
#.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
      <title>Title</title>
</head>
<body>
    <h3>{{ name.name }}</h3>
    <h1>{{title | reverse | upper}}</h1>
    <h2>{{"hello world" | reverse | upper}}</h2>
    <h4>{{list2 | last}}</h4>

    <br>
    {{list2 | listreverse }}
    <br>
    <ul>
        {% for item in my_list %}
        <li>{{item.id}}----{{item.value  }}</li>
        {% endfor %}
    </ul>

    {% for item in my_list %}
        {% if loop.index==1 %}
            <li style="background-color: red;">{{ loop.index }}--{{ item.get('value') }}</li>
        {% elif loop.index==2 %}
            <li style="background-color: blue;">{{ loop.index }}--{{ item.get('value') }}</li>
        {% elif loop.index==3 %}
            <li style="background-color: green;">{{ loop.index }}--{{ item.get('value') }}</li>
        {% else %}
            <li style="background-color: yellow;">{{ loop.index }}--{{ item.get('value') }}</li>
        {% endif %}
    {% endfor %}

 {#  动态传值 #}
{{param_str}}
<br>
{{param_list}}
<br>
{{param_list.0}}
<br>
{{param_list[-1]}}
<hr>
姓名:{{param_dict['name']}}
<hr>
年龄:{{param_dict['age']}}
param_dict{{ param_dict}}


<hr>
{# 控制代码块 #}
{% for index  in param_list %}
{{index}}
{% endfor %}

<hr>
if的使用方法
{% for  param  in  param_list %}
{% if  param  <3 %}
{{ param }}
{% endif %}
{% endfor %}

    {# 常见内建过滤器 #}

    {# 字符串操作  #}
<!--  safe：禁用转义  -->
    <p>{{ '<em>hello</em>'  | safe}}</p>

<!--capitalize 把变量值的首字母转成大写，其余转成小写-->
<!--    lower: 把值转成小写-->
<!--    upper: 把值转成大写-->
<!--    title: 把值中的每个单词首字母大写-->
    <p>{{'hello asdasdasdas' | capitalize}}</p>

<p>{{title | capitalize}}</p>
    <p>{{'hello asdasdasdas' | title}}</p>
<!--reverse 字符串反转-->
    <p>{{'hello asdasdasdas' | reverse}}</p>
<!--format 格式化输出-->
    <p>{{ '%s is %d' | format('name',17)}}</p>
<!--渲染之前把值中所有的HTML标签都删掉-->
<p>{{ '<em>hello</em>' |safe  }}</p>
<!--字符串截断-->
<p>{{ 'hello every one' | truncate(9)}}</p>


{# 列表操作 #}
<!--    取第一个元素 -->
<p> {{  my_list | first}}</p>
<!--取最后一个元素-->
<p> {{  my_list | last}}</p>
<!--获取列表长度-->
<p> {{  my_list | length}}</p>
<!--   列表求和   sum-->
<p> {{  list2 | sum}}</p>
<!--列表排序-->
<p> {{  [1,2,3,100,5,6] | sort}}</p>

<hr>


{# 循环语句 #}

{% for post in my_list %}

        <h1>{{ post.id }}------

        {{post.value}}</h1>
<!--        <p>{{ post.name | upper }}</p>-->

{% endfor %}


    {# 循环+判断 #}
{% for post in your_list if post.id %}

        <h1>{{ post.id }}------
        {{post.value}}</h1>
<!--        <p>{{ post.name | upper }}</p>-->

{% endfor %}



</body>
</html>
```



### 3.模板继承

#### 1.base.html（基模板）

```
顶文和底文都一样的代码 中间留好填充的块
{% block content %}
{% endblock  %}
```

#### 2.son.html（子模板）

```
{% extends "base.html" %}
.....
#  上下block的块的名 要一样 
{% block content %}
中间写内容 
{% endblock}
.....

```

模板继承使用时注意点：



1. 不支持多继承，但是支持多层继承
2. 为了便于阅读，在子模板中使用extends时，尽量写在模板的第一行。
3. 不能在一个模板文件中定义多个相同名字的block标签。
4. 当在页面中使用多个block标签时，建议给结束标签起个名字，当多个block嵌套时，阅读性更好。

## 四.入门进阶实例

**摘自各种技术博客文档**

### 1.基于蓝图的一个小实例写法

#### 1.redirect跳转

##### 1.参数是url形式

app.py  相当于manage.py

```
from flask import Flask

# 导入此前写好的蓝图模块
import blue

app = Flask(__name__)  # type:Flask

# 在Flask对象中注册蓝图模块中的蓝图对象 blue 中的 bl
app.register_blueprint(blue.bl)

app.run()
# 现在Flask对象中并没有写任何的路由和视图函数
```



blue.py

```
from  flask import  Blueprint,render_template
#实例化一个蓝图(Blueprint)对象
bl = Blueprint("first",__name__)


from  flask   import  redirect
@bl.route('/redirect/')
def make_redirect():
    return redirect('/hello/index/')


from  flask import  make_response
@bl.route('/hello/index/')
def  test_page():
    return  render_template("baibai.html")
```





##### 2.参数是name.name

app.py相当于 manage.py  

```
from flask import Flask

# 导入此前写好的蓝图模块
import blue

app = Flask(__name__)  # type:Flask

# 在Flask对象中注册蓝图模块中的蓝图对象 blue 中的 bl
app.register_blueprint(blue.bl)

app.run()
# 现在Flask对象中并没有写任何的路由和视图函数
```

蓝图目录可以相同blue.py

```
from  flask import  Blueprint,render_template
#实例化一个蓝图(Blueprint)对象
bl = Blueprint("first",__name__)
@bl.route("/index/")
def  index():
    return render_template('hello.html')


from  flask  import  redirect ,url_for
# 这里添加路由和视图函数的时候与在Flask对象中添加是一样的
@bl.route('/redirect/')
def  make_redirect():
    #参数是name.name  就是蓝图名。函数方法名
    return  redirect(url_for( 'first.index'))
```



### 2.蓝图多个app注册实例

#####  1.目录结构:/项目名/templates

**templates/蓝图模板 都OK!,总而言之外面的都是平级的**

##### 					2./项目名/manage.py  （主app）

```
from  flask   import  Flask,render_template
from  product import  product
from   user  import  user
app = Flask(__name__)
app.register_blueprint(product)
app.register_blueprint(user)
@app.route('/')
def  index():
    return  render_template('hello.html')
if __name__ == '__main__':
    app.run()
```

##### 					3./项目名/蓝图.py（子app）

 **/项目名/蓝图文件夹/蓝图.py  也OK！**

```
#蓝图product.py
from  flask import Flask,Blueprint,render_template

product = Blueprint('product',__name__,)

@product.route('/product/')
def  product_index():
    return  render_template('product.html')

```

### 3.flask链接数据库（基于应用APP,未分离）

#### **1.安装 **

##### 1.安装mysql服务在服务器上或者是本机

#### 2.安装依赖库

```
$ pip  install flask_sqlalchemy

```

#### 3.配置文件config.py

```

#数据库类型
DIALECT = 'mysql'


#数据库的驱动
DRIVER = 'pymysql'


#数据库的用户名
USERNAME = 'root'


#数据库密码
PASSWORD = 'lyl123456'

HOST = 'localhost'  

#数据库的端口号
PORT = '3306'

#连接的数据库名称
DATABASE = 'demo'



SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

```



#### 4.代码实例

```
from  flask import  Flask,render_template,jsonify
from flask_sqlalchemy import  SQLAlchemy


import  config
app = Flask(__name__)


#配置数据库
app.config.from_object(config)
db = SQLAlchemy(app)
class Article(db.Model):
    __tablename__='article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title =db.Column(db.String(100),nullable=False)
    content =db.Column(db.Text,nullable=False)


class Person(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(30),
        nullable=False,
        unique=True,
    )
    age = db.Column(
        db.Integer,
        default=1
    )


db.create_all()

@app.route('/')
def index():
    return  render_template('2.html')


@app.route("/create_data")
def create_user():
    u = Person(
        name="liyanliang"
    )
    db.session.add(u)
    db.session.commit()

@app.route("/create_many")
def create_many():
    persons = []
    for  i  in  range(10):
        u =Person(
            name="asdasd"+str(i)
        )
        persons.append(u)
    db.session.add_all(persons)
    db.session.commit()
    print(persons)
    return  "创建完毕"

@app.route("/get_users")
def get_users():
    res = Person.query.all()
    for i in res:
        return "ok"


if __name__ == '__main__':
    app.run()
```





### 4.基于包结构的模块导入

首先在当前目录FlaskPath下创建一个包project,project会自带一个包文件__init__.py,需要在里面初始化app和实例化数据库

然后在包project目录下创建models.py 创建对应数据库的Python语句，创建类及对应的属性字段，通过orm的sqlalchem模块实现创建数据库中对应的表以及对应的字段的关系映射

创建views.py文件 ，这一部分相当于django中的路由加视图，在这里可以实现对数据库的增删改查操作，相应服务器请求以返回相对应的数据

创建main.py文件，启动app

#### 1./project/__init__.py

```
from flask import Flask

#实例化App
app = Flask(__name__)

# 配置好数据库
from flask_sqlalchemy import SQLAlchemy


app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:lyl123456@localhost:3306/mydb?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#实例化数据库
db = SQLAlchemy(app)

```

#### 2./project/views.py

```
from project import app

from project.models import db  # 这个db导入之前一定是执行过数据库同步的

from project.models import Student

session = db.session  # 这里的db实例已经执行过数据库同步



@app.route("/")
def inedx():
    student = Student(name="老边", age="18", gender="男", classes="python")

    session.add(student)

    session.commit()

    #返回值一定要有
    return "hello world"

@app.route("/cha")
def  cha():
    students = Student.query.all()
    
    print(students)
    return  'ok'

```

#### 3./project/main.py

```
import sys

from project.views import app

from project.models import db

command = input('请输入执行命令:')

if command == 'runserver':

    app.run()


elif command == 'migrate':

    db.create_all()

```

#### 3.project/models.py

```


from project import db



class Student(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    name = db.Column(db.String(32))

    age = db.Column(db.Integer)

    gender = db.Column(db.String(32))

    classes = db.Column(db.String(32))



    def __repr__(self):

        return self.name

```



### 5. flask-sqlalchemy用法详解

#### 1. 一对多实例

**一对父母，对应多个孩子**

##### 1.目录结构/摘自基于包结构的

##### 2.views.py

```

'''
一对多视图部分
'''
#增
@app.route("/insert")
def  in_sert_data():
    p1 = Parent(name='p1')
    c1 = Child('c1')
    c2 = Child('c2')
    p1.children = [c1, c2]
    db.session.add(p1)
    db.session.commit()
    return  'ok'

#改
@app.route("/modify")
def  modify():
    #先查询出需要修改的条目
    # p = db.session.query(Parent).get(1)
    # p.name='p2'
    # db.session.commit()

    #或者直接用一条语句：直接查询出后修改，update采用字典修改{修要修改的列：'修改后的值'}
    db.session.query(Child).filter(Child.id==1).update({Child.name:'c3'})
    db.session.commit()
    return '修改成功c3'

#删
@app.route('/delete')
def delete():
    c = db.session.query(Child).filter(Child.id==2).first()
    db.session.delete(c)
    db.session.commit()
    return  '删除孩子id'

#查
@app.route('/cha')
def  cha():
    #查询孩子的爸爸 反向查询
    # res = session.query(Child).filter(Child.name=='c3').first().parent
    # 或者 ，但是我这边暂时报错 ，还没理解
    # Child.query.filter(Child.name == 'c1').parent
    #查询爸爸的孩子  正向查询
    res =session.query(Parent).filter(Parent.name=='p1').first().children
    print(res)
    return  'ok'
```

##### 3.models.py

```


# 针对Flask-SAlchemy 的学习记录测试

'''

一对多 模型部分
'''
#一对多 一个父母有多个孩子   //一对多 定义到多的那边
class Parent(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    #                                  反向查询
    children=db.relationship("Child",backref="parent")
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "name is %r" %self.name


class Child(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    #关联字段
    parent_id=db.Column(db.Integer,db.ForeignKey('parent.id'))
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "name is %r" % self.name


```



#### 2.一对一实例

**身份证和人名**

一对一需要设置relationship中的uselist=Flase，其他数据库操作一样。



#### 3.多对多实例

例子:频道和卫视      

**频道：央视频道 卫视频道**

**卫视：CCTV-1  CCTV-2  湖南卫视 江苏卫视 浙江卫视  翡翠电视台 TVB**

##### 1.views.py

```
from project import app

from project.models import db  # 这个db导入之前一定是执行过数据库同步的

from project.models import Tag,Channel
from  flask import  jsonify

session = db.session  # 这里的db实例已经执行过数据库同步

@app.route('/')
def index():
   return 'ok'


'''
多对多视图部分
'''

@app.route('/insert')
def insert():
    tag1 =Tag(name='央视频道')
    tag2 =Tag(name='卫视频道')
    cha1 =Channel(name='北京卫视')
    cha2 = Channel(name='湖南卫视')
    cha3 = Channel(name='CCTV-10')
    cha4 = Channel(name='CCTV-15')
    tag1.channels.append(cha3)
    tag1.channels.append(cha4)
    tag2.channels.append(cha1)
    tag2.channels.append(cha2)
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(cha1)
    db.session.add(cha2)
    db.session.add(cha3)
    db.session.add(cha4)
    # db.session.add()
    db.session.commit()
    return 'ok'


@app.route('/get_channelinfo_by_tagname')
#通过频道查卫视
def get_channelinfo_by_tagname():
    tag = Tag.query.filter_by(name='卫视频道',status=1).first()
    print(tag.channels)
    return '卫视频道有'


@app.route('/get_taginfo_by_channelname')
def get_taginfo_by_channelname():
    channel = Channel.query.filter_by(name = 'CCTV-10',status=1).first()
    if  channel.tag:
        print(channel.tag)
        return '查到了'
    else:
        return  '没查到'
```



##### 2.models.py

```
'''
多对多，模型部分，建立多对多的关系
'''
tag_channel = db.Table(
    'tag_channel', #数据库的表名
    db.Column('id',db.Integer,autoincrement=True,primary_key=True),

    #id进行关联
    db.Column('tid',db.Integer,db.ForeignKey('tag.id')),
    db.Column('cid',db.Integer,db.ForeignKey('channel.id'))
)


'''
一级分类   比如说 央视频道 卫视频道  港澳台频道

'''
class  Tag(db.Model):
    __tablename__ ='tag'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(32),nullable=False)
    status =db.Column(db.SmallInteger,default=1)
    addtime =db.Column(db.DateTime,default=datetime.now())
    update_time =db.Column(db.DateTime,default=datetime.now())
    #反向查询db.backref
    channels =db.relationship('Channel',backref = db.backref('tag'),secondary =tag_channel)

'''
二级分类   比如说 CCTV-1  CCTV-2  湖南卫视 江苏卫视 浙江卫视  翡翠电视台 TVB
'''

class  Channel(db.Model):
    __tablename__ ='channel'
    id =db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(32),nullable=False)
    status =db.Column(db.SmallInteger,default=1)
    addtime =db.Column(db.DateTime,default=datetime.now())
```



#### 4.flask-sqlachemy总结

##### 1.什么是ORM



##### 2.配置

| SQLALCHEMY_DATABASE_URI   | 用于连接的数据库 URI 。例如:sqlite:////tmp/test.dbmysql://username:password@server/db |
| ------------------------- | :----------------------------------------------------------- |
| SQLALCHEMY_BINDS          | 一个映射 binds 到连接 URI 的字典。更多 binds 的信息见[用 Binds 操作多个数据库](http://docs.jinkan.org/docs/flask-sqlalchemy/binds.html#binds)。 |
| SQLALCHEMY_ECHO           | 如果设置为Ture， SQLAlchemy 会记录所有 发给 stderr 的语句，这对调试有用。(打印sql语句) |
| SQLALCHEMY_RECORD_QUERIES | 可以用于显式地禁用或启用查询记录。查询记录 在调试或测试模式自动启用。更多信息见get_debug_queries()。 |
| SQLALCHEMY_NATIVE_UNICODE | 可以用于显式禁用原生 unicode 支持。当使用 不合适的指定无编码的数据库默认值时，这对于 一些数据库适配器是必须的（比如 Ubuntu 上 某些版本的 PostgreSQL ）。 |
| SQLALCHEMY_POOL_SIZE      | 数据库连接池的大小。默认是引擎默认值（通常 是 5 ）           |
| SQLALCHEMY_POOL_TIMEOUT   | 设定连接池的连接超时时间。默认是 10 。                       |
| SQLALCHEMY_POOL_RECYCLE   | 多少秒后自动回收连接。这对 MySQL 是必要的， 它默认移除闲置多于 8 小时的连接。注意如果 使用了 MySQL ， Flask-SQLALchemy 自动设定 这个值为 2 小时。 |

连接其他数据库

完整连接 URI 列表请跳转到 SQLAlchemy 下面的文档 ([Supported Databases](http://www.sqlalchemy.org/docs/core/engines.html)) 。这里给出一些 常见的连接字符串。

- Postgres:

```
postgresql://scott:tiger@localhost/mydatabase
```

- MySQL:

```
mysql://scott:tiger@localhost/mydatabase
```

- Oracle:

```
- oracle://scott:tiger@127.0.0.1:1521/sidname
```

- SQLite （注意开头的四个斜线）:

```
sqlite:////absolute/path/to/foo.db
```



##### 3.定义模型

###### 1.常用的SQLAlchemy字段类型

| 类型名       | python中类型      | 说明                                                |
| :----------- | :---------------- | :-------------------------------------------------- |
| Integer      | int               | 普通整数，一般是32位                                |
| SmallInteger | int               | 取值范围小的整数，一般是16位                        |
| BigInteger   | int或long         | 不限制精度的整数                                    |
| Float        | float             | 浮点数                                              |
| Numeric      | decimal.Decimal   | 普通整数，一般是32位                                |
| String       | str               | 变长字符串                                          |
| Text         | str               | 变长字符串，对较长或不限长度的字符串做了优化        |
| Unicode      | unicode           | 变长Unicode字符串                                   |
| UnicodeText  | unicode           | 变长Unicode字符串，对较长或不限长度的字符串做了优化 |
| Boolean      | bool              | 布尔值                                              |
| Date         | datetime.date     | 时间                                                |
| Time         | datetime.datetime | 日期和时间                                          |
| LargeBinary  | str               | 二进制文件                                          |

###### 2.常用的SQLAlchemy列选项

| 选项名      | 说明                                              |
| :---------- | :------------------------------------------------ |
| primary_key | 如果为True，代表表的主键                          |
| unique      | 如果为True，代表这列不允许出现重复的值            |
| index       | 如果为True，为这列创建索引，提高查询效率          |
| nullable    | 如果为True，允许有空值，如果为False，不允许有空值 |
| default     | 为这列定义默认值                                  |

###### 3.常用的SQLAlchemy关系选项

| 选项名         | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| backref        | 在关系的另一模型中添加反向引用                               |
| primary join   | 明确指定两个模型之间使用的联结条件                           |
| uselist        | 如果为False，不使用列表，而使用标量值                        |
| order_by       | 指定关系中记录的排序方式                                     |
| secondary      | 指定多对多关系中关系表的名字                                 |
| secondary join | 在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件 |



##### 4.sqlachemy多条件查询语句

#### 6. flask小项目开发实例（工厂模式）